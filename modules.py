#import sys

import sys as s



print(s.path)
s.path.append("modules")
print(s.path)
import geometry as geo
# print(s.maxsize)
data = geo.distance(1,1,5,5)
print(data)
data =geo.slope(1,2,5,6)
print (data)
print(s.path)
# sys.path.append("modules")
#print(sys.path)
