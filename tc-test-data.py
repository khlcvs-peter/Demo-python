import time
import hashlib
import requests
import json 
app_key = 'f24fc42d1c574e2c84755ccc'
secret_key = '60475a5140d672c8f361cd114091bca3' 
host = 'tc.stu.edu.tw' 
timestamp = int(time.time())
#timestamp = int(1695893389)
 # 一個10碼的時間 timestamp數字 
 #  產生一個臨時檔案
filename = "test_file.txt"
f = open(filename, "w+")
f.write("it is a test file")
f.seek(0, 2)
 # 在 TC 建立檔案的 meta 資料 
url_partial = '/external-api/v2/ono/uploads?app_key={}&ts={}'.format(app_key, timestamp)
token = hashlib.md5((url_partial + secret_key).encode()).hexdigest()[:20]
#token = '73406d843c2f30d95401'
target_url = 'https://{}{}&token={}'.format(host, url_partial, token)
response = requests.post(target_url,
    data=json.dumps( 
    { 
    "name": f.name, 
    "size": f.tell(), 
    "user_no": "stu01", 
    "allow_download": False, 
    "is_folder": False, 
    "parent_id": 0, 
    } ), 
    headers={"Content-Type": "application/json"},) 
f.close()
 # 利用上面回傳的 upload_url 參數開始上傳檔案，上傳完成才算完整成功
print(response)
print(response.status_code, response.json())
if response.status_code == 201:
    url = response.json().get("upload_url") 
    fields = {"file": (filename, open(filename, "rb"))}
    m = MultipartEncoder(fields=fields) 
    response = requests.put(url, data=m, headers={"Content-Type": m.content_type})
    print(response.status_code, response.json())
#  # 刪除臨時檔案 os.remove("test_file.txt")