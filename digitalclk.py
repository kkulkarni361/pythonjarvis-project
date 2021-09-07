import datetime
import time
from  tkinter import *
import  calendar

root = Tk()

root.geometry("500x200+0+0")
root.configure(background = "black")
root.resizable(0,0)

root.overrideredirect(1)


def start():
    text = (time.strftime("%H:%M:%S"), time.strftime("%d:%m:%y"))

    label.config(text= text)

    label.after(200,start)

   # label.config(text=dd)
label = Label(root,font=("ds-digital",50,'bold'),bg='white',fg='green',bd=50)
label.grid(row=1,column=2)
start()
print("done")
root.mainloop()