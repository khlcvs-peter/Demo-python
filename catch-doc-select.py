'''
import os
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
'''
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 權限：可讀取 Google Drive 與 Google Docs 文件
SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/documents.readonly'
]

def get_credentials():
    """取得 Google OAuth2 憑證（若 credentials.json 不存在則提醒）"""
    if not os.path.exists('credentials.json'):
        print("⚠️ 找不到 'credentials.json' 憑證檔，請依下列步驟建立：")
        print("1️⃣ 進入 https://console.cloud.google.com/")
        print("2️⃣ 建立專案並啟用 Google Drive API 與 Google Docs API")
        print("3️⃣ 建立『OAuth 2.0 用戶端 ID』 (選桌面應用程式)")
        print("4️⃣ 下載 JSON 檔並重新命名為 credentials.json")
        print("5️⃣ 放入與此程式相同資料夾中，再重新執行程式")
        exit(1)

    # 正常載入憑證流程
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def list_docx_files(service, folder_id):
    """列出指定資料夾中的所有 DOCX 檔案"""
    query = f"'{folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    return results.get('files', [])

def read_docx_file(docs_service, file_id):
    """讀取 Google Docs 內容（自動轉換 DOCX 格式）"""
    doc = docs_service.documents().get(documentId=file_id).execute()
    content = ""
    for element in doc.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for el in element['paragraph'].get('elements', []):
                if 'textRun' in el:
                    content += el['textRun']['content']
    return content

def main():
    # ✅ 請在這裡輸入你的 Google Drive 資料夾 ID https://drive.google.com/drive/folders/1ikACGNurRLwmpAiKOvep9MdTHF01pXKE?usp=sharing
    FOLDER_ID = "1ikACGNurRLwmpAiKOvep9MdTHF01pXKE"

    creds = get_credentials()
    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    files = list_docx_files(drive_service, FOLDER_ID)
    print(f"\n📂 找到 {len(files)} 個 DOCX 檔案：\n")

    for f in files:
        print(f"📄 {f['name']}")
        try:
            content = read_docx_file(docs_service, f['id'])
            print(content[:300])  # 顯示前300字
            print("-" * 60)
        except Exception as e:
            print(f"❌ 無法讀取 {f['name']}：{e}")

if __name__ == "__main__":
    main()
