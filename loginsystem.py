from tkinter import*
from PIL import Image,ImageTk

root = Tk()
root.title("Registration Form")
root.geometry("1366x768")
root.config(bg="white")

#Background Image"
bg= ImageTk.PhotoImage(file="Images/Background.jpg")
label=Label(root, image=bg).place(relwidth=1, relheight=1)

title =Label(root, text="REGISTER HERE", font=("Comic Sans MS", 20, "bold"), bg="white", fg="Black").place(x=180, y =90)

f_name = Label(root, text="First Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 160)
txt_fname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=165, width=250)

f_name = Label(root, text="Last Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 220)
txt_fname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=225, width=250)

f_name = Label(root, text="Email Address", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 280)
txt_fname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=285, width=250)

f_name = Label(root, text="Contact No.", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 340)
txt_fname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC") .place(x=220,y=345, width=250)

chk = Checkbutton(root, text="I agree to the terms and conditions", font=("Comic Sans MS",11), bg="white") .place(x=150,y=400)
btn = Button(root, text="SUBMIT", font=("Comic Sans MS",13), bg="#52be80", fg="black") .place(x=250, y=450)
root.mainloop()