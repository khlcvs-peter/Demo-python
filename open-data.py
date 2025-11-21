#----------open network--------------------------------------
# import urllib.request as request
# src="https://www.stu.edu.tw/"
# with request.urlopen(src) as response :
#     data = response.read().decode("utf-8")
# print(data)

# with open("data.txt",mode="r",encoding="utf-8")as file :
#     for line in file :
# connect network---------------------------------------------
# import csv
# with open("C:\Users\User\Downloads\科技文選（網路教學） - BMU001020110223.csv",mode="r",encoding="utf-8")as response :
#     data = response.read()
# print(data)
#---------------------------------------------------------------

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import csv
# name = []
# email = []
# score = []
# path = "BMU001020110223.csv"
# with open("BMU001020110223.csv",mode="r",encoding="utf-8", newline='') as csvfile:
#     rows = csv.reader(csvfile, delimiter=',')
#     headers = next(rows)
#     print('headers: %s' % headers)
#     for row in rows:
#         name.append(row[0])
#         email.append(row[1])
#         score.append(int(row[2]))
#     print(name)
#     print(score)
    
# print(email)
# print(score)

# import csv
# name = []
# email = []
# score = []

# with open("BMU001020110223.CSV",mode="r",encoding="utf-8",newline='') as file :
#     data = csv.reader(file,delimiter=',')
#     header = next(data)
#     print('the data is ' %header)
#     for row in data :
#         name.append(row[0])
#         email.append(row[1])
#         score.append(int(row[2]))
#     print ("name",name)
#     print("email : ",email)
#     print("score is ",score)
#---------------------------------------------------------------
# import json
# with open("mdl_stc_ignore.json",mode="r",encoding="utf-8") as file :
#     data = json.load(file)
#     print(data[2]['data'][0]['CourseCode'])
#     for item in data[2]['data']:
#         print(item['CourseCode']) 
#-------------------------------------------------------------------------------
import json
with open("mdl_stc_ignore.json",mode="r",encoding="utf-8") as file :
    result = json.load(file)
with open("open-data.txt",mode="w",encoding="utf-8") as paper :    
    for data in result[2]['data'] :
        paper.write(data['CourseCode']+"\n")
        print(data['CourseCode'])








   