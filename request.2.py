from zeep import Client
from zeep.exceptions import Fault

class SoapWebService:
    def __init__(self, wsdl_url):
        """初始化 SOAP Web 服務"""
        self.client = Client(wsdl=wsdl_url)

    def call_api(self, method_name, **kwargs):
        """通用 API 呼叫函數，帶有錯誤處理"""
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

# 使用 Web 服務
if __name__ == "__main__":
    WSDL_URL = "https://mfser.stu.edu.tw/wbsforcuserviceapi/webservice1.asmx?WSDL"
    soap_service = SoapWebService(WSDL_URL)

    id_key = "EC0FC7EF-3EE3-4E0D-ADB6-1FFA8C526AE5"
    
    # 查詢教師資料
    print("\n查詢教師資料...")
    teacher_response = soap_service.get_bas_teacher(id_key)
    
    if teacher_response:
        # 將回應寫入 result.txt 檔案
        with open('result.txt', 'w', encoding='utf-8') as file:
            file.write(str(teacher_response))
        print("已將教師資料寫入 result.txt 檔案。")
    else:
        print("未獲取到教師資料，無法寫入檔案。")
