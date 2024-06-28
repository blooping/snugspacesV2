import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.state('zoomed')
root.configure(background='#ffffff')

#frame para d gumalaw
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(relwidth=1, relheight=1)

#logo picture
my_pic = Image.open ("Rental Management images/SnugSpaceslogo.png")
resized = my_pic.resize((300,300),Image.Resampling.LANCZOS)
new_pic = ImageTk.PhotoImage(resized)
my_label = tk.Label(Login_frame, image=new_pic,borderwidth=0)
my_label.pack(pady=(100,0))

Username= tk.Label (text="Username",background="white")
Username.pack(pady=(420,0),padx=(0,193))

#eto ung entry
User=tk.Entry(background="#D9D9D9",width=40,borderwidth=0)
User.pack(pady=(20,0))

#email picture para soft edges
User_pic = Image.open ("Rental Management images/long rectangle.png")
resized = User_pic.resize((250,35),Image.Resampling.LANCZOS)
User_pic = ImageTk.PhotoImage(resized)
User_label = tk.Label(Login_frame, image=User_pic,borderwidth=0,bg="white")
User_label.pack(pady=(50,0))


Passwordname= tk.Label (text="Password",background="white")
Passwordname.pack(pady=(20,0), padx=(0,185))

#eto ung entry
password=tk.Entry(background="#D9D9D9",width=40,borderwidth=0)
password.pack(pady=(15,0))

#password picture para soft edges
pass_pic = Image.open ("Rental Management images/long rectangle.png")
resized = pass_pic.resize((250,35),Image.Resampling.LANCZOS)
pass_pic = ImageTk.PhotoImage(resized)
pass_label = tk.Label(Login_frame, image=pass_pic,borderwidth=0,bg="white")
pass_label.pack(pady=(40,0))





Login = tk.Button(Login_frame,text="Log in", pady= 5, padx= 20,background= "#2C6FBC")
Login.pack(pady=(25,0))

Termsandco = tk.Label (Login_frame,text= "By logging into our system, you acknowledge that you have read and understood the Terms of Use and Privacy statement to our"
                      " collection, use, and sharing of your personal information as described.", background="white")
Termsandco.pack(pady=(30,0))


root.mainloop()