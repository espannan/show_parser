from bs4 import BeautifulSoup
from datetime import datetime


def parse(page, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    for entry in soup.find_all('div', class_='faq_main calendar'):
        parts = entry.findChild('p', class_='title').text.split('with')

        show = {'headliner': parts[0]}

        if len(parts) > 1:
            show['openers'] = parts[1].strip()

        time_info = entry.findChild('span', class_='content').findChild('p')

        date = time_info.next_element

        time = str(date.next_element.next_element).split(' // ')[1].replace('Show ', '').replace('.', '').strip()

        show['showtime'] = datetime.strptime('{} {}'.format(date, time), '%A, %B %d, %Y %I:%M %p')

        shows.append(show)

    return shows
