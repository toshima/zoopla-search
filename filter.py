import click
import jsonplus as json  # supports datetimes


@click.command()
@click.option('--data', required=True)
@click.option('--query', required=True)
def filter(data, query):
    with open(data, 'r') as f:
        s = f.read()
    query = query.lower()

    for d in json.loads(s):
        if all(query not in str(s).lower() for s in d.values()):
            continue
        area = extract_area(d['description'])
        print(f"£ {d['price']}\t{area} sqft\t{d['details_url']}")


def extract_area(desc):
    desc = desc.lower()
    keys = [
        'internal sq',
        'sqft',
        'sq ft',
        'sq.ft',
        'sq. ft',
        'square feet',
    ]
    remove = [
        ',',
        '(',
        'c.',
        'unit',
    ]
    for k in keys:
        if k in desc:
            for words in desc.split(k)[:-1]:
                area = words.split()[-1]
                for s in remove:
                    area = area.replace(s, '')
                if area.replace('.', '').isdigit():
                    area = float(area)
                    if 400 < area < 10000:
                        return area
    return 0.0


if __name__ == '__main__':
    filter()
