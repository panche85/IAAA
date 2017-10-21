#!/usr/bin/python
import glob
import csv
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from av_list_handler import get_average_data

lista = glob.glob('./data/data_20*.csv')
lista = sorted(lista)
avr = set()
avr_data = set()

#merged_file_name = 'merged_data.csv'

# Ova e novata lokacija kade ke se skladiraat podatocite sto ke se koristi
No_areas = 0
areas = set()

file_name = 'av_list.csv'
with open(file_name, 'r') as o_file:
    reader = csv.reader(o_file, delimiter=';', quoting=csv.QUOTE_NONE)
    for line in reader:
        if line[0] != 'area':
            #print line[0]
            avr_data.add((line[0],line[2]))
            areas.add(line[0])
            No_areas += 1
    o_file.close()

# inserting all the names found at the position 0
i = 0
data = [[] for x in xrange(No_areas)]
for area in areas:
    data[i].append(area)
    print data[i][0]
    i += 1

# get averages values
average = []
for file in lista:
    avr = get_average_data(str(file))
    print str(file)
    #print avr
    i = 1
    for item in data:
        flag_find = 0
        for area in avr:
            tmp = list(area)[0]
            if not item: # check if list is empty
                item.append('empty')
                continue
            else:
                if item[0] == tmp:
                   item.append(area[1])
                   #average.append(area[2])
                   flag_find = 1
        if flag_find == 0:
            item.append(0)

yn = [[] for x in xrange(No_areas)]
yn_leg = []
for item in data:
    if item[0] != 'empty':
        yn.append(item)

for y in yn:
    if not y:
        continue
    else:
        yn_leg.append(y.pop(0))

for y in yn:
    if not y:
        continue
    else:
        tmp = 0
        for i in range(0,len(y)):
            if y[i] == 0:
                y[i] = tmp
            else:
                tmp = y[i]

        for i in range((len(y)-1), -1, -1):
            if y[i] == 0:
                y[i] = tmp
            else:
                tmp = y[i]
        print(range((len(y)-1), -1, -1))

N = len(lista)
std = range(0, N)
ind = np.arange(0, N, 1)  # the x locations

#fig, ax = plt.subplots()
#print [list(average)[2]] * 10
# make up some data
x = range(1, N, 1)
#y = [i+random.gauss(0,1) for i,_ in enumerate(x)]

#fig = plt.figure(figsize=(10, 6))
#line, = ax.plot(x, y,label='Inline label')

i = 0
subp = []
figs = []
average = 0
for y in yn:
    if not y:
        continue
    else:
        if i < len(avr_data):
            for item in avr_data:
                if yn_leg[i] == item[0]:
                    average = float(item[1])
                    print average

            aver = [average] * int(len(x))
            y.pop(0)
            figs.append(plt.figure(figsize=(7, 2)))
            subp.append(figs[i].add_subplot(1, 1, 1))  # instead of plt.subplot(2, 2, 1)
            subp[i].set_title(yn_leg[i])  # non OOP: plt.title('The function f')
            subp[i].plot(x, y, label=yn_leg[i])
            subp[i].plot(x, aver, label="test")
            plt.gcf().autofmt_xdate()
            plt.savefig('./data/graph/graph_' + yn_leg[i] + '.png', bbox_inches='tight')
            plt.close()
        i += 1

#plt.gcf().autofmt_xdate()
#plt.show()