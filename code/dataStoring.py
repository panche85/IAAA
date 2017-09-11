#!/usr/bin/python
import csv
#import tailer as tl


# Function definition is here
def printinfo(name, age):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return;


def append_data(file_name, data):
    with open(file_name, 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(data)
    return;


def read_data(file_name):
    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            print row
    return;

    # def read_data_tail(file_name):
    #    file = open(file_name)
    #    lastLines = tl.tail(file, 3)  # to read last 15 lines, change it  to any value.
    #    file.close()
    #    return lastLines;
