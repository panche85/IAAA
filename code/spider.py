import requests
from bs4 import BeautifulSoup
import re

from dataStoring import printinfo

page = requests.get("https://en.spitogatos.gr/search/results/residential/sale/r108/m108m")

# Vraka status na pristap na stranata:
# status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.
print page.status_code

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

html = list(soup.children)[2]
body = list(html.children)[3]
#print list(body.children)

# Zemanje na delot od HTML-to kaj sto 
search_list = soup.find(id='searchDetailsMainContent')
prices = search_list.find_all(class_='text xbig bold padding-right')
locations = search_list.find_all(class_='text color dark_grey margin-bottom-small')
area = search_list.find_all(class_='padding-right text medium')

print prices[0].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[0].get_text())  + '\t' + locations[0].get_text()
print prices[1].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[2].get_text())  + '\t' + locations[1].get_text()
print prices[2].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[4].get_text())  + '\t' + locations[2].get_text()
print prices[3].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[6].get_text())  + '\t' + locations[3].get_text()
print prices[4].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[8].get_text())  + '\t' + locations[4].get_text()
print prices[5].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[10].get_text()) + '\t' + locations[5].get_text()
print prices[6].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[12].get_text()) + '\t' + locations[6].get_text()
print prices[7].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[14].get_text()) + '\t' + locations[7].get_text()
print prices[8].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[16].get_text()) + '\t' + locations[8].get_text()
print prices[9].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', area[18].get_text()) + '\t' + locations[9].get_text()

printinfo('test' , '111')

print('End')

#print p.get_text()

