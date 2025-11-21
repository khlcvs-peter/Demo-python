# break----------------------------
# x =0
# while x < 5 :
#     if x == 3 :
       
#         break
    
#     x +=1 
#     print(x)
# print("x  =", x )

#continue-----------------------------
# n=0
# for x in [8,5,41,55,24,77,25,20,79] :
    
#     if x%2 == 1 :
#         continue
#     print("x is ",x)
#     n += 1
# print("n is ",n)
# sum = 0
# x = 0
# y = 0
# sum1 =0
# while x <11 :
#     sum  += x
#     x += 1
# else:
#     print("sum = " , sum)
# for y in range(11) :
#     sum1 += y
#     #y += 1
# else:
#     print("sum1 =" , sum1)
#     print("avg is ",sum1//y)

#else--------------------------------
x = int(input("請輸入一個數字 找尋是否有平方根"))
i =0

for i in range(x) :
    if i ** 2 == x :
        print("整數平方根",i)
        break
else :
    print("none")    
