#def function-----------------------------------------
# def multiply():
#     print(3*4)
# multiply() 
# def multiply(n1,n2):
#     n3 = n1*n2
#     return n3

# result = multiply(3,4)
# print("the answer is ",result)
# def add(n1,n2):
#     n3 = n1 +n2
#     return n3
# def sub(n1,n2) :
#     n3 = n1- n2
#     return n3
# def mul(n1,n2) :
#     n3=n1*n2
#     return n3
# def duv(n1,n2) :
#     n3 = n1/n2
#     return n3
# n1=int(input("please insert the integer number1 "))
# n2=int(input("please insert the integer number2 "))
# count=input("please insert the function(+ - * /)")
# if count == '+' :
#     result =add(n1,n2)
#     print("the add is ",result )
# elif count == "-" :
#     result = sub(n1,n2)
#     print("the sub is ", result) 
# elif count == "*" :
#     result = mul(n1,n2)
#     print("the mul is ",result) 
# elif count == "/" :
#     result = duv(n1,n2) 
#     print("the duv is ",result)
# else:
#     print("the prpgram is error") 

def cal(max) :
    sum = 0
    for x in range(1,max+1) :
        sum += x
    print("sum is ",sum)    
    return sum
result = cal(0)
result1=cal(10)
result2 = cal(20)
print("the result is ",result) 
print("the result is ",result1) 
print("the result is ",result2) 
#call function-----------------------------------------
