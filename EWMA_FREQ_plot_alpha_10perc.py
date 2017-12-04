import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('seaborn-deep')

ratio= pd.read_csv('Processed_Ratio.csv',index_col=0)

S= pd.read_csv('EWMA_10PERC.csv',index_col=0)


Length = len(ratio)

RatioMean = ratio.mean()
ratio_std = np.std(ratio.values[:,0])


fig, ax1 = plt.subplots(figsize=(20, 16))



bins = np.linspace(-0.5,2,100)

hist, bins1 = np.histogram(ratio.values.flatten(), bins = 200)
#width = 0.7 * (bins[1] - bins[0])
#center = (bins[:-1] + bins[1:]) / 2
#ax1.bar(center, hist, align='center', width=width)

plt.hist(ratio.values.flatten(), bins,color=['blue'], alpha=0.7, label='Original',edgecolor='black', linewidth=1.2)

plt.hist(S.values.flatten(), bins, color=['coral'], alpha=0.7, label='EWMA Filter',edgecolor='black', linewidth=1.2)

#ax1.axvline(RatioMean, color='b', linestyle='dashed', linewidth=2)


#cumulative frequency
hist_Freq, bins = np.histogram(ratio.values.flatten(), bins = 200)
ratio_freq = hist_Freq/(Length*1.000)
ratio_min = min(ratio.values)
ratio_max = max(ratio.values)

x = np.linspace(ratio_min, ratio_max, 200)
ax2 = ax1.twinx()
ax2.plot(x,np.cumsum(ratio_freq), 'r.', label='Original - Cumulative Frequency')

hist_S_Freq, bins = np.histogram(S.values.flatten(), bins = 200)
S_freq = hist_Freq/(len(S)*1.000)
S_min = min(S.values)
S_max = max(S.values)
Y = np.linspace(S_min, S_max, 200)
ax2.plot(Y,np.cumsum(S_freq), 'go', label='EWMA Filter - Cumulative Frequency')






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



ax2.text(1.1,0.5, ' Original data Analysis: \n Total number of samples = %d\n Mean Value = %.3f\n Standard Deviation = %.3f\n Max Value = %.3f\n Min Value = %.3f'%(Length, RatioMean, ratio_std,ratio_max,ratio_min),
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0),
         fontsize=20)


ax2.text(1.1,0.1, ' EWMA-Filtered data Analysis: \n Total number of samples = %d\n Mean Value = %.3f\n Standard Deviation = %.3f\n Max Value = %.3f\n Min Value = %.3f'%(len(S.values), S.mean(), np.std(S.values[:,0]),S_max,S_min),
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0),
         fontsize=20)
ax2.text(1.1,0.85, 'Standard deviation reduction is %.3f' %(1 - np.std(S.values[:,0])/ratio_std),
         bbox=dict(facecolor='none', edgecolor='black', pad=10.0),
         fontsize=20) 

ax1.legend(loc='center left')
ax2.legend(loc='upper left')
#plt.show()
##
plt.savefig('EWMA_frequency_Analysis.png',bbox_inches='tight')
##
##
##
##
##
