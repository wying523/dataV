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
ratio_std = np.std(ratio.values)

#EWMA coefficient
Alpha = 0.1

#initialize the filtered data frame
S = pd.DataFrame(index = range(0,Length-1),columns = [1])


temp = ratio.values[0][0]
S.at[0,1] = temp

for i in xrange(1,Length):
    S.at[i,1] = (1-Alpha) * S.values[i-1,0] + Alpha * ratio.values[i,0]

New_std = np.std(S.values)
