# !/usr/bin/python
from notifications import send_email_notification
import csv
import numpy as np
import matplotlib
import random
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from av_list_handler import av_list_update_item
from av_list_handler import av_list_get_avr

def extract_by_item(file_name, item, index):

    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        results = filter(lambda row: row[index] == item, reader)
    f.close()

    return results;

def get_data_graph(file_name):

    unique = set()  # set for fast O(1) amortized lookup
    # remove duplicates
    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        # creating a list
        for line in reader:
            if line[3] in unique: continue  # skip duplicate
            unique.add(line[3])
    f.close()

    data = set()
    for area in unique:
        sum = 0
        counter = 0
        sort = extract_by_item(file_name, area, 3)
        for item in sort:
            sum += float(item[2].replace(" ", "").rstrip(item[2][-2:]).upper())
            counter += 1
        data.add((area, sum/counter, av_list_get_avr(area)))
        print area
        print str(sum/counter) + '  ' + str(av_list_get_avr(area))
        av_list_update_item(area, sum/counter)

    return data;

def plot_data(data, file_name):
    
    names = []
    prices = []
    avr = []
    std1 = []
    std2 = []

    N = len(data)
    std = range(0, N)
    
    for item in data:
        names.append(item[0])
        prices.append(item[1])
        avr.append(item[2])
        std1.append(int(item[1]) % 10)
        std2.append((int(item[2]) % 10))

    ind = np.arange(0, N, 1)  # the x locations for the groups
    width = 0.333333  # the width of the bars

    fig, ax = plt.subplots()

    fig.set_figheight(3)
    fig.set_figwidth(int(N))

    color1 = '#5CB3FF'
    color2 = '#CC6600'
    rects1 = ax.bar(ind+(width/2), prices, width, color=color1, yerr=std1) # set shift of the graph
    rects2 = ax.bar(ind+(1.5*width), avr, width, color=color2, yerr=std2)  # set shift of the graph

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Price [euro/m2]')
    ax.set_title('Thessaloniki - City Areas')

    ax.set_xticks(ind+(width*1.5)) # set shift of the names
    ax.set_xticklabels(names)
    plt.xticks(rotation=270)

    ax.legend((rects1[0],rects2[0]), ('Daily-Average Price', 'Average Price'), loc='center left', bbox_to_anchor=(1, 0.5))

    def autolabel1(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,
                    height,
                    '%d' % int(height),
                    ha='center',
                    va='bottom',
                    color='b')

    def autolabel2(rects, rects_txt):
        """
        Attach a text label above each bar displaying its height
        """
        height_txt = []
        i = 0

        for rect in rects_txt:
            height_txt.append(rect.get_height())

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,
                    #height,
                    height_txt[i] + 85,
                    '%d' % int(height),
                    ha='center',
                    va='bottom',
                    #rotation='vertical',
                    color='r')
            i += 1

    autolabel1(rects1)
    autolabel2(rects2, rects1)
    plt.savefig(file_name, bbox_inches='tight')