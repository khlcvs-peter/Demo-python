import os
import re
import csv
from zeep import Client
from zeep.exceptions import Fault

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

    def get_bas_teacher(self, id_key):
        """查詢教師基本資料"""
        return self.call_api("GetBasTeacher", IDKey=id_key)

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
    print("\n查詢教師資料...")
    teacher_response = soap_service.get_bas_teacher(id_key)

    if teacher_response:
        # 轉換為字串，確保能夠儲存
        teacher_response_str = str(teacher_response)
        save_to_file("result.txt", teacher_response_str)

# 合併 result.txt 與 result1.txt
def merge_files(file1, file2, output_file):
    """將兩個檔案合併並儲存為 output_file"""
    try:
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            content = f1.read() + "\n" + f2.read()
        
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(content)
        print(f"檔案已合併並儲存至 {output_file}")
    except Exception as e:
        print(f"[File Error] 無法合併檔案: {e}")

# 合併檔案
merge_files("result.txt", "result1.txt", "result.txt")

# 清理文本內容
def clean_text(text):
    """刪除指定文字與特殊字元"""
    text = text.replace("GetBasTeacherResult", "")
    text = text.replace("tbltmp", "")
    text = text.replace("_value_1", "")
    text = text.replace("'schema': <Schema(location=None, tns=None)>", "")
    text = re.sub(r"[\{\}\[\]\,\'':\ \/n]", "", text)  # 移除 {} 和 []
    return text

# 轉換檔案為 CSV
def convert_txt_to_csv(txt_filename, csv_filename):
    """讀取 result.txt，解析多筆資料並轉換成 result.csv"""
    headers = ["TEACHER_CODE", "NAME", "GENDER", "EMAIL", "TEL", "ACCOUNT", "IS_TEACHER", "EDU_DEPT"]
    data_list = []  # 存放多筆資料
    data_dict = {}  # 暫存單筆資料

    try:
        with open(txt_filename, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]  # 移除空白行
        
        for line in lines:
            match = re.match(r"([A-Z_]+)(\d*.*)", line)  # 擷取 KEY 和 VALUE
            if match:
                key, value = match.groups()

                # 如果遇到新的 TEACHER_CODE，代表新的一筆資料開始
                if key == "TEACHER_CODE" and data_dict:
                    data_list.append(data_dict)  # 先儲存上一筆
                    data_dict = {}  # 清空暫存字典
            
                data_dict[key] = value  # 存入當前資料

        if data_dict:  # 儲存最後一筆資料
            data_list.append(data_dict)

        # 確保每筆資料都有所有欄位，沒有則補空字串
        rows = [[data.get(header, "") for header in headers] for data in data_list]

        # 寫入 CSV 檔案
        with open(csv_filename, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)  # 寫入標題
            writer.writerows(rows)  # 寫入所有資料

        print(f"已成功轉換 {txt_filename} 為 {csv_filename}，共 {len(data_list)} 筆資料")

    except Exception as e:
        print(f"[Error] 無法處理文件: {e}")

# 轉換 result.txt 為 CSV
convert_txt_to_csv("result.txt", "get-teacher.csv")
