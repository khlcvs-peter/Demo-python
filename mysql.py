import pymysql as py
# 连接到MySQL数据库
#conn = pymysql.Connect(host ='myadmin.stu.edu.tw',user='admin', password='cnacc', database='stu-moodle')
conn = py.connect(host="10.1.0.43", user="admin", passwd="cnacc", database="stu-moodle") 
# 创建一个游标对象，用于执行SQL语句
cur = conn.cursor()
# 执行SQL查询
cur.execute("SELECT firstname,email FROM `mdl_user` WHERE email 
             NOT LIKE ('s1%') AND email NOT LIKE ('s2%') AND email 
             NOT LIKE ('s9%') AND email NOT LIKE ('user%') AND email  
             LIKE ('%@stu%')order by firstname ASC")

            
# 获取所有查询结果
rows = cur.fetchall()

# 打印查询结果
for row in rows:
    print(row)

# 关闭游标和数据库连接
cur.close()
conn.close()
