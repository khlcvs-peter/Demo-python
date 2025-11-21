# save file----------------------------
# file = open("data.txt",mode = "w",encoding="utf-8")
# file.write("5\n3\n10")
# file.close()
#open file-------------------------------------------
# with open("data.txt",mode="w",encoding="utf-8") as file :
#     file.write("3\n6")
# with open("data.txt",mode="r",encoding="utf-8")as file :
#     data = file.read()
# print("the file is \n",data)
# sum =0
# with open("data.txt",mode="r",encoding="utf-8")as file :
#     for line in file :
#         sum+=int(line)
# print("the sum is ",sum)
# with open("data.txt",mode="r",encoding="utf=8") as file :
#     for data in file:
#         print(data)
#close file----------------------------------------------
# import json
# with open("config.json",mode="r",encoding="utf-8") as file :
#     data =json.load(file)
# # print("name",data["name"])
# # print("version",data["version"])
# # print("title",data["title"])
# print(data)
# data["name"] = "new name"
# print(data)
# with open("config.json",mode="w",encoding="utf-8") as file:
#     json.dump(data,file)
# print(data)
#R+ ------------------------------------------
with open("data.txt",mode="w",encoding="utf-8") as paper :
    paper.write("\n test\n測試")
with open("data.txt",mode="r+",encoding="utf-8") as paper :
    for data in paper :
        print(data)
    paper.write("\n 好棒棒 \n good job ")
with open("data.txt",mode="r+",encoding="utf-8") as paper :
    data1 = paper.read()
    print(data1)
with open("data.txt",mode="r+",encoding="utf-8") as paper :
    for data in paper :
        print(data)
    