#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re

from data_handler import append_data
#from data_handler import read_data
#from data_handler import read_data_tail

def get_data_spitogatos(filename):
    page = requests.get("https://en.spitogatos.gr/search/results/residential/sale/r108/m108m")

    # Vraka status na pristap na stranata:
    # status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.
    if page.status_code != 200:
        print 'Error accessing the web-site! [error code: ' + page.status_code + ' ]'
        return;
        # print(soup.prettify())

    data = page.text
    soup = BeautifulSoup(data, 'html.parser')

    html = list(soup.children)[2]
    body = list(html.children)[3]

    # Zemanje na delot od HTML-to
    search_list = soup.find(id='searchDetailsMainContent')
    prices = search_list.find_all(class_='text xbig bold padding-right')
    locations = search_list.find_all(class_='text color dark_grey margin-bottom-small')
    areas = search_list.find_all(class_='padding-right text medium')
    squareMs = search_list.find_all(class_='padding-right text medium')
    dates = search_list.find_all(class_='text color grey_dark')
    links = search_list.find_all(class_='text color cyan larger semibold searchListing_title')

    # Wtrte the data into the filey
    i = 0
    for i in range(10):
        # Reformatting the data
        item_price = re.sub('[^0-9]+', '', prices[i].get_text())
        item_area = re.sub('[^0-9a-zA-Z]+', '', areas[i * 2].get_text())
        item_square = re.sub('[^0-9a-zA-Z]+', '', squareMs[(i * 2) + 1].get_text())
        item_location = ' '.join(locations[i].get_text().split())
        item_data = re.sub('[^0-9/]+', '', dates[i].get_text())
        item_link = links[i].find('a').get('href')

        # Appending the data to the tail of the file
        append_data(filename, [item_price, item_area, item_square, item_location, item_data, item_link])

    return;

