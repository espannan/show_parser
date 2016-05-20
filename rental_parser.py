#!/usr/bin/env python
from collector import Collector
from jinja2 import Environment, FileSystemLoader
import sys

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('rentals.html')

debug = len(sys.argv) > 1 and sys.argv[1] == '-d'

collector = Collector('config/agencies.yml', 'agency_parsers', debug)

agency_listings = collector.scrape_sites()

for agency, listings in agency_listings.items():
    print agency
    for listing in listings:
        print '\t', listing['title']
        print '\t\tPrice: ', listing['price']
        print '\t\tAddress: ', listing['address']
        print '\t\tBed/Bath: ', listing['bed/bath']
        print '\t\tSize: ', listing['size'], ' sq ft'
        print '\t\tURL: ', listing['url']

rendered_page = template.render(agency_listings=agency_listings)

f = open('rentals.html', 'w')
f.write(rendered_page)
f.close()
