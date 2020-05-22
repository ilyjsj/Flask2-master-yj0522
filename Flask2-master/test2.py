#import test1
from test1 import add, sub, BusinessCard
print(__name__)
result = add(3,4)
print(result)

shkim = BusinessCard("sungho kim")
shkim.print_info()
result1 = sub(4,5)
print(result1)

#result1 = sub(5,4)
#print(result1)
