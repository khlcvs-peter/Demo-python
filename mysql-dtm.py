import pymysql as py
import csv
import html
# 连接到MySQL-Dtm数据库
conn = py.connect(host="10.1.0.45", user="admin", passwd="cnacc", database="stu-dtm") 


# 创建一个游标对象，用于执行SQL语句
cur = conn.cursor()
# 执行SQL查询
cur.execute("SELECT course,mdl_course.idnumber,mdl_course.shortname, externalurl \
            FROM `mdl_url` INNER JOIN mdl_course ON mdl_url.course = mdl_course.id \
            WHERE startdate >= '1694361600' AND year_term = '1122'")
            
# 获取所有查询结果
# 获取所有查询结果
rows = cur.fetchall()

#寫入到mysql3.txt 文件資料中
with open("mysql3.csv",mode = "w",encoding="utf-8") as file:
    for row in rows:
        file.write(str(row) + '\n')
        #print(row)
with open("mysql3.csv",mode="r",encoding="utf-8",newline='') as file :
    data = file.read()
    data1 = (html.unescape(data))
    

#寫入到mysql4.txt 文件資料中
with open("mysql4.csv",mode = "w",encoding="utf-8",newline='') as file1:
    for row in data1:
        #file1.write(str(row) + '\n')
        file1.write(str(row) )
        
# 打印查询结果
# 关闭游标和数据库连接
cur.close()
conn.close()
