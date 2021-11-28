import requests 
import numpy as np
import pandas as pd, matplotlib.pyplot as plt
import seaborn as sns

response = requests.get("https://github.com/kalilurrahman/TCSData/blob/main/TCS_stock_history.csv")
table_data = pd.read_html(response.text, header=0)
df_full = table_data[0] #first in a list of DataFrame objects

df = df_full.iloc[1:100]

df.plot(x = "Date", y = "Close")
plt.title("Close Price")
plt.ylabel("Price")

df.plot(x = "Date", y = "Volume", kind="bar")
plt.title("Volume")
plt.ylabel("Volume")

sns.lmplot(x='Close',y='Volume', data=df, fit_reg=True)
plt.title("Volume - Scatter Plot w/ Linear Regrassion")
plt.ylabel("Volume")

plt.show()