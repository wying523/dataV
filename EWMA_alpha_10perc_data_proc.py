import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ratio= pd.read_csv('Processed_Ratio.csv',index_col=0)



Length = len(ratio)

RatioMean = ratio.mean()
ratio_std = np.std(ratio.values[:,0])

#EWMA coefficient
Alpha = 0.1



S = pd.DataFrame(index = range(len(ratio)),columns = [0])
                            
temp = ratio.values[0][0]
S.values[0][0] = temp
                            

                            
for i in xrange(1,Length):
                                    
    S.values[i][0] =(1-Alpha) *S.values[i-1][0] + Alpha * ratio.values[i][0]

    std_arr = np.std(S[0])

