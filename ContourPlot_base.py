import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import interpolate

# one could use np.loadtxt and it returns an array however the computational time
# is much slower than pd.read_csv.

Set11 = pd.read_csv('Set11.csv')
R = Set11.values[:,3]
T = Set11.values[:,1]
H = Set11.values[:,2]

x = np.linspace(-35,-5,2000)
y = np.linspace(60,2000,2000)
xx, yy = np.meshgrid(x, y)

grid_z0 = interpolate.griddata((T,H), R, (xx, yy), method='linear')


v = np.linspace(-.5, 2.0, 20, endpoint=True)

plt.contourf(xx,yy,grid_z0,v, cmap=plt.cm.jet)
cbar = plt.colorbar(ticks=v)

plt.xlabel('Temperature ' u'\N{DEGREE SIGN}''C',fontsize=16)
plt.ylabel('Heighit ft',fontsize=16)
plt.title('Relative deviation between the measured and modeled Nox engine out concentration',fontsize=16)
x_tic = np.linspace(-35, -5, 7)
plt.xticks(x_tic)

y_tic = np.linspace(-250, 3750, 5)
plt.yticks(y_tic)

plt.savefig('SET11.png',bbox_inches='tight')
