from tkinter import*
from tkinter import messagebox
from PIL import image,ImageTk

root=Tk()
root.title("Denomination Counter")
root.configure(bg='light blue')
root.geometry('650x400')
label=label(root  
            text=hey user ,welcome to Denomination Counter application
              bg=light blue  )
label1.place(relx=0.5 , y=340, anchor=CENTER)
def msg ():
    Msgbox=messagebox.showinfo(
        "Alert"do you want to calculate the Denomination count ?)
        if Msgbox=ok
        topwin()
    button1 = Button(root,
                     text = "let's get started"
                     command = msg,
                     bg = brown,
                     fg=wihte)
button1.place("x=260 , y=360")

def topwin()
top=tplevel()
top.tile"Denomination Counter"
root.configure(bg='light blue')
root.geometry('600x350 + 50+50')


label=label(top, text="enter total amount" bg= light grey)
entry = Entry (top)
lbl=label(top, text = "here are number of note for each Denomination" bg=light grey )