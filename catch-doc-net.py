#需要安裝的套件：
#pip install pydrive python-docx
#pip install gdown python-docx
import os
import gdown
from docx import Document

# === 設定分享資料夾 ID ===
# 分享連結: https://drive.google.com/drive/folders/XXXXXX?usp=sharing
FOLDER_ID = "https://drive.google.com/drive/folders/1ikACGNurRLwmpAiKOvep9MdTHF01pXKE?usp=sharing"

DOWNLOAD_DIR = "downloaded_docs"

def download_folder(folder_id: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    gdown.download_folder(id=folder_id, output=output_dir, quiet=False, use_cookies=False)

def list_docx_files(dirpath: str):
    return [f for f in os.listdir(dirpath) if f.lower().endswith(".docx")]

def read_docx_file(filepath: str):
    document = Document(filepath)
    for para in document.paragraphs:
        print(para.text)

def main():
    # 1) 下載整個資料夾
    download_folder(FOLDER_ID, DOWNLOAD_DIR)

    # 2) 抓取下載到的 DOCX 檔案
    docx_files = list_docx_files(DOWNLOAD_DIR)

    if not docx_files:
        print("⚠️ 沒有找到任何 .docx 文件")
        return

    print("找到以下 DOCX 文件：")
    for i, f in enumerate(docx_files, 1):
        print(f"{i}. {f}")

    # 3) 讓使用者選擇要讀的文件（包含輸入防錯處理）
    try:
        choice = int(input("請輸入要讀取的文件編號：").strip()) - 1
        if choice < 0 or choice >= len(docx_files):
            print("輸入的編號不在範圍內")
            return
    except ValueError:
        print("輸入錯誤，請輸入數字")
        return

    file_path = os.path.join(DOWNLOAD_DIR, docx_files[choice])

    # 4) 讀取 DOCX 內容
    print("\n=== 文件內容 ===")
    read_docx_file(file_path)

if __name__ == "__main__":
    main()
