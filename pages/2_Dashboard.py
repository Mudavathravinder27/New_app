import streamlit as st
from matplotlib import image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import os

df=pd.read_csv('resources/BITCOIN_TOTAL_CLEAN.csv')

st.subheader('Bitcoin of last 10 years history :red[Market Cap]')
fig1=plt.figure(figsize=(10,5))
# plt.figure(figsize=(10,5))
plt.plot(df.Date,df.Price_in_dollar,color = '#008000')
plt.title('Price History of Bitcoin(2013-2022)',color='g')
plt.xlabel('Date')
plt.ylabel('Price(in Dollar)')
st.pyplot(fig1)

fig1=plt.figure(figsize=(10,5))
plt.plot(df.Date,df['7day_chg_per'])
plt.title('Percent Change in 7 Days(Bitcoin)',color='b')
plt.xlabel('Date')
plt.ylabel('7 Days Change(in Percent)')
st.pyplot(fig1)
# st.subheader('Count of :blue[Bitcoin marketcap]')

# fig=plt.figure()
# df['Price'].value_counts().plot(kind="bar")
# st.pyplot(fig)

# st.subheader('Some of :red[Indian Companies] and their details')
# x=df[df['price']==' India']
# st.dataframe(x)