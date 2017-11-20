from bs4 import BeautifulSoup
from datetime import datetime


def parse(page, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    events_listing = soup.find('div', class_='container content').findAll('div', class_='col-md-8 left no-padding')

    for event in events_listing:
        show = {'headliner': event.find('div', class_='title').text}

        date = event.find('div', class_='bottom').text

        time = event.find('div', class_='door').text.split(' // ')[1].replace('Event: ', '').strip()

        show['showtime'] = datetime.strptime('{} {}'.format(date, time), '%A, %B %d, %Y %I:%M %p')

        shows.append(show)

    return shows
