import requests #this libary is useful to see if the server is up
from bs4 import BeautifulSoup #this is useful to scrap a website and collect data from html tag name
#this is using requests to grab the html in the website and store it in html_text
html_txt =requests.get('https://www.scrapethissite.com/pages/simple/').text
print(html_txt)
 