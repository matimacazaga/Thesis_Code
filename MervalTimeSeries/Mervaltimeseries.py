import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib as mpl 
import urllib.request as url

plt.style.use('seaborn-paper')
params = {
   'axes.labelsize': 10,
   'font.size': 10,
   'legend.fontsize': 10,
   'xtick.labelsize': 10,
   'ytick.labelsize': 10,
   'text.usetex': False,
   'figure.figsize': [6, 4.5]
   }
mpl.rcParams.update(params)

file_path = '/home/matimacazaga/Documents/Universidad/Tesis/Informe/PythonCode/MervalTimeSeries/MervalPrices.csv'
url.urlretrieve('http://www.ravaonline.com/v2/empresas/precioshistoricos.php?e=MERVAL&csv=1', file_path)
merval = pd.read_csv(file_path, sep = ',')
closes = merval['cierre']
dates = pd.to_datetime(merval['fecha'], yearfirst = True)
fig, ax = plt.subplots()
ax.plot(dates, closes, linewidth=2, color='#1c6bf3', label = r'Cierre Diario Indice Merval')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio')
ax.legend()
plt.savefig('/home/matimacazaga/Documents/Universidad/Tesis/Informe/PythonCode/MervalTimeSeries/Closes.png',dpi = 'figure', format = 'png', bbox_inches = 'tight' )
plt.show()

