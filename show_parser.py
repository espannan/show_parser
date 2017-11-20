#!/usr/bin/env python
from collector import Collector
import json
import requests
import sys

debug = len(sys.argv) > 1 and sys.argv[1] == '-d'

collector = Collector('config/venues.yml', 'venue_parsers', debug)

shows = collector.scrape_sites()

# print in console
for venue, venue_shows in shows.items():
    print venue
    for show in venue_shows:
        print '\t', show['headliner']
        if 'openers' in show:
            print '\t\t', show['openers']
        print '\t\t', show['showtime']


def get_venue(url, venue_list):
    for venue in venue_list:
        if venue['url'] == url:
            return venue

    return None


# update via the API
r = requests.get('http://127.0.0.1:8000/show-venues/')
venue_list = json.loads(r.content)
for venue_tag, venue_shows in shows.items():
    url = collector.sites[venue_tag]['url']
    venue = get_venue(url, venue_list)

    for show in venue_shows:
        show['show_venue'] = venue['id']
        r = requests.post('http://127.0.0.1:8000/shows/', data=show)
