from bs4 import BeautifulSoup
import re

def parse(page):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    for entry in soup.find_all('div', class_='faq_main calendar'):
        parts = entry.findChild('p', class_='title').text.split('with')

        show = {'headliner' : parts[0]}

        if len(parts) > 1:
            show['openers'] = parts[1].strip()

        time_info = entry.findChild('span', class_='content').findChild('p')

        date = time_info.next_element

        show['date'] = str(date)

        show['time'] = str(date.next_element.next_element)

        shows.append(show)

    return shows

