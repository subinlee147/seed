## 3 ##
from tkinter import *
window = Tk()

def rdo_change() :
    if var.get() == 1:
        label1.configure(text = "벤츠")
    else :
        label1.configure(text="포르쉐")

var = IntVar()
rdo1 = Radiobutton(window, text = "벤츠", variable = var , value = 1, command= rdo_change)
rdo2 = Radiobutton(window, text = "포르쉐", variable = var , value = 2, command= rdo_change)

label1 = Label(window, text="선택한 차량", fg="red")
rdo1.pack()
rdo2.pack()
label1.pack()

window.mainloop()

## 4 ##

#답만 작성
#(1) LEFT
#(2) RIGHT
#(3) TOP
#(4) BOTTOM

## 5 ##

from tkinter import *
from time import *

fnameList = ["one.gif", "two.gif", "three.gif"]
num = 0

def clickNext():
    global num
    num = (num + 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

def clickPrev():
    global num
    num = (num - 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

val = Tk()

pLabel = Label(val, text=fnameList[num])
pLabel.pack()

prevButton = Button(val, text="이전", command=clickPrev)
prevButton.pack(side=LEFT)

nextButton = Button(val, text="다음", command=clickNext)
nextButton.pack(side=RIGHT)

val.mainloop()
