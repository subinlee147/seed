## 5 ##

ss = 'Python'
for i in range(0,len(ss)):
    print(ss[i]+ '$', end ='')
    
#--- answer : P$y$t$h$o$n$


## 9 ##

inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0,strLen) : 
    outStr += inStr[strLen - (i+1)]
print("내용을 거꾸로 출력 --> %s"%outStr)

#--- answer : 내용을 거꾸로 출력 --> nohtyP


## 11 ##

text = '파이썬 ### CookBook $$$ @@@ 열공중 1234'
for c in text:
    if c.isalpha():
        print(c, end='')

#--- answer : 파이썬CookBook열공중

## 13 ##

import turtle
import random
import math
from tkinter.simpledialog import *

#전역 변수 선언 부분#
inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = [0]*3

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')


for i, ch in enumerate(inStr):
    tX = 200* math.cos(math.radians(360*2)/ len(inStr)-i)
    tY = 200* math.sin(math.radians(360*2)/ len(inStr)-i)


    r= random.random(); g= random.random() ; b= random.random()
    txtSize = 20
    
    turtle.goto(tX,tY)
    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은 고딕',txtSize,'bold'))
    
turtle.done()





# 원 모양으로 문자열을 배치하여 출력
for i, ch in enumerate(inStr):
    angle = 360*2 / len(inStr) * i
    radius = 200
    tX = radius * math.cos(math.radians(angle))
    tY = radius * math.sin(math.radians(angle))

