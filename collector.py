import yaml
import requests
from selenium import webdriver
import time


class Collector(object):

    def __init__(self, config_file, parser_directory, debug=False):
        self.sites = yaml.load(open(config_file))
        self.parser_directory = parser_directory
        self.debug = debug
        self.site_divider = '*****'
        self.item_divider = '^^^^^'
        self.title_divider = ':::'

    def get_loaded_page(self, url):
        try:
            driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
        except AttributeError:
            pass
        driver.get(url)
        time.sleep(3)
        page_source = driver.page_source.encode('utf-8')
        driver.close()

        return page_source

    def load_log(self, log_title):
        f = open('logs/%s.txt' % log_title, 'r')
        full_file = f.read()
        sites_dict = {}
        site_chunks = full_file.strip().split(self.site_divider)[1:]
        for site in site_chunks:
            site_listings = []
            full_chunk = site.strip().split(self.item_divider)
            site = full_chunk[0].strip()
            listing_chunks = full_chunk[1:]
            for listing in listing_chunks:
                listing_dict = {}
                line_items = listing.strip().split('\n')
                for line_item in line_items:
                    parts = line_item.strip().split(self.title_divider)
                    listing_dict[parts[0]] = parts[1] if len(parts) > 1 else ''
                site_listings.append(listing_dict)
            sites_dict[site] = site_listings
        return sites_dict

    def write_log(self, site_contents, log_title):
        f = open('logs/%s.txt' % log_title, 'w')
        log_message = []
        for site, contents in site_contents.items():
            log_message.append(self.site_divider)
            log_message.append(site)
            for content in contents:
                log_message.append(self.item_divider)
                for category, info in content.items():
                    log_message.append('%s%s%s' % (category, self.title_divider, info.encode('utf-8')))
        f.write('\n'.join(log_message))
        f.close()

    def scrape_sites(self):
        site_contents = {}

        for site, info in self.sites.items():
            parser = __import__(self.parser_directory + '.' + info['parser'], fromlist=[info['parser']])
            base = info.get('base', '')
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'}
            if self.debug:
                f = open('debug_sites/' + site + '.html', 'r')
                page = f.read().encode('utf-8')
            elif info['javascript']:
                page = self.get_loaded_page(info['url'])
            else:
                page = requests.get(info['url'], headers=headers).content
            site_contents[site] = parser.parse(page, base)

        return site_contents
