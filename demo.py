from tkinter import *
import tkinter.font as tkFont

def insertItem():
    listbox.insert(END, content.get())
    entry.delete(0, END)
def deleteAll():
    listbox.delete(0, END)

def deleteItem():
    listbox.delete(ANCHOR)

tk = Tk()

tk.title("Memo list")
tk.geometry("527x600")
tk.resizable(0,0)

titleFont = tkFont.Font(family="Verdana", size=20)
inpFont = tkFont.Font(family="Verdana", size=13)
textFont = tkFont.Font(family="Verdana", size=10)

titleLabel = Label(tk, text="LIST TO DO TODAY", font=titleFont)
titleLabel.place(x=120,y=20)

yScrollbar = Scrollbar(tk, orient="vertical")
yScrollbar.pack(side=RIGHT, fill=Y)

xScrollbar = Scrollbar(tk, orient="horizontal")
xScrollbar.pack(side=BOTTOM, fill=X)

listbox = Listbox(tk, width=44, height=20, font=inpFont, xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set, bg="#36382e", fg="#ede6e3")
listbox.place(x=10, y=60)


yScrollbar.config(command=listbox.yview)
xScrollbar.config(command=listbox.xview)

content = StringVar()

entry = Entry(tk, width=35 ,textvariable=content, font=inpFont)
entry.insert(0,"Enter your plan")
entry.place(x=10, y=500)

btnInsert = Button(tk, text="Insert item", font=textFont ,command=insertItem, bg="#5bc3eb", fg="#36382e")
btnInsert.place(x=400, y=500)

btnDelItem = Button(tk, text="Delete Item", font=textFont, command=deleteItem, bg="#21bf73", fg="#36382e")
btnDelItem.place(x=300, y=550)

btnDelAll = Button(tk, text="Delete All", font=textFont, command=deleteAll, bg="#f06449", fg="#36382e")
btnDelAll.place(x=400, y=550)







tk.mainloop()

