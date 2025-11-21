#需要安裝的套件：
#pip install pydrive python-docx
#pip install gdown python-docx
import os
import gdown
from docx import Document

# === 設定分享資料夾 ID ===
# 分享連結: https://drive.google.com/drive/folders/XXXXXX?usp=sharing
FOLDER_ID = "https://drive.google.com/drive/folders/1ikACGNurRLwmpAiKOvep9MdTHF01pXKE?usp=sharing"

# === 第一步：下載整個資料夾 ===
# gdown 會把所有檔案下載到 "downloaded_docs" 資料夾
os.makedirs("downloaded_docs", exist_ok=True)
gdown.download_folder(id=FOLDER_ID, output="downloaded_docs", quiet=False, use_cookies=False)

# === 第二步：抓取下載到的 DOCX 檔案 ===
docx_files = [f for f in os.listdir("downloaded_docs") if f.endswith(".docx")]

if not docx_files:
    print("⚠️ 沒有找到任何 .docx 文件")
    exit()

print("找到以下 DOCX 文件：")
for i, f in enumerate(docx_files, 1):
    print(f"{i}. {f}")

# === 第三步：讓使用者選擇要讀的文件 ===
choice = int(input("請輸入要讀取的文件編號：")) - 1
file_path = os.path.join("downloaded_docs", docx_files[choice])

# === 第四步：讀取 DOCX 內容 ===
document = Document(file_path)

print("\n=== 文件內容 ===")
for para in document.paragraphs:
    print(para.text)
