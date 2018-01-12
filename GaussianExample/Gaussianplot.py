import matplotlib.pyplot as plt 
import matplotlib as mpl 
import numpy as np 
from scipy.stats import norm

plt.style.use('seaborn-paper')
plt.rc('text', usetex = True)
params = {
   'axes.labelsize': 10,
   'font.size': 10,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'figure.figsize': [6, 4.5]
   }
mpl.rcParams.update(params)

x_axis = np.arange(-10,10,0.001)
mean = 0
variance = 1
fig, ax = plt.subplots()
ax.plot(x_axis, norm.pdf(x_axis,mean,variance), linewidth=2, color='#1c6bf3', label = r'Distribución Gaussiana $\displaystyle\mu = 0$, $\displaystyle\sigma = 1$')
ax.set_xlabel(r'$\displaystyle x$')
ax.set_ylabel(r'$\displaystyle p(x)$')
ax.legend()
plt.savefig('/home/matimacazaga/Documents/Universidad/Tesis/Informe/PythonCode/GaussianExample/GaussianProb.png',dpi = 'figure', format = 'png', bbox_inches = 'tight' )
plt.show()


