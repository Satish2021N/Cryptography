from tkinter import*
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox

'''Connect to Database'''
conn = sqlite3.connect('userdata.db')

'''Create a Cursor'''
c = conn.cursor()

'''Create a Table'''
c.execute("""CREATE TABLE IF NOT EXISTS Information(
            Firstname text,
            Lastname text,
            Email text,
            Contact number
            )""")

'''Commit to Database'''
conn.commit()

'''Close our connection'''
conn.close()

def insert_record():
    check_counter=0
    warn=""
    if txt_fname.get()=="":
        warn="First Name can't be empty"
    else:
        check_counter+=1
    if txt_lname.get()=="":
        warn="Last Name can't be empty"
    else:
        check_counter+=1
    if txt_email.get()=="":
        warn="Email can't be empty"
    else:
        check_counter+=1
    if txt_contact.get()=="":
        warn="Contact No. can't be empty"
    else:
        check_counter+=1
    if check_counter==4:
        # try:
            conn=sqlite3.connect('userdata.db')
            c=conn.cursor()
            c.execute("INSERT INTO Information VALUES (:firstname,:lastname, :email, :contact,)", {
                        'Firstname': txt_fname.get(),
                        'Lastname': txt_lname.get(),
                        'Email': txt_email.get(),
                        'Contact':txt_contact.get()
                     })
            conn.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

         # except Exception as ep:
         #    messagebox.showerror('', ep)

    else:
        messagebox.showerror('Error', warn)

root = Tk()
root.title("Registration Form")
root.geometry("1366x768")
root.config(bg="white")


'''Background Image"'''
bg= ImageTk.PhotoImage(file="Images/Background.jpg")
label=Label(root, image=bg).place(relwidth=1, relheight=1)

'''Title'''
title =Label(root, text="REGISTER HERE", font=("Comic Sans MS", 20, "bold"), bg="white", fg="Black").place(x=180, y =90)

'''Widgets'''

f_name = Label(root,text="First Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 160)
txt_fname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC").place(x=220,y=165, width=250)

l_name = Label(root, text="Last Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 220)
txt_lname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=225, width=250)

e_address = Label(root, text="Email Address", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 280)
txt_email =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=285, width=250)

c_contact = Label(root, text="Contact No.", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 340)
txt_contact =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=345, width=250)

chk = Checkbutton(root, text="I agree to the terms and conditions", font=("Comic Sans MS",11), bg="white") .place(x=150,y=400)
btn_register = Button(root, text="REGISTER", font=("Comic Sans MS",13),bd=0,cursor="hand2", command=insert_record, bg="#52be80", fg="black") .place(x=250, y=450)


root.mainloop()