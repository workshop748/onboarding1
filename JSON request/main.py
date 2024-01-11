import requests #this libary is useful to see if the server is up
from bs4 import BeautifulSoup #this is useful to scrap a website and collect data from html tag name
#this is opening up the file and stroing the content as html file
with open("website.html", 'r') as html_file:
    #reading file and stroing the text in content
   content = html_file.read()
   #print(content) 
   
   
   #creating an instance  
   soup =BeautifulSoup(content,'lxml')
   country_population = soup('span', class_="country-population")
    
 