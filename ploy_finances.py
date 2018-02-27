years = ['2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18 \nYTD']
revenues = [3356, 10874.43, 11693.23, 18382.15, 19417.50, 19515.21, 23356.95]
expenditures = [4209, 10996.07, 11512.83, 13996.51, 19675.53, 22541.80, 381.65]

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import ScalarFormatter
plt.style.use("seaborn-whitegrid")

params = {
            # 'text.usetex' : True,
           'font.family': 'sans-serif',
            'font.sans-serif': 'Tw Cen MT',
# #           'text.latex.preamble': [r'\usepackage{siunitx}',]
}
matplotlib.rcParams.update(params)

fig = plt.figure() 
ax = fig.add_subplot(111)
ind = np.arange(len(revenues))
width = 0.35 
p1 = ax.bar(ind, revenues, width, color=(207/255,20/255,43/255), label="Revenue")
p2 = ax.bar(ind + width, expenditures, width, color=(207/255,20/255,43/255,0.4), label="Expenditure")
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(years)
ax.spines['top'].set_visible(False)    
ax.spines['right'].set_visible(False)
ax.xaxis.grid(False)
ax.set_xlabel("Financial Year")
ax.set_ylabel("Amount (£)")
ax.set_title("UKSEDS Revenue and Expenditure (2011 - 2018 YTD)")
plt.legend()
plt.savefig('graph.pdf', format='pdf', dpi=1000)
plt.show()
