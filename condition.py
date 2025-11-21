#判斷式 If while true:
# x=int(input("請輸入數字 : ")) 
# if x>=200:
#     print("over 200")
# elif x >= 150:
#     print("over 150" )
# elif x>= 100:
#     print("over 100")
# else:
#     print("False")

n1 = int(input("請樹入數字"))
n2 = int(input("請輸入 第二數字"))
n3 = input("輸家加減符號")
if n3 == "+" :
    sum = n1 +n2
    print(sum)
elif n3 == "-" :
    sum = n1-n2
    print(sum)
elif  n3 == "*" :
    sum = n1 * n2
    print(sum)
elif n3 == "/" :
    sum = n1/n2
    print(sum)
else :
    print("wrong") 


