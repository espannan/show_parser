#!/usr/bin/env python
from collector import Collector
import requests

config_file = raw_input('Config file: ')
parser_directory = raw_input('Parser directory: ')

collector = Collector(config_file, parser_directory)

parser = raw_input('Parser name: ')

if collector.sites[parser]['javascript']:
    page = collector.get_loaded_page(collector.sites[parser]['url'])
else:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'}
    page = requests.get(collector.sites[parser]['url'], headers=headers)

f = open('debug_sites/%s.html' % parser, 'w')
f.write(page)
f.close()
