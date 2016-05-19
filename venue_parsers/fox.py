from bs4 import BeautifulSoup
import re


def parse(page, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    table = soup.find('table', class_='concert_calendar')

    for entry in table.findAll('tr'):

        main_act = entry.find('span', class_='headliner')
        if main_act:
            prepender = main_act.find('span', class_='prepend')
            if prepender:
                headliner = prepender.findNextSibling()
                show = {'headliner': headliner.text}
            else:
                show = {'headliner': main_act.text}
            opening_act = entry.find('span', class_="warmup")
            if opening_act:
                if opening_act.text:
                    show['openers'] = opening_act.text
            show_date = entry.findChild()
            show['date'] = re.sub('\,', ', ', show_date.text)
            show_time = main_act.findParent().findParent().findNextSibling()
            show['time'] = re.sub('show', '', show_time.text).strip()
            shows.append(show)

    return shows
