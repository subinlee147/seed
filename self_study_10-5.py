from tkinter import *
from tkinter.filedialog import askopenfilename

def func_open():
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))
    if filename:
        photo = PhotoImage(file=filename)
        
        w = photo.width()
        h = photo.height()
        
        for i in range(w):
            for k in range(h):
                r, g, b = photo.get(i, k) 
                grey = int((r + g + b) / 3)
                photo.put("#%02x%02x%02x" % (grey, grey, grey), (i,k))
        
        pLabel.configure(image=photo)
        pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy()

window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

window.mainloop()
