import requests
from bs4 import BeautifulSoup
import re

import time

from dataStoring import append_data
from dataStoring import read_data
from dataStoring import read_data_tail

timestr = time.strftime("%Y%m%d")
print time.strftime("%Y%m%d-%H%M%S")

filename = './data_'+timestr+'.csv'

def get_data_spitogatos(filename):
    page = requests.get("https://en.spitogatos.gr/search/results/residential/sale/r108/m108m")

    # Vraka status na pristap na stranata:
    # status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.
    if page.status_code != 200:
        print 'Error accessing the web-site! [error code: ' + page.status_code + ' ]'
        return;
        # print(soup.prettify())

    soup = BeautifulSoup(page.content, 'html.parser')

    html = list(soup.children)[2]
    body = list(html.children)[3]
    # print list(body.children)

    # Zemanje na delot od HTML-to
    search_list = soup.find(id='searchDetailsMainContent')
    prices = search_list.find_all(class_='text xbig bold padding-right')
    locations = search_list.find_all(class_='text color dark_grey margin-bottom-small')
    areas = search_list.find_all(class_='padding-right text medium')
    squareMs = search_list.find_all(class_='padding-right text medium')
    dates = search_list.find_all(class_='text color grey_dark')
    links = search_list.find_all(class_='text color cyan larger semibold searchListing_title')
    #print(links)
    #for link in links:
    #    print link.find('a').get('href')

    #i = 0
    #for i in range(10):
    #    print prices[i].get_text() + '\t\t' + re.sub('[^0-9a-zA-Z]+', '', areas[i*2].get_text()) + '\t' + locations[
    #        i].get_text()

    i = 0
    for i in range(10):
        # Reformatting the data
        item_price = re.sub('[^0-9]+', '', prices[i].get_text())
        item_area = re.sub('[^0-9a-zA-Z]+', '', areas[i*2].get_text())
        item_square = re.sub('[^0-9a-zA-Z]+', '', squareMs[(i*2)+1].get_text())
        item_location = ' '.join(locations[i].get_text().split())
        item_data = re.sub('[^0-9/]+', '', dates[i].get_text())
        item_link = links[i].find('a').get('href')
        
        # Appending the data to the tail of the file
        append_data(filename, [item_price, item_area, item_square, item_location, item_data, item_link])

        if int(item_price) <= 20000:
            print 'todo: implement email notification!'

    return;

get_data_spitogatos(filename);

print('End')

'''
    if [item_price, item_area, item_location, item_data] == read_data_tail(filename):
        print 'Nothing to get.'
    else:
        print 'New data is detected!'
        # Appending the data to the tail of the file
        append_data(filename, [item_price, item_area, item_location, item_data])
        #read_data(filename)
        #read_data_tail(filename)
        # Send notification
        if int(item_price) <= 20000:
            print 'todo: implement email notification!'
'''
