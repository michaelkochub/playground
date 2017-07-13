# -*- coding: iso-8859-15 -*-

from bs4 import BeautifulSoup as BSoup
import requests

url = 'https://weather.com/weather/hourbyhour/l/USVA0027:1:US'

text = requests.get(url).text
soup = BSoup(text, 'html.parser')

hours = [data.text for data in soup.select('span.dsx-date')]
days = [data.text for data in soup.select('div.hourly-date')]
temps = [list(data.children)[0] for data in soup.select('td.temp > span')]

data = zip(days, hours, temps)

formatted = ["{day}, {hour}: {temp}˚F".format(day=day, hour=hour, temp=temp) for (day, hour, temp) in data]

for line in formatted:
    print(line)
