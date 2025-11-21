height = 11 
for i in range(height): 
    print((' ' * (height - i)) + ('*' * ((2 * i) + 1))) 
print((' ' * height) + '||')
############################################################
import os 
import random 

height1 = 11 
for i in range(height1): 
    print(' ' * (height1 - i), end='') 
    for j in range((2 * i) + 1): 
        if random.random() < 0.1: 
            color = random.choice(['\033[1;31m', '\033[33m', '\033[1;34m']) 
            print(color, end='') # 彩燈 
        else: 
            print('\033[32m', end='') # 綠色 
        print('*', end='') 
    print() 
print((' ' * height1) + '||')
print("Merry Christmas 聖誕節快樂 \n by 王獻章  ")
os.system("pause")
