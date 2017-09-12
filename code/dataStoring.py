#!/usr/bin/python
import csv

def append_data(file_name, data):
    with open(file_name, 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(data)

        csvfile.close()
    return;


def read_data(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            print row

    f.close()
    return;


def read_data_tail(file_name):
    row_count = 0
    last = []

    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        row_count = sum(1 for row in reader)
        f.close()
        #print row_count

    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        i = 0;
        for row in reader:
            if i == (row_count-1):
                #print "This is the line."
                last = list(row)
                f.close()
                break
            i += 1

    f.close()
    return last;
