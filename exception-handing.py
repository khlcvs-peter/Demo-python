#exception
#輸入錯誤 請他再次輸入 直到正確
while True:
    data = input("輸入數字")
    try:
        number = int(data)
        break
    except Exception :
        number = 0

    print("資料錯誤 請再次輸入 : ")
number = number*2
print(number)