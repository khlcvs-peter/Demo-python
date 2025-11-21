import time
import hashlib
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import os
import glob
import pymysql
app_key = 'f24fc42d1c574e2c84755ccc'
secret_key = '60475a5140d672c8f361cd114091bca3'
host = 'tc.stu.edu.tw'
timestamp = int(time.time()) # 一個 10 碼的時間 timestamp 數字
# 產生一個臨時檔案
stu_id = 'stuadmin'

filename = 'view'
# 在 TC 建立檔案的 meta 資料
url_partial = '/external-api/v2/ono/uploads?app_key={}&ts={}'.format(app_key,timestamp)
token = hashlib.md5((url_partial + secret_key).encode()).hexdigest()[:20]
target_url = 'https://{}{}&token={}'.format(host, url_partial, token)
# conn = pymysql.connect(host='tc.stu.edu.tw', user='stuadmin', password='el vm/6uo4tl6', database='lms')




# with open('vw_file_status.json', 'r') as file:
#     data = json.load(file)

# # 获取表格头部
# header = data['table']['header']

# # 获取表格数据
# table_data = data['table']['data']

# # 打印表格头部
# print("Table Header:")
# print(header)

# # 打印表格数据
# print("Table Data:")
# for row in table_data:
#     print(row)

# # print(response.status_code,response.json())# 解析JSON响应


def list_directory(path):
    # 初始化一个字典，用于存储目录结构
    directory_structure = {'path': path, 'contents': []}

    try:
        # 获取目录下的文件和子目录
        contents = os.listdir(path)
        
        # 遍历每个文件或子目录
        for item in contents:
            item_path = os.path.join(path, item)
            
            # 如果是目录，递归获取其目录结构
            if os.path.isdir(item_path):
                item_structure = list_directory(item_path)
            else:
                item_structure = {'file': item, 'path': item_path}
            
            # 将当前项的结构添加到目录结构中
            directory_structure['contents'].append(item_structure)
    
    except Exception as e:
        # 处理可能的异常，例如权限不足等
        directory_structure['error'] = str(e)

    return directory_structure

# 指定目录路径
directory_path = 'view vw_file_satus'

# 获取目录结构
result = list_directory(directory_path)

# 将结果输出为 JSON 字符串
json_result = json.dumps(result, indent=2)
print(json_result)