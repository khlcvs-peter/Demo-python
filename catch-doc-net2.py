import requests
import gdown
from docx import Document
import tempfile
import os

# === 輸入分享資料夾 ID ===
# 範例連結：https://drive.google.com/drive/folders/1bSLnsbJOTsRZ9I0vA3ije8cInwkGpIif?usp=sharing
FOLDER_ID = "1bSLnsbJOTsRZ9I0vA3ije8cInwkGpIif"

# === 取得公開 JSON feed ===
url = f"https://drive.google.com/drive/u/0/folders/{FOLDER_ID}"
res = requests.get(f"https://drive.google.com/drive/folders/{FOLDER_ID}?hl=zh-TW")

if res.status_code != 200:
    print("❌ 無法連線至 Google Drive，請檢查網路或分享連結。")
    exit()

# === 從頁面原始碼中擷取檔案資訊（新版 Drive 格式） ===
import re
pattern = r'\[\[\["(.*?)","(.*?)","(.*?)","(.*?)","(.*?)"'
matches = re.findall(pattern, res.text)

file_list = []
for m in matches:
    if m[1].endswith(".docx"):
        file_name = m[1]
        file_id = m[0]
        file_list.append((file_name, file_id))

if not file_list:
    print("⚠️ 沒有找到任何 .docx 文件，請確認資料夾內有 .docx 檔。")
    exit()

# === 顯示檔案清單 ===
print("找到以下 DOCX 文件：")
for i, (name, _) in enumerate(file_list, 1):
    print(f"{i}. {name}")

choice = int(input("請輸入要讀取的文件編號：")) - 1
file_name, file_id = file_list[choice]

print(f"\n📄 正在下載：{file_name} ...")

# === 使用 gdown 下載 ===
file_url = f"https://drive.google.com/uc?id={file_id}"
with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_file:
    gdown.download(file_url, tmp_file.name, quiet=False)
    tmp_path = tmp_file.name

# === 讀取 DOCX 文件內容 ===
document = Document(tmp_path)
print("\n=== 文件內容 ===")
for para in document.paragraphs:
    print(para.text)

# === 清理暫存檔案 ===
os.remove(tmp_path)
