# user pandas function

import pandas as pd
# import json
# #user series
# with open("mdl_user.json",mode="r",encoding="utf-8") as file :
#     data = json.load(file)
# print(data)    

# data1 = pd.Series([10,20,30,40])
# condition = [True,False,True,True]
# filterdata = data1[condition]
# print(filterdata)
# data1 = pd.Series(["你好","python","pandas"])
# #condition =[True,True,False]
# condition = data1.str.contains("p")
# print(condition)
# filterdata= data1[condition]
# print(filterdata)
#------------------------------dataframe-------------------------
data1 =pd.DataFrame({
    "name":["Amy","peter","joyce","tom","kitty"],
    "salary":[20000,50000,30000,25000,16000],
    "sex":["female","male","female","male","female"]})
#print(data1)
print("-----------------------------------")
#condition = [False,True,True]
con =data1["salary"] >= 18000 
print(data1[con]["name"])
#print(data1)
condition = data1["sex"] == "female"
#print(condition)
filterdata = data1[condition] 
print(filterdata)
