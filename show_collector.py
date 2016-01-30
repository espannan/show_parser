import yaml
import requests

venues = yaml.load(open('venues.yml'))

shows = {}

for venue, info in venues.items():
    parser = __import__('venue_parsers.' + info['parser'], fromlist=[info['parser']])
    page = requests.get(info['url']).content
    shows[venue] = parser.parse(page)

for venue, venue_shows in shows.items():
    print venue
    for show in venue_shows:
        print '\t', show['headliner']
        if 'openers' in show:
            print '\t\t', show['openers']
        print '\t\t(', show['time'], ') ', show['date']

