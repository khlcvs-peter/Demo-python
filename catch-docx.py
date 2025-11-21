
import os
from docx import Document

def list_docs(folder="."):
    """列出資料夾內的 docx 檔案"""
    files = [f for f in os.listdir(folder) if f.endswith(".docx")]
    return sorted(files)

def read_docx(file_path):
    """讀取 docx 內容"""
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return "\n".join(content)

def main():
    # 🔹 新增：讓使用者輸入要讀取的資料夾路徑
    folder = input("👉 請輸入文章所在的資料夾路徑 (直接按 Enter 使用目前資料夾)：").strip()
    if folder == "":
        folder = "."  # 預設為目前資料夾
    
    if not os.path.isdir(folder):
        print("❌ 資料夾不存在，請確認路徑")
        return

    docs = list_docs(folder)

    if not docs:
        print("❌ 在指定資料夾中找不到任何 .docx 檔案")
        return

    print("\n📄 可選擇的文章：")
    for i, f in enumerate(docs, start=1):
        print(f"{i}. {f}")

    try:
        choice = int(input("\n👉 請輸入要開啟的文章編號："))
        if 1 <= choice <= len(docs):
            file_path = os.path.join(folder, docs[choice - 1])
            print(f"\n📖 文章內容 ({docs[choice - 1]})：\n")
            print(read_docx(file_path))
        else:
            print("❌ 無效的選擇")
    except ValueError:
        print("❌ 請輸入正確的數字")

if __name__ == "__main__":
    main()
