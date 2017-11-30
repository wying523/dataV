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
