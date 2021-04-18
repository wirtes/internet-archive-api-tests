# These are Internet Archive Tests

from internetarchive import search_items

for i in search_items('identifier:nasa'):
    print(i['identifier'])

