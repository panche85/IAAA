#!/usr/bin/python
import csv
import fileinput
import sys


def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

def av_list_update_item(item, value):

    file_name = 'av_list.csv'

    with open(file_name, 'r+') as io_file:
        reader = csv.reader(io_file, delimiter=';', quoting=csv.QUOTE_NONE)

        for line in reader:
            if item in line[0]:
                No_samples = int(line[1])
                avr = float(line[2])
                new_avr = ((No_samples*avr) + float(value))/(No_samples + 1)
                # item is existing
                print str(line) + ' <- (new_avr = %f)' % new_avr
                replaceAll(file_name,
                           '%s;%d;%f;' % (item,int(line[1]), float(line[2])),
                           '%s;%d;%f;' % (item, int(line[1])+1, new_avr))
            else:
                print line
                io_file.write('\n%s;%d;%f;' % (item, 1, float(value)))

    io_file.close()
    return;

def av_list_reset_item(item):

    file_name = 'av_list.csv'

    with open(file_name, 'r+') as io_file:
        reader = csv.reader(io_file, delimiter=';', quoting=csv.QUOTE_NONE)

        for line in reader:
            if item in line[0]:
                # item is existing
                print 'item: %s detected!' %item
                replaceAll('./data/' + file_name,
                           '%s;%d;%f;' % (item,int(line[1]), float(line[2])),
                           '%s;%d;%f;' % (item, int(0), float(0)))
            else:
                print 'item: %s' % item

    io_file.close()
    return;

def av_list_get_avr(item):
    file_name = 'av_list.csv'
    with open(file_name, 'r') as o_file:
        reader = csv.reader(o_file, delimiter=';', quoting=csv.QUOTE_NONE)
        for line in reader:
            if str(item) in line[0]:
                # item is existing
                print 'item: %s detected!' %item
                return float(line[2])
    o_file.close()
    return 0.;

def extract_by_item(file_name, item, index):

    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        results = filter(lambda row: row[index] == item, reader)
    f.close()

    return results;

def get_average_data(file_name):

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

    return data;

# Todo: the function need to be implemented!
def av_list_update_remove(item):
    with open(file_name, 'r') as in_file, open(file_name, 'w') as out_file:
        seen = set()  # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen: continue  # skip duplicate

            seen.add(line)
            out_file.write(line)
    return;

#av_list_update_item('nikica', 10)
#av_list_reset_item('test')