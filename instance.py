#point
# class Point :
#     def __init__(self) -> None:
#         self.x =3
#         self.y =4
# p1 = Point()
# print(p1.x,p1.y)

# class Point2 :
#     def __init__(self,a,b) :
#         self.x = a
#         self.y= b
# p2=Point2(5,6)
# p3=Point2(7,8)
# print(p2.x*p2.y)
# print(p1.x + p2.x + p1.y + p2.y)
# print(p3.x,p3.y)

#fullname
class Fullname :
    def __init__(self,first,last ) -> None:
        self.first = first
        self.last = last
    def say(self):
        return("歡迎光臨")
    def show(self):
        return("這是Python程式")
name1=input("please enter first name :")
name2 = input("please enter last name :")
result = Fullname(name1,name2)
print(result.say(),result.first,result.last ,result.show())