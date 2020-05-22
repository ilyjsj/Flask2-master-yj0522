#import my1
from my1 import add, BusinessCard, Woman
print(__name__)

#result = my1.add(3,4)
result = add(3,4)
print(result)

#a = my1.BusinessCard("Kimsungho")
a = BusinessCard("Kimsungho")
a.print_info()

#she = my1.Woman(55,100,160)
she = Woman(55,100,160)

she.print_her_info()

she.eat()
she.study()
she.sleep()

she.print_her_info()
