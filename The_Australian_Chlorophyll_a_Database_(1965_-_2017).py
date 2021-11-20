#!/usr/bin/env python
import codecs
import csv

try:
    # Python 3
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib2 import urlopen

# The URL to the collection (as comma-separated values).
collection_url = "http://geoserver-portal.aodn.org.au/geoserver/ows?typeName=imos:aus_chla_db_data&SERVICE=WFS&outputFormat=csv&REQUEST=GetFeature&VERSION=1.0.0&CQL_FILTER=INTERSECTS(geom%2CPOLYGON((106.7431640625%20-37.310546875%2C106.7431640625%20-24.7421875%2C119.0478515625%20-24.7421875%2C119.0478515625%20-37.310546875%2C106.7431640625%20-37.310546875)))%20AND%20SAMPLE_TIME_UTC%20%3E%3D%20'1992-01-01T00%3A00%3A00.000Z'%20AND%20SAMPLE_TIME_UTC%20%3C%3D%20'2021-11-20T23%3A59%3A59.999Z'"

# Fetch data...
response = urlopen(collection_url)

# Iterate on data...
csvfile = csv.reader(codecs.iterdecode(response, 'utf-8'))
for row in csvfile:
    print(row)
