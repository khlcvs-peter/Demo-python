import html;
import csv;
path = "mysql3.csv"
#c1 = ()
c2 = []
c3 = []
with open("mysql3.csv",mode="r",encoding="utf-8",newline='') as file :
    #data = csv.reader(file,delimiter=',')
    data = file.read()
    data1 = (html.unescape(data))
    #print(data1)

#寫入到mysql4.txt 文件資料中
with open("mysql4.csv",mode = "w",encoding="utf-8",newline='') as file1:
    for row in data1:
        #file1.write(str(row) + '\n')
        file1.write(str(row) )
        
