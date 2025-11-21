
import os
from io import BytesIO
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from docx import Document

# 權限：可讀取 Google Drive 檔案
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_credentials():
    """取得 Google OAuth2 憑證（若 credentials.json 不存在則提醒）"""
    if not os.path.exists('credentials.json'):
        print("⚠️ 找不到 'credentials.json' 憑證檔，請依下列步驟建立：")
        print("1️⃣ 進入 https://console.cloud.google.com/")
        print("2️⃣ 建立專案並啟用 Google Drive API")
        print("3️⃣ 建立『OAuth 2.0 用戶端 ID』 (選桌面應用程式)")
        print("4️⃣ 下載 JSON 檔並重新命名為 credentials.json")
        print("5️⃣ 放入與此程式相同資料夾中，再重新執行程式")
        exit(1)

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def list_docx_files(service, folder_id):
    """列出指定資料夾中的所有 DOCX 檔案"""
    query = f"'{folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    return results.get('files', [])

def download_docx_file(service, file_id, file_name):
    """從 Google Drive 下載 .docx 檔案並讀取內容"""
    try:
        request = service.files().get_media(fileId=file_id)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)
        doc = Document(fh)
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
        return text
    except Exception as e:
        print(f"❌ 無法解析 {file_name}: {e}")
        return None

def main():
    # ✅ 請在這裡輸入你的 Google Drive 資料夾 ID
    FOLDER_ID = "1ikACGNurRLwmpAiKOvep9MdTHF01pXKE"

    creds = get_credentials()
    drive_service = build('drive', 'v3', credentials=creds)

    files = list_docx_files(drive_service, FOLDER_ID)
    print(f"\n📂 找到 {len(files)} 個 DOCX 檔案：\n")

    for f in files:
        print(f"📄 {f['name']}")
        content = download_docx_file(drive_service, f['id'], f['name'])
        if content:
            print(content[:300])  # 顯示前300字
            print("-" * 60)

if __name__ == "__main__":
    main()
