# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup as BSoup
from sys import argv
import requests

url = 'https://weather.com/weather/hourbyhour/l/US{region}:1:US'
region_codes = {
    'tysons corner': 'VA0974',
    'ashburn': 'VA0027',
    'dc': 'DC0001'
}

region = ''
default_region = region_codes['tysons corner']

if len(argv) > 1 and argv[1] in region_codes.keys():
    region = region_codes[argv[1]]
else:
    region = default_region

text = requests.get(url.format(region=region)).text
soup = BSoup(text, 'html.parser')

hours = [data.text for data in soup.select('span.dsx-date')]
days = [data.text for data in soup.select('div.hourly-date')]
temps = [list(data.children)[0] for data in soup.select('td.temp > span')]

data = zip(days, hours, temps)

formatted = ["{day}, {hour}: {temp}˚F".format(day=day, hour=hour, temp=temp) for (day, hour, temp) in data]

for line in formatted:
    print(line)
