from tkinter import *
from datetime import date
window=Tk()
window.title("sample")
window.geometry("500x700")
lbl=Label(text="hello everyone", fg="orange", bg="blue",height= 1, width=300)
name=Label(text="full name", fg="green", bg="yellow")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    Message="welcome to the application! \n today's date is "
    greet="hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box=Text(height=3)
btn=Button(text="began",command=display,height=1,fg="red",bg="black")
lbl.pack()
name.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()