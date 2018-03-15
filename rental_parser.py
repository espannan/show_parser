#!/usr/bin/env python
from collector import Collector
from jinja2 import Environment, FileSystemLoader
import sys

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('rentals.html')

debug = '-d' in sys.argv

region = 'bay_area'
if '--region' in sys.argv:
    region = sys.argv[sys.argv.index('--region') + 1]

collector = Collector('config/agencies.yml', 'agency_parsers', debug=debug, subset=region)

collector.load_log('rentals')

agency_listings = collector.scrape_sites()

for agency, listings in agency_listings.items():
    print agency.capitalize().replace('_', ' ')
    for listing in listings:
        print '\t', listing['title']
        print '\t\tPrice: ', listing['price']
        print '\t\tAddress: ', listing['address']
        print '\t\tBed/Bath: ', listing['bed/bath']
        print '\t\tSize: ', listing['size'], ' sq ft'
        print '\t\tURL: ', listing['url']

collector.write_log(agency_listings, 'rentals')

rendered_page = template.render(agency_listings=agency_listings)

f = open('{}_rentals.html'.format(region), 'w')
f.write(rendered_page.encode('utf-8'))
f.close()
