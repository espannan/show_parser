#!/usr/bin/env python
from collector import Collector
import sys

debug = len(sys.argv) > 1 and sys.argv[1] == '-d'

collector = Collector('config/venues.yml', 'venue_parsers', debug)

shows = collector.scrape_sites()

for venue, venue_shows in shows.items():
    print venue
    for show in venue_shows:
        print '\t', show['headliner']
        if 'openers' in show:
            print '\t\t', show['openers']
        print '\t\t', show['showtime']
