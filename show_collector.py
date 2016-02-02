import yaml
import requests

venues = yaml.load(open('venues.yml'))

shows = {}

for venue, info in venues.items():
    parser = __import__('venue_parsers.' + info['parser'], fromlist=[info['parser']])
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'}
    page = requests.get(info['url'], headers=headers).content
    shows[venue] = parser.parse(page)

for venue, venue_shows in shows.items():
    print venue
    for show in venue_shows:
        print '\t', show['headliner']
        if 'openers' in show:
            print '\t\t', show['openers']
        print '\t\t(', show['time'], ') ', show['date']

