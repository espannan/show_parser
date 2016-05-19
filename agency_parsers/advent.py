from bs4 import BeautifulSoup

def parse(page):
    soup = BeautifulSoup(page, 'html.parser')
    listings = []

    for entry in soup.findAll('div', class_='listing-item result js-listing-item'):
        listing = {}
        listing['url'] = 'https://adventproperties.appfolio.com' + entry.find('a', class_='js-link-to-detail').attrs['href']
        listing['title'] = entry.find('h2', class_='listing-item__title js-listing-title').text.strip()

        details = entry.findAll('dd', class_='detail-box__value')
        listing['price'] = details[0].text if len(details) >= 1 else ''
        listing['size'] = details[1].text if len(details) >= 2 else ''
        listing['bed/bath'] = details[2].text if len(details) >= 3 else ''
        listing['address'] = entry.find('span', class_='js-listing-address').text

        listings.append(listing)

    return listings

def debug():
    #url = 'https://adventproperties.appfolio.com/listings/?1463542934435'
    #headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30'}
    #import requests
    #page = requests.get(url, headers=headers).content
    f = open('advent.html', 'r')
    page = f.read()
    f.close()
    listings = parse(page)
    print listings
    return BeautifulSoup(page, 'html.parser')
