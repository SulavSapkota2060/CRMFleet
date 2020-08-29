import requests 
from bs4 import BeautifulSoup as bs
import urllib.request
import random

main_url = 'https://wallpaperscraft.com/catalog/cars/3840x2400/page2'

r = requests.get(main_url)
soup = bs(r.content,'lxml')
wallpapers = soup.select('ul.wallpapers__list a')
initial_url = 'https://wallpaperscraft.com'



for link in wallpapers:
    rem_url = link['href']
    full_url = initial_url + rem_url
    r2 = requests.get(full_url)
    soup2 = bs(r2.content,'lxml')
    a= soup2.select("img.wallpaper__image")
    image_link = a[0]['src']
    random_name = 'image' + str(random.randint(100,1000)) + '.jpg'
    urllib.request.urlretrieve(image_link,filename=random_name)
    print("done")
