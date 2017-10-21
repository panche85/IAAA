#!/usr/bin/python

# note: The script is backUp-ing yesterdays' data!

import time
import os
from datetime import date, timedelta
from data_plot import plot_data
from data_plot import get_data_graph
from gen_area_graph import gen_graph_daily_avr

from notifications import send_email_notification
from data_handler import remove_duplicates

from shutil import copyfile

today = date.today()
yesterday = date.today() - timedelta(1)

# Print the start time of the script
print 'Daily notification for' + yesterday.strftime("%Y%m%d")

timestr = yesterday.strftime("%Y%m%d")
filename = 'data.csv' #data_'+timestr+'.csv'
filename_grafik = 'data_'+timestr+'.png'

# post-collecting data processing
remove_duplicates(filename)
print 'the code is starting'
data = get_data_graph(filename)
plot_data(data, './data/'+filename_grafik)
gen_graph_daily_avr()
send_email_notification(filename)

copyfile('av_list.csv', './data/avr_data/gav_'+today.strftime("%Y%m%d")+'.csv')
# remove the temp file.
#os.remove(filename)
