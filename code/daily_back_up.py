#!/usr/bin/python

# note: The script is backUp-ing yesterdays' data!

import time
from datetime import date, timedelta

from notifications import send_email_notification
from data_handler import remove_duplicates

yesterday = date.today() - timedelta(1)

# Print the start time of the script
print 'Daily notification for' + yesterday.strftime("%Y%m%d")

timestr = yesterday.strftime("%Y%m%d")
filename = 'data_'+timestr+'.csv'

# post-collecting data processing
remove_duplicates(filename)
send_email_notification('./data/' + filename)

# remove the temp file.
os.remove(filename, *, dir_fd=None)
