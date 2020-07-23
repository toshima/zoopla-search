import click
import jsonplus as json  # supports datetimes
import time
from zoopla import Zoopla

API_KEY = "tfj69htyzg344yu2dzv634zc"
API_KEY = "z7cyp8jsb3enyxxfvvs8s8fn"

@click.command()
@click.option('-o', '--output', required=True)
def fetch(output, api_key):
    zoopla = Zoopla(api_key=API_KEY)
    page = 1
    listings = []
    while True:
        res = zoopla.property_listings({
            'page_number': page,
            'page_size': 100,
            'listing_status': 'sale',
            'area': 'Canary Wharf E14',
            'minimum_beds': 2,
        })
        page += 1
        if not res['listing']:
            break
        listings += res['listing']
        print(f"Listings found: {len(listings)}")
        time.sleep(1)

    out = json.dumps(listings)
    with open(output, 'w') as f:
        f.write(out)
    print(f"Wrote {output}")

if __name__ == '__main__':
    fetch()
