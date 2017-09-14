import time

from data_spitogatos import get_data_spitogatos

# Print the start time of the script
print time.strftime("%Y%m%d-%H%M%S")

timestr = time.strftime("%Y%m%d")
filename = './data_'+timestr+'.csv'

get_data_spitogatos(filename);

print('End')
