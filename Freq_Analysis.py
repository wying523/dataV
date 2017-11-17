import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# one could use np.loadtxt and it returns an array however the computational time
# is much slower than pd.read_csv.
Temperature = pd.read_csv('Temperature.txt')

ratio= pd.read_csv('rnoxdiffavrgmaxus.txt')

Height = pd.read_csv('height.txt')


Length = len(Height)

RatioMean = ratio.mean().values

fig, ax1 = plt.subplots(figsize=(20, 16))

ax2 = ax1.twinx()

hist, bins = np.histogram(ratio.values.flatten(), bins = 20)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
ax1.bar(center, hist, align='center', width=width)
ax1.axvline(RatioMean, color='b', linestyle='dashed', linewidth=2)

hist_Freq, bins = np.histogram(ratio.values.flatten(), bins = 200)
ratio_freq = hist_Freq/(Length*1.000)
ratio_min = min(ratio.values)
ratio_max = max(ratio.values)

x = np.linspace(ratio_min, ratio_max, 200)

ax2.plot(x,np.cumsum(ratio_freq), 'r.')

ax1.set_ylabel('Frequency [-]',fontsize=16)
ax2.set_ylabel('Cumulative frequency [-]',fontsize=16)
ax1.set_xlabel('Relative deviation between measured and modeled Engine Out NOx concentration [-]',
               fontsize=16)
x_tic = np.linspace(-0.5, 2, 26)
ax1.set_xticks(x_tic)
ax1.set_xticklabels(x_tic, rotation=0, fontsize=16)
y_tic = np.linspace(0, 1,11)
ax2.set_yticks(y_tic)
ax2.set_yticklabels(y_tic, rotation=0, fontsize=16)

y_tic1 = ax1.get_yticks()
ax1.set_yticklabels(y_tic1, rotation=0, fontsize=16)

ratio_std = np.std(ratio.values)


ax1.text(1.1,400000, ' Total number of samples = %d\n Mean Value = %.3f\n Standard Deviation = %.3f\n Max Value = %.3f\n Min Value = %.3f'%(Length, RatioMean, ratio_std,ratio_max,ratio_min),
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0),
         fontsize=20)


plt.savefig('frequency_Analysis.png',bbox_inches='tight')


##test git
#ahfhadfaiu

