import requests #this libary is useful to see if the server is up
from bs4 import BeautifulSoup #this is useful to scrap a website and collect data from html tag name
#this is using requests to grab the html in the website and store it in html_text
html_txt =requests.get('https://www.scrapethissite.com/pages/simple/').text
soup =BeautifulSoup(html_txt,'lxml')
#gets the html and find the class name asosiated with it
countrys =soup.find_all('div',class_='col-md-4 country')
for country in countrys:
    country_name = country.find('h3',class_='country-name')
    country_population = country.find('span',class_='country-population')
    print(country_name.text.strip(),':',country_population.text,'\n')