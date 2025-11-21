#pip install google-auth google-auth-oauthlib google-api-python-client python-docx


import os
from io import BytesIO
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from docx import Document

# 權限：只讀取 Drive 檔案
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_credentials():
    """取得 OAuth2 憑證"""
    if not os.path.exists('credentials.json'):
        print("⚠️ 找不到 credentials.json，請先建立 OAuth 2.0 憑證（桌面應用程式）。")
        exit(1)

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def list_docx_files(service, folder_id):
    """列出指定資料夾內所有 DOCX 檔案"""
    query = f"'{folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document' and trashed=false"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    return results.get('files', [])

def read_docx_from_drive(service, file_id):
    """從 Google Drive 下載 .docx 檔案並讀取內容"""
    request = service.files().get_media(fileId=file_id)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()

    fh.seek(0)
    document = Document(fh)
    text = "\n".join([p.text for p in document.paragraphs if p.text.strip()])
    return text

def main():
    # ⚠️ 修改這裡成你的 Google Drive 資料夾 ID
    FOLDER_ID = "1ikACGNurRLwmpAiKOvep9MdTHF01pXKE"

    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)

    # === 列出 DOCX 檔案 ===
    files = list_docx_files(service, FOLDER_ID)
    if not files:
        print("⚠️ 找不到任何 .docx 檔案")
        return

    print("\n📂 找到以下 DOCX 檔案：\n")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f['name']}")

    # === 讓使用者選擇要讀取的檔案 ===
    try:
        choice = int(input("\n請輸入要讀取的檔案編號（或 0 離開）："))
        if choice == 0:
            print("👋 已離開。")
            return
        selected_file = files[choice - 1]
    except (ValueError, IndexError):
        print("❌ 無效的輸入")
        return

    print(f"\n📥 正在下載並讀取：{selected_file['name']} ...")

    try:
        content = read_docx_from_drive(service, selected_file['id'])
        print("\n=== 文件內容預覽 ===\n")
        print(content[:800] if content else "（此文件無文字內容）")
    except Exception as e:
        print(f"❌ 讀取文件時發生錯誤：{e}")

if __name__ == "__main__":
    main()
