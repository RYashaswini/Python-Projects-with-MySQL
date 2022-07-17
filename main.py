from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database()
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

id = StringVar()
name = StringVar()
doj = StringVar()
email = StringVar()
gender = StringVar()
address = StringVar()

# Entries frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#2c3e50", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky='w')

lblId = Label(entries_frame, text="ID", font=("Calibri", 16), bg="#535c68", fg="white")
lblId.grid(row=1, column=0, padx=10, pady=10, sticky='w')
txtId = Entry(entries_frame, textvariable=id, font=("Calibri", 16), width=30)
txtId.grid(row=1, column=1, padx=10, pady=10, sticky='w')

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=2, padx=10, pady=10, sticky='w')
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=3, padx=10, pady=10, sticky='w')

lbldoj = Label(entries_frame, text="DOJ", font=("Calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky='w')
txtdoj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
txtdoj.grid(row=2, column=1, padx=10, pady=10, sticky='w')

lblemail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblemail.grid(row=2, column=2, padx=10, pady=10, sticky='w')
txtemail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtemail.grid(row=2, column=3, padx=10, pady=10, sticky='w')

lblgender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblgender.grid(row=3, column=0, padx=10, pady=10, sticky='w')
combogender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
combogender['values'] = ("Male", "Female")
combogender.grid(row=3, column=1, padx=10, pady=10, sticky='w')

lbladdress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lbladdress.grid(row=4, column=0, padx=10, pady=10, sticky='w')
txtaddress = Text(entries_frame,width=85,height=5,font=("Calibri",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,sticky='w')

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    id.set(row[0])
    name.set(row[1])
    doj.set(row[2])
    email.set(row[3])
    gender.set(row[4])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[5])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtId.get()=="" or txtName.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","please fill all the details")
        return
    db.insert(txtId.get(),txtName.get(),txtdoj.get(),txtemail.get(),combogender.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("Data inserted successfully!!")
    clearall()
    displayall()

def update_employee():
    if txtId.get() == "" or txtName.get() == "" or txtdoj.get() == "" or txtemail.get() == "" or combogender.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "please fill all the details")
        return
    db.update(txtId.get(), txtName.get(), txtdoj.get(), txtemail.get(), combogender.get(), txtaddress.get(1.0, END))
    messagebox.showinfo("Data updated successfully!!")
    clearall()
    displayall()
def delete_employee():
    db.delete(row[0])
    clearall()
    displayall()

def clearall():
    id.set("")
    name.set("")
    doj.set("")
    email.set("")
    gender.set("")
    address.set("")
    txtaddress.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky='w')

btnadd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Calibri",16,'bold'),fg="white",bg="#16a085", bd=0).grid(row=0,column=0)
btnedit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("Calibri",16,'bold'),fg="white",bg="#2988b9", bd=0).grid(row=0,column=1,padx=10)
btndelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Calibri",16,'bold'),fg="white",bg="#c0392b", bd=0).grid(row=0,column=2,padx=10)
btnclear=Button(btn_frame,command=clearall,text="Clear Details",width=15,font=("Calibri",16,'bold'),fg="white",bg="#f39c12", bd=0).grid(row=0,column=3,padx=10)


# Table frame
tree_frame= Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1980,height=520)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',18),rowheight=50)

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.column("2",width=5)
tv.heading("3",text="DOJ")
tv.column("3",width=5)
tv.heading("4",text="Email")
tv.column("4",width=10)
tv.heading("5",text="Gender")
tv.column("6",width=5)
tv.heading("6",text="Address")
tv.column("6",width=5)
tv['show']="headings"
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)


displayall()
root.mainloop()
