<<<<<<< HEAD
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
    import time
    import hashlib
    import requests
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    import json
    import os
    from pathlib import Path

    # Config
    app_key = 'f24fc42d1c574e2c84755ccc'
    secret_key = '60475a5140d672c8f361cd114091bca3'
    host = 'tc.stu.edu.tw'


    def get_files(root_folder, extensions=None):
        """Walk `root_folder` and return list of files matching `extensions`.

        `extensions` should be an iterable of lowercase suffixes like ('.csv', '.xlsx').
        """
        if extensions is None:
            extensions = ('.csv', '.xlsx')
        root = Path(root_folder)
        results = []
        for p in root.rglob('*'):
            if p.is_file() and p.suffix.lower() in extensions:
                results.append(str(p))
        return results


    def upload_file_to_tc(file_path, stu_id):
        timestamp = int(time.time())
        url_partial = '/external-api/v2/ono/uploads?app_key={}&ts={}'.format(app_key, timestamp)
        token = hashlib.md5((url_partial + secret_key).encode()).hexdigest()[:20]
        target_url = 'https://{}{}&token={}'.format(host, url_partial, token)

        filename = Path(file_path).name
        # Create metadata
        payload = {
            "name": filename,
            "size": int(1.8),
            "user_no": stu_id,
            "allow_download": False,
            "is_folder": False,
            "parent_id": 0,
        }
        resp = requests.post(target_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        try:
            upload_url = resp.json().get("upload_url")
        except Exception:
            print('Failed to get upload URL, response:', resp.text)
            return False

        with open(file_path, 'rb') as fh:
            fields = {"file": (filename, fh)}
            m = MultipartEncoder(fields=fields)
            put_resp = requests.put(upload_url, data=m, headers={"Content-Type": m.content_type})

        print(put_resp.status_code)
        try:
            print(put_resp.json())
        except Exception:
            print(put_resp.text)

        return put_resp.status_code == 200


    if __name__ == '__main__':
        stu_id = input("請輸入STU ID  : ")
        root_folder = r"E:\data"
        files = get_files(root_folder)
        if not files:
            print('No matching files found in', root_folder)
        for f in files:
            print('Uploading', f)
            ok = upload_file_to_tc(f, stu_id)
            if ok:
                print(f"文件 {stu_id} 上傳成功: {f}")
            else:
                print('Failed to upload file:', f)
    