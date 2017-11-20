from bs4 import BeautifulSoup
from datetime import datetime


def parse(page, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    for entry in soup.findAll('div', class_='mix detail-information'):
        show = {}
        show['headliner'] = entry.find('h2', class_='show-title').text

        openers = entry.find('h3', class_='support')
        if openers is not None:
            show['openers'] = openers.text

        date_show = entry.find('div', class_='date-show')
        show['showtime'] = datetime.strptime(date_show.attrs['content'], '%B %d, %Y %I:%M %p')

        shows.append(show)

    return shows
