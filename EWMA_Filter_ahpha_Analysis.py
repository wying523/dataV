import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ratio= pd.read_csv('Processed_Ratio.csv',index_col=0)



Length = len(ratio)

RatioMean = ratio.mean()
ratio_std = np.std(ratio.values[:,0])

#EWMA coefficient
Alpha = np.arange(0,1,0.01)
Alpha =pd.DataFrame(Alpha)

#initialize the filtered data frame
std_arr = pd.DataFrame(index = range(len(Alpha)),columns = [0])

for j in xrange(len(Alpha)):
    S = pd.DataFrame(index = range(len(ratio)),columns = [0])
    
    temp = ratio.values[0][0]
    S.values[0][0] = temp
    
    Alp = Alpha.values[j][0]
    
    for i in xrange(1,Length):
        
        S.values[i][0] =(1-Alp) *S.values[i-1][0] + Alp * ratio.values[i][0]
         

    std_arr.values[j][0] = np.std(S[0])

 
SAVE = pd.concat([Alpha, std_arr], axis=1)
SAVE.to_csv("STD.csv")

perc_reduction = 1-std_arr.values[:,0]/ratio_std
plt.plot(Alpha,perc_reduction)
