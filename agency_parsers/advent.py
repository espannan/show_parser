from bs4 import BeautifulSoup


def parse(page, base, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')
    listings = []

    for entry in soup.findAll('div', class_='listing-item result js-listing-item'):
        listing = {}
        listing['url'] = base + entry.find('a', class_='js-link-to-detail').attrs['href']
        listing['title'] = entry.find('h2', class_='listing-item__title js-listing-title').text.strip()

        details = entry.findAll('dd', class_='detail-box__value')
        listing['price'] = details[0].text if len(details) >= 1 else ''
        listing['size'] = details[1].text if len(details) >= 2 else ''
        listing['bed/bath'] = details[2].text if len(details) >= 3 else ''
        listing['address'] = entry.find('span', class_='js-listing-address').text

        listings.append(listing)

    return listings
