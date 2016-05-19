from bs4 import BeautifulSoup
import re


def parse(page, *args, **kwargs):

    soup = BeautifulSoup(page, 'html.parser')

    event_list = soup.find('div', class_='event_list')

    more_info_list = event_list.find_all('a', title='More Info')

    shows = []

    for info in more_info_list:
        text = re.sub(r'\s+', ' ', info.text).strip()

        # this line has a show
        if text:
            show = {'headliner': text}

            # check for openers
            text = re.sub(r'\s+', ' ', info.parent.findNextSibling('h4').text).strip()
            if text:
                show['openers'] = text

            # get the date
            text = re.sub(r'\s+', ' ', info.parent.parent.parent.findChild('span', class_='fa fa-calendar-o').next_sibling).strip()
            if text:
                show['date'] = text

            # get the time
            text = re.sub(r'\s+', ' ', info.parent.parent.parent.findChild('span', class_='fa fa-clock-o').next_sibling).strip()
            if text:
                show['time'] = re.sub('Show ', '', text)

            shows.append(show)

    return shows
