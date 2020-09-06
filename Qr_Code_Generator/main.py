from tkinter import*


root = Tk()
root.geometry('390x350')
root.title('Qr Code Generator')

data=StringVar()

def Click():
    print(data.get())

def Clear():
    data.set("")

Label(root,text=("Qr Code Generator"),font=('arial',20,'bold')).place(x=60,y=10)
Label(root,text=("Enter Data "),font=('arial',15,'bold')).place(x=50,y=100)
Entry(root,text=("Enter Data "),font=('arial',15)).place(x=50,y=140,width=280,height=30)
e1=Entry(root,font=('arial',15),textvariable=data)
e1.focus()
e1.place(x=50,y=140)

Button(root,text=("CLICK Here "),font=('arial',14,'bold'),command=Click).place(x=130,y=220,width=120)
Button(root,text=("Clear "),font=('arial',12,'bold'),command=Clear).place(x=140,y=280,width=100)



root.mainloop()
