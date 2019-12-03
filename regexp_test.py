import urllib.request
import re

site_url = 'https://bankir.ru/kurs/'
page = str(urllib.request.urlopen(site_url).read())

result = re.findall(r"<s\w*>\d*\.\d*", page)

print(f"Курс доллара:\nCегодня - {result[0][8:]}")
print(f"Завтра - {result[1][8:]}\nИсточник - {site_url}")



