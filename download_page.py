#!/usr/bin/env python
from collector import Collector

config_file = raw_input('Config file: ')
parser_directory = raw_input('Parser directory: ')

collector = Collector(config_file, parser_directory)

parser = raw_input('Parser name: ')

page = collector.get_loaded_page(collector.sites[parser]['url'])

f = open('debug_sites/%s.html' % parser, 'w')
f.write(page)
f.close()
