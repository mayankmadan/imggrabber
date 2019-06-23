#!/usr/bin/env python
import urllib.request # To send the http request
from urllib.parse import quote # To encode spaces in url to a valid ASCII format
from bs4 import BeautifulSoup # To parse the response

def get_image(q):
    req = urllib.request.Request('https://google.com/search?q={query}&tbm=isch'.format(query=q), headers={'User-Agent': 'Mozilla/5.0'}) # tbm=isch makes sure that its an image search
    # The header dictionary contains the http request headers. Since automated searches are not allowed
    # User-agent is manually set to Mozilla/5.0
    res = urllib.request.urlopen(req)
    s = BeautifulSoup(res.read(), 'html.parser')
    img = s.find(id='ires').find_all('img')[0]['src'] # Parsing through the response to get the src attribute of the first image returned
    imgres = urllib.request.urlopen(img) # Sending an http request to get the image
    with open('img', 'wb') as f:
        f.write(imgres.read()) # Writing the contents of the response received to a file as binary content

if __name__=='__main__': # If script is executed directly, it will take input from user and call the function with that argument
    q = quote(input('Image to be searched: '))
    get_image(q)
