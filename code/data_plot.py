# !/usr/bin/python
from notifications import send_email_notification
import csv
import numpy as np
# note: Redosledot na povikuvanje na modulite e biten!!!
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
        data.add((area, sum/counter))
        print area
        print sum/counter

    return data;

def plot_data(data, file_name):
    
    names = []
    prices = []

    N = len(data)
    std = range(0, N)
    
    for item in data:
        names.append(item[0])
        prices.append(item[1])

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, prices, width, color='y', yerr=std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Cena (euro/m2)')
    ax.set_title('Dnevni prosecni ceni na stanovite')
    ax.set_xticks(ind)

    ax.set_xticklabels(names)
    plt.xticks(rotation=270)

    ax.legend((rects1[0],), ('Oblast',))

    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2.,
                    1. * height,
                    '%d' % int(height),
                    ha='center',
                    va='bottom')

    autolabel(rects1)
    # autolabel(rects2)
    plt.savefig(file_name, bbox_inches='tight')
