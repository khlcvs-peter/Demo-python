import time
import hashlib
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import os
import glob
import csv
app_key = 'f24fc42d1c574e2c84755ccc'
secret_key = '60475a5140d672c8f361cd114091bca3'
host = 'tc.stu.edu.tw'
timestamp = int(time.time()) # 一個 10 碼的時間 timestamp 數字
# 產生一個臨時檔案
stu_id = input("請輸入STU ID  : ")
root_folder = "E:\data"
def get_txt_files(root_folder):
    txt_files = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in glob.glob(os.path.join(foldername, '*.csv')):
            txt_files.append(filename)
    return txt_files

# 使用示例
files = get_txt_files(root_folder)
for txt_file in files:
    print(txt_file)
    filename = txt_file[8:]
    # 在 TC 建立檔案的 meta 資料
    url_partial = '/external-api/v2/ono/uploads?app_key={}&ts={}'.format(app_key,timestamp)
    token = hashlib.md5((url_partial + secret_key).encode()).hexdigest()[:20]
    target_url = 'https://{}{}&token={}'.format(host, url_partial, token)
    response = requests.post(target_url,data=json.dumps( 
    { 
    "name": filename, 
    "size": int(1.8), 
    "user_no": stu_id, 
    "allow_download": False, 
    "is_folder": False, 
    "parent_id": 0, 
    } ), 
    headers={"Content-Type": "application/json"},)
    url = response.json().get("upload_url") 
    fields = {"file": (filename, open(txt_file, "rb"))}
    m = MultipartEncoder(fields=fields) 
    response = requests.put(url, data=m, headers={"Content-Type": m.content_type})
print(response.status_code,response.json())# 解析JSON响应
if response.status_code == 200:
    print(f"文件 {stu_id} 上传成功")
        
# 如果请求失败，打印错误消息
    print('Failed to retrieve data. Status code:', response.status_code)
    