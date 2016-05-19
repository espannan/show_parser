#!/usr/bin/env python
from collector import Collector
import sys

debug = len(sys.argv) > 1 and sys.argv[1] == '-d'

collector = Collector('config/agencies.yml', 'agency_parsers', debug)

agency_listings = collector.scrape_sites()

for agency, listings in agency_listings.items():
    print agency
    for listing in listings:
        print '\t', listing['title']
        print '\t\tPrice: ', listing['price']
        print '\t\tBed/Bath: ', listing['bed/bath']
        print '\t\tSize: ', listing['size'], ' sq ft'
        print '\t\tURL: ', listing['url']
