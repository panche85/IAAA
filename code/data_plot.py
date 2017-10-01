# !/usr/bin/python
from notifications import send_email_notification
import csv
import numpy as np
import matplotlib
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

    ind = np.arange(0, N * 2, 2)  # the x locations for the groups
    width = 0.45  # the width of the bars

    fig, ax = plt.subplots()

    color1 = '#168EF7'
    color2 = '#F88017'
    rects1 = ax.bar(ind, prices, width, color=color1, yerr=std1) # set shift of the graph
    rects2 = ax.bar(ind + width, avr, width, color=color2, yerr=std2)  # set shift of the graph

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Cena (euro/m2)')
    ax.set_title('Dnevni prosecni ceni na stanovite')
    ax.set_xticks(ind+width/2) # set shift of the names

    ax.set_xticklabels(names)
    plt.xticks(rotation=270)

    ax.legend((rects1[0],rects2[0]), ('daily average', 'AVR'))

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
                    va='bottom')

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
