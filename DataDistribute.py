import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

# one could use np.loadtxt and it returns an array however the computational time
# is much slower than pd.read_csv.

Temperature = pd.read_csv('Temperature.txt')

ratio= pd.read_csv('rnoxdiffavrgmaxus.txt')

Height = pd.read_csv('height.txt')


Length = len(Height)

H_min = min(Height.values)
H_max = max(Height.values)

T_min = min(Temperature.values)
T_max = max(Temperature.values)



#x = np.linspace(T_min,T_max,1000)
#y = np.linspace(H_min,H_max,1000)
#xx, yy = np.meshgrid(x, y)

#grid_z0 = interpolate.griddata((Temperature.values.flatten(),Height.values.flatten()), ratio, (xx, yy), method='linear')

#h = plt.contourf(Temperature.values,Height.values,grid_z0)
#plt.scatter(Temperature.values,Height.values,c = ratio)
#plt.savefig('Contour.png',bbox_inches='tight')
T = Temperature.values.flatten()
H = Height.values.flatten()
R = ratio.values.flatten()
min(H)
i = 1
j = 1
set11 = []
set12 = []
set13 = []
set21 = []
set22 = []
set23 = []
set31 = []
set32 = []
set33 = []
for i in xrange(1,Length):
    if H[i]<3750 and T[i]<-5:
        set11.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if H[i]<3750 and -5<=T[i]<25:
        set12.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if H[i]<3750 and 25<=T[i]<55:
        set13.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])

    if 3750<=H[i]<7750 and T[i]<-5:
        set21.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if 3750<=H[i]<7750 and -5<=T[i]<25:
        set22.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if 3750<=H[i]<7750 and 25<=T[i]<55:
        set23.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])

    if 7750<=H[i]<12000 and T[i]<-5:
        set31.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if 7750<=H[i]<12000  and -5<=T[i]<25:
        set32.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    if 7750<=H[i]<12000  and 25<=T[i]<55:
        set33.append([format(T[i],'.2f'),format(H[i],'.2f'),format(R[i],'.2f')])
    
df11 = pd.DataFrame(set11)
df11.to_csv("set11.csv")

df12 = pd.DataFrame(set12)
df12.to_csv("set12.csv")

df13 = pd.DataFrame(set13)
df13.to_csv("set13.csv")

df21 = pd.DataFrame(set21)
df21.to_csv("set21.csv")

df22 = pd.DataFrame(set22)
df22.to_csv("set22.csv")

df23 = pd.DataFrame(set23)
df23.to_csv("set23.csv")

df31 = pd.DataFrame(set31)
df31.to_csv("set31.csv")

df32 = pd.DataFrame(set32)
df32.to_csv("set32.csv")

df33 = pd.DataFrame(set33)
df33.to_csv("set33.csv")







