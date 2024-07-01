import pandas as pd
import numpy as np
import streamlit as st
c=st.container()
with c:
  data=pd.read_csv("zomato.csv",encoding="latin-1")
  feature_na=[i for i in  data.columns if data[i].isnull().sum()>0]
  for i in feature_na:
      print(f"{i} has {np.round((data[i].isnull().sum()/len(data[i])*100),4)}% null values")
  def a(data):
      if(data in ["NEW",'-']):
          return np.nan
      else:
          return data
  data["rate"]=data["rate"].apply(a)
  data.dropna(subset=["rate"],axis=0,inplace=True)
  data.replace(["NEW","-"],0,inplace=True)
  def split(x):
      return x.split('/')[0].strip()
  data["rate"]=data["rate"].apply(split)
  data.drop(columns=["url","address","phone"],inplace=True)
  data["rate"]=data["rate"].apply(float)
  rating=pd.pivot_table(data,index='name',values='rate')
  rating=rating.sort_values(['rate'],ascending=False)
  f1=plt.figure(figsize=(15,8))
  sns.barplot(x=rating[0:20].rate,y=rating[0:20].index,orient="h")
  st.pyplot(f1)
  f2=plt.figure(figsize=(15,8))
  sns.set_style('whitegrid')
  sns.distplot(data["rate"])
  st.pyplot(f2)
  f3=plt.figure(figsize=(10,7),dpi=110)
  chains=data["name"].value_counts()[0:15]
  sns.barplot(x=chains,y=chains.index,palette="deep")
  plt.xlabel("no. of outlets")
  st.pyplot(f3)
