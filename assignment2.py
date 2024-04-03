## 3 ##

def plus (v1,v2,v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = plus(100,200,300)
print(hap)

#--> answer : 600


## 4 ##

def f1():
    print(var)
    
def f2():
    var = 10
    print(var)
    
var = 100
f1()
f2()

#--> answer
#f1() = 100
#f2() = 10

## 8 ##

def myFunc(p1=1,p2=2,p3=3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==>", myFunc())
print("매개변수가 1개로 호출 ==>", myFunc(1))
print("매개변수가 2개로 호출 ==>", myFunc(1,2))
print("매개변수가 3개로 호출 ==>", myFunc(1,2,3))

## 11 ##

def addNumber(num):
    if num == 0:
       return 0
    else:
       return num + addNumber(num - 1)
print(addNumber(100))