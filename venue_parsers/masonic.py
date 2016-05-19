from bs4 import BeautifulSoup


def parse(page, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')

    shows = []

    events_listing = soup.find('div', class_='container content').findAll('div', class_='col-md-8 left no-padding')

    for event in events_listing:
        show = {'headliner': event.find('div', class_='title').text}

        show['date'] = event.find('div', class_='bottom').text

        show['time'] = event.find('div', class_='door').text

        shows.append(show)

    return shows
