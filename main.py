import requests 
import numpy as np
import pandas as pd, matplotlib.pyplot as plt, statsmodels.api as sm

response = requests.get("https://github.com/kalilurrahman/TCSData/blob/main/TCS_stock_history.csv")
#print(response.text)
table_data = pd.read_html(response.text)
df = table_data[0]
df.head()
print(df) 

df.plot(x = "Date", y = "Close")
plt.title("Close Price")
plt.ylabel("price")
plt.figure()
#plt.show()
#y_axis = np.array(df['Dividends'])
#x_axis = np.array(df['Date'])
#df.plot(x = "Date", y = "Dividends")
#d = np.polyfit(x_axis, y_axis, 1)
#f = np.poly1d(d)
#df.insert(6, 'Treg', f(df['Date']))
#ax = df.plot(x = 'Date', y = 'Dividends')
#df.plot(x = 'Date', y = 'Treg', color = 'Red', ax= ax)
#plt.show()
#df2 = df
df.plot(x = "Date", y = "Volume")
df.plot.bar()
plt.figure()
plt.show()