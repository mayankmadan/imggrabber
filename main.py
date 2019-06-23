#!/usr/bin/env python
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup

q = quote(input('Image to be Searched: '))

req = urllib.request.Request('https://google.com/search?q={query}&tbm=isch'.format(query=q), headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
s = BeautifulSoup(res.read(), 'html.parser')
img = s.find(id='ires').find_all('img')[0]['src']
imgres = urllib.request.urlopen(img)
with open('img', 'wb') as f:
  f.write(imgres.read())
