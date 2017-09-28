# !/usr/bin/python
from notifications import get_data_graph
from notifications import send_email_notification
import numpy as np
import matplotlib.pyplot as plt

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


print 'the code is starting'
data = get_data_graph('data.csv')
plot_data(data, 'grafik.png')
send_email_notification('data.csv')