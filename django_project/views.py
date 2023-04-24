from django.shortcuts import render
from django.http import HttpResponse, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np


def Home(request):
    return render(request,'Home.html')


def Predict(request):
    data=pd.read_excel('F:\djanko\MarathonData.xlsx')
    category=LabelEncoder()
    data['Category']=category.fit_transform(data['Category'])
    data=data.drop(['id','Marathon','Name'],axis=1)
    x=data[['Category','km4week','sp4week','Wall21']]
    y=data['MarathonTime']
    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=199,test_size=0.15)
    model=RandomForestRegressor(n_estimators=16,random_state=55)
    model.fit(x_train,y_train)

    var1=(request.GET['n1'])
    var2=float(request.GET['n2'])
    var3=float(request.GET['n3'])
    var4=float(request.GET['n4'])
    
    catagory_=var1
    catagory_=int(category.transform([catagory_]))
    
    pred=model.predict([[catagory_,var2,var3,var4]])

    Time='Predicted marathon finishing time......'+str(pred)
    
    return render(request,'predict.html',{"result":Time})
