import requests
from bs4 import BeautifulSoup
import re

from dataStoring import append_data
from dataStoring import read_data
#from dataStoring import read_data_tail

def get_data_spitogatos():
    page = requests.get("https://en.spitogatos.gr/search/results/residential/sale/r108/m108m")

    # Vraka status na pristap na stranata:
    # status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.
    print page.status_code

    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    html = list(soup.children)[2]
    body = list(html.children)[3]
    # print list(body.children)

    # Zemanje na delot od HTML-to kaj sto
    search_list = soup.find(id='searchDetailsMainContent')
    prices = search_list.find_all(class_='text xbig bold padding-right')
    locations = search_list.find_all(class_='text color dark_grey margin-bottom-small')
    areas = search_list.find_all(class_='padding-right text medium')

    # Get Timestamp

    #i = 0
    #for i in range(10):
    #    print prices[i].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', areas[i*2].get_text()) + '\t' + locations[
    #        i].get_text()

    # Reformatting the data
    item_price = re.sub('[^0-9]+', '', prices[0].get_text())
    item_area = re.sub('[^0-9a-zA-Z]+', '', areas[0*2].get_text())
    item_location = ' '.join(locations[0].get_text().split())
    # Appending the data to the tail of the file
    append_data('data.csv', [item_price, item_area, item_location])

    read_data('data.csv')

    return;

get_data_spitogatos();

#print read_data_tail('data.csv')

print('End')


#print p.get_text()

