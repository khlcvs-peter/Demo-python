import os
import re
from zeep import Client
from zeep.exceptions import Fault
def main():
    print("這是 查詢系所基本資料.py 的主要功能！")

class SoapWebService:
    def __init__(self, wsdl_url):
        """初始化 SOAP Web 服務"""
        try:
            self.client = Client(wsdl=wsdl_url)
        except Exception as e:
            print(f"[Initialization Error] 無法連接 WSDL: {e}")
            self.client = None  # 防止後續調用出錯

    def call_api(self, method_name, **kwargs):
        """通用 API 呼叫函數，帶有錯誤處理"""
        if not self.client:
            print("[Error] SOAP Client 未初始化")
            return None

        try:
            response = getattr(self.client.service, method_name)(**kwargs)
            print(f"API Response: {response}")  # 打印 API 回應
            return response
        except Fault as fault:
            print(f"[SOAP Fault] {fault}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")
        return None

    def GetSection(self, id_key):
        """查詢系所基本資料"""
        return self.call_api("GetSection", IDKey=id_key)

def save_to_file(filename, data):
    """將結果寫入文件"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)
        print(f"結果已儲存至 {filename}")
    except Exception as e:
        print(f"[File Error] 無法寫入文件: {e}")

# 使用 Web 服務
if __name__ == "__main__":
    WSDL_URL = "https://mfser.stu.edu.tw/wbsforcuserviceapi/webservice1.asmx?WSDL"
    soap_service = SoapWebService(WSDL_URL)

    id_key = "EC0FC7EF-3EE3-4E0D-ADB6-1FFA8C526AE5"
    
    # 查詢教師資料
    print("\n查詢系所資料...")
    teacher_response = soap_service.GetSection(id_key)

    if teacher_response:
        # 轉換為字串，確保能夠儲存
        teacher_response_str = str(teacher_response)
        save_to_file("GetSection.txt", teacher_response_str)
import re

def clean_text(text):
    """刪除指定文字與特殊字元"""
    # 移除 'tbltmp'
    
    text = text.replace("GetSectionResult", "")
    text = text.replace("tbltmp", "")
    text = text.replace("_value_1", "")
    text = text.replace("'schema': <Schema(location=None, tns=None)>", "")
    
    # 移除 {} 和 []
    text = re.sub(r"[\{\}\[\]\,\'':\ \/n]", "", text)
    #text = re.sub(r"[\{\}\[\]\,\''\ \/n]", "", text)
    
    return text
def clean_file(filename):
    """讀取檔案，刪除空白文字與空白行，並重新寫入檔案"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # 移除每行前後空白，並過濾掉空行
        cleaned_lines = [line.strip() for line in lines if line.strip()]

        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(cleaned_lines))

        print(f"已清理並更新 {filename}")

    except Exception as e:
        print(f"[File Error] 無法處理文件: {e}")

# 執行清理
clean_file("GetSection1.txt")

def process_file(input_file, output_file):
    """讀取檔案、處理文字，並寫入新檔案"""
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            content = infile.read()

        cleaned_content = clean_text(content)

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(cleaned_content)
        
        print(f"已處理並儲存至 {output_file}")
    except Exception as e:
        print(f"[File Error] {e}")

def clean_file(filename):
    """讀取檔案，刪除空白文字與空白行，並重新寫入檔案"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # 移除每行前後空白，並過濾掉空行
        cleaned_lines = [line.strip() for line in lines if line.strip()]

        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(cleaned_lines))

        print(f"已清理並更新 {filename}")

    except Exception as e:
        print(f"[File Error] 無法處理文件: {e}")


# 執行檔案處理
process_file("GetSection.txt", "GetSection1.txt")

import os
import re

# 設定目標目錄
folder_path = "your_folder_path"  # 替換為你的TXT文件夾路徑
keywords = ["目標關鍵字1", "目標關鍵字2"]  # 你要查找的關鍵字列表

# 正則表達式匹配特殊符號
special_chars_pattern = r'[(),{}"\']'

def clean_text(text):
    """去除特殊符號"""
    return re.sub(special_chars_pattern, '', text)

def search_keywords_in_txt(folder):
    """遍歷TXT文件並搜尋關鍵字"""
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

                # 去除特殊符號
                cleaned_content = clean_text(content)

                # 查找關鍵字
                for keyword in keywords:
                    if keyword in cleaned_content:
                        print(f"文件: {filename} 發現關鍵字: {keyword}")
                        print(f"內容: {cleaned_content}\n")

# 執行搜尋
#search_keywords_in_txt(folder_path)
import csv
import re

def convert_txt_to_csv(txt_filename, csv_filename):
    """讀取 GetSection1.txt，解析多筆資料並轉換成 GetSection.csv"""
    headers = ["SectioNO", "SectioName"]
    data_list = []
    data_dict = {}

    try:
        with open(txt_filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]

        for line in lines:
            # ✅ 改良：允許 SectioNO 後接任意字母或數字
            match = re.match(r"^(SectioNO|SectioName)([A-Za-z0-9]*)\s*(.*)$", line)
            
            if match:
                key, suffix, value = match.groups()
                if suffix:  # 有附加編號（例如 E1 或 87）
                    key = key  # 不變
                    value = suffix if not value else value  # 處理無空格情況
                
                # ✅ 新一筆資料的開始條件：遇到 SectioNO
                if key == "SectioNO" and data_dict:
                    data_list.append(data_dict)
                    data_dict = {}

                data_dict[key] = value.strip()

        # ✅ 追加最後一筆
        if data_dict:
            data_list.append(data_dict)

        # 寫入 CSV
        with open(csv_filename, "w", encoding="utf-8-sig", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            for data in data_list:
                writer.writerow([data.get("SectioNO", ""), data.get("SectioName", "")])

        print(f"✅ 已成功轉換 {txt_filename} → {csv_filename}，共 {len(data_list)} 筆資料")

    except Exception as e:
        print(f"[Error] 無法處理文件: {e}")


# 執行轉換
convert_txt_to_csv("GetSection1.txt", "GetSection.csv")

file_path = "GetSection1.txt" 
if os.path.exists(file_path):
    os.remove(file_path)
file_path = "GetSection.txt" 
if os.path.exists(file_path):
    os.remove(file_path)

