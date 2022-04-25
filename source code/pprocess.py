import sys
import pandas as pd
import numpy as np
from sys import argv


dataframe1 = pd.read_csv(argv[1])#churn.txt

# storing this dataframe in a csv file
#dataframe1.to_csv('log.csv',index=None)
dataframe1.to_csv('churn_csv.csv')
data=pd.read_csv("churn_csv.csv")


# Rời rạc hóa dữ liệu ở các thuộc tính liên tục
data["Day Mins"] = pd.cut(data["Day Mins"],
bins=[0., 150, 250, np.inf],
labels=["low", "medium", "high"])

data["Day Calls"] = pd.cut(data["Day Calls"],
bins=[0., 75, 125, np.inf],
labels=["low", "medium", "high"])

data["Eve Mins"] = pd.cut(data["Eve Mins"],
bins=[0., 150, 250, np.inf],
labels=["low", "medium", "high"])
    
data["Eve Calls"] = pd.cut(data["Eve Calls"],
bins=[0., 80, 120, np.inf],
labels=["low", "medium", "high"])

data["Night Mins"] = pd.cut(data["Night Mins"],
bins=[0., 150, 250, np.inf],
labels=["low", "medium", "high"])
data["Night Calls"] = pd.cut(data["Night Calls"],
bins=[0., 80, 120, np.inf],
labels=["low", "medium", "high"])

data["Int'l Calls"] = pd.cut(data["Intl Calls"],
bins=[0., 6, 13, np.inf],
labels=["low", "medium", "high"])

data["CustServ Calls"] = pd.cut(data["CustServ Calls"],
bins=[-1, 3, np.inf],
labels=["low", "high"])
#Lấy ngẫu nhiên 1000 mẫu
#data=data.sample(n=1000)
data=data[data['Day Mins']=='high']

# Lấy lại những thuộc tính cần thiết cho việc sinh luật
newData=data[["Int'l Plan", "VMail Plan","Day Mins",
"Day Calls","Eve Mins","Eve Calls","Night Mins",
"Night Calls","CustServ Calls","Churn?"]]

newData.to_csv("ChurnProcessed.csv")#file csv sau khi đã được xử lý