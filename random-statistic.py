import random
# data = random.sample([1,2,5,6,8,10,20,25],5)
# print(data)
#-----------------------------------------------------------------------
# random.shuffle(data)
# print(data) 
#----------------------------------------
# data =random.random()
# data1  =random.uniform(1.0,100.0)
# data2 =int(data1)
# print(data)
# print(data2)
#------------------------------------------------
# data=[1,2,5,6,8,10,20,25]
# data1 =random.choice(data)
# print(data1)
# data = random.normalvariate(100,10)
# print(data)
#----------------------------------------------------------
import statistics as stat
# data = stat.mean([1,2,5,6,8,10,20,525])
# print(data)
# data = stat.median([1,2,3,4,5,525])
# print(data)
# data = stat.median_high([1,2,3,4,5,525])
# print(data)
# data = stat.median_low([1,2,3,4,5,525])
# print(data)
#----------------------------------------------
data = stat.stdev([1,2,5,6,8,10,20,25])
print(data)