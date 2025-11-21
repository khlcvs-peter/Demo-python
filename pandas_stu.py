# use pandas to get json file
#import json
import pandas as pd
data = pd.read_csv("mdl_user.csv")
#print(data)
#print("data total:",data.shape)
#print("data columns",data.columns)

# print(data["firstaccess"])
# print("+++++++++++++++++++++++++++++++++")
# condition = data["password"] == "2012-08-21 18:21:41"
# #print(condition)
# data=data[condition]
# print(data)
# print("=================================")
# print("平均數",data["firstaccess"].mean())
# print("中位數",data["firstaccess"].median())
# print("前20名的中位數",data["firstaccess"].nlargest(20).mean())
print("----------------------------------------------------------------")
#data is not clear use function to clear it. for example 10000+ , free100; 
#data["firstaccess"] = pd.to_numeric(data["firstaccess"].str.replace("[,+],""").replace("Free",""))
data["firstaccess"] = pd.to_numeric(data["firstaccess"])
print(data["firstaccess"].mean())
print(data["firstaccess"].median())
       
con = data["firstaccess"] >= 1427675848
print("over ",data[con].shape[0])
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
keyword = input("please inter keyword ")
con = data["firstname"].str.contains(keyword)
print(data[con]["firstname"])
print("the keyword for APP",data[con].shape[0])