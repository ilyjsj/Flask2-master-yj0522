def add(a,b):             #add(int a, int b) {   }
    return a+b           #c, java 함수리턴 값 1개
def sub(a,b):
    return a-b

class BusinessCard:                    # class BusinessCard {field int weight   }
    def __init__(self, name):          # class 내의 멤버함수
        self.name = name               # this (C++ : pointer java this -> reference

    def print_info(self):
        print("---------------")
        print("name:", self.name)

        # python modules -> package
        # java  packages -> module      :: class, interface...
        # matplotlib.  . -> subdirectory
