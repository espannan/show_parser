from bs4 import BeautifulSoup


def parse(page, base, *args, **kwargs):
    soup = BeautifulSoup(page, 'html.parser')
    listings = []

    for entry in soup.findAll('div', class_='listing-item result js-listing-item'):
        listing = {}
        try:
            listing['url'] = base + entry.find('a', class_='btn js-hand-hidden-link-to-detail').attrs['href']

            try:
                title = entry.find('h2', class_='listing-item__title js-listing-title').text.strip()
            except AttributeError:
                title = 'No Title'
            listing['title'] = title

            details = entry.findAll('dd', class_='detail-box__value')
            listing['price'] = details[0].text if len(details) >= 1 else ''
            listing['size'] = details[1].text if len(details) >= 2 else ''
            listing['bed/bath'] = details[2].text if len(details) >= 3 else ''
            listing['address'] = entry.find('span', class_='u-pad-rm js-listing-address').text

            listings.append(listing)
        except AttributeError:
            pass

    return listings
