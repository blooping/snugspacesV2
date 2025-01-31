import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.state('zoomed')
root.configure(background='white')

#frame para d gumalaw
side_frame = tk.Frame(root, bg="white")
side_frame.pack(side="left", fill="y")

# Load and resize logo
snugspacelogo = Image.open("Rental Management images/snugspaceheading.png")
resized_logo = snugspacelogo.resize((302,100), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_logo)
logo_label = tk.Label(side_frame, image=logo_img,borderwidth=0,bg='white')
logo_label.pack()


#Dashboard button
dashboard_img = Image.open("Rental Management images/Dashboard.png")
resized_dashboard = dashboard_img.resize((300, 100), Image.LANCZOS)
dashboard_img_tk = ImageTk.PhotoImage(resized_dashboard)
dashboard_button = tk.Button(side_frame, image=dashboard_img_tk,borderwidth=0,bg='white')
dashboard_button.pack()

# Room button
room_img = Image.open("Rental Management images/Rooms.png")
resized_room = room_img.resize((300, 100), Image.LANCZOS)
room_img_tk = ImageTk.PhotoImage(resized_room)
room_button = tk.Button(side_frame, image=room_img_tk,borderwidth=0,bg='white')
room_button.pack()

# Tenant button
tenant_img = Image.open("Rental Management images/Tenants.png")
resized_tenant = tenant_img.resize((300, 100), Image.LANCZOS)
tenant_img_tk = ImageTk.PhotoImage(resized_tenant)
tenant_button = tk.Button(side_frame, image=tenant_img_tk,borderwidth=0,bg='white')
tenant_button.pack()

# payment button
payment_img = Image.open("Rental Management images/Payment.png")
resized_payment = payment_img.resize((300, 100), Image.LANCZOS)
payment_img_tk = ImageTk.PhotoImage(resized_payment)
payment_button = tk.Button(side_frame, image=payment_img_tk,borderwidth=0,bg='white')
payment_button.pack()

# analytics button
analytics_img = Image.open("Rental Management images/analytics.png")
resized_payment = analytics_img.resize((300, 100), Image.LANCZOS)
analytics_img_tk = ImageTk.PhotoImage(resized_payment)
analytics_button = tk.Button(side_frame, image=analytics_img_tk,borderwidth=0,bg='white')
analytics_button.pack()

# accounts button
acc_img = Image.open("Rental Management images/Account.png")
resized_acc = acc_img.resize((300, 100), Image.LANCZOS)
acc_img_tk = ImageTk.PhotoImage(resized_acc)
acc_button = tk.Button(side_frame, image=acc_img_tk,borderwidth=0,bg='white')
acc_button.pack()

#Rental button
rent_img = Image.open("Rental Management images/Rental.png")
resized_rent = rent_img.resize((300, 100), Image.LANCZOS)
rent_img_tk = ImageTk.PhotoImage(resized_rent)
rent_button = tk.Button(side_frame, image=rent_img_tk,borderwidth=0,bg='white')
rent_button.pack()


#room label
tenant_frame = tk.Frame(root,height=10,width=500)
tenant_frame.place(x=325,y=60)

tenant_label=tk.Label(tenant_frame,text="Tenants",bg='white',font=('times new roman',20,'bold'))
tenant_label.pack()

#occupied
occupied_rdbutton=tk.Radiobutton(bg='white')
occupied_rdbutton.place(x=1000,y=70)

occupied_frame = tk.Frame(root,height=10,width=500)
occupied_frame.place(x=1025,y=70)

occupied_label=tk.Label(occupied_frame,text="Occupied",bg='white',font=('times new roman',12,'bold'))
occupied_label.pack()

#avalable
available_rdbutton=tk.Radiobutton(bg='white')
available_rdbutton.place(x=1140,y=70)

available_frame = tk.Frame(root,height=10,width=500)
available_frame.place(x=1160,y=70)

available_label=tk.Label(available_frame,text="Available",bg='white',font=('times new roman',12,'bold'))
available_label.pack()

#room list
frame_width =1160
frame_height = 500
bg_color='pink'

# Create a frame to hold the listbox
frame = tk.Frame(root, width=frame_width, height=frame_height,relief="raised",borderwidth=5)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.place(x=325,y=98)

# Create a scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create the Treeview (multi-column listbox)
columns = ("Tenant Id", "Name", "Age","Birthday","Gender","Email","Contact No",
           "Address","Balance")
tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=tree.yview)

# Define the column headings with specified background and foreground colors
style = ttk.Style()
style.configure("Treeview.Heading", foreground="black", font=("Times new roman", 15, "bold"),relief="raised",borderwidth=5,bd=1)
style.configure("Treeview", foreground="black", fieldbackground="blue", font=("Helvetica", 10))

# Define row stripe colors
style.map("Treeview", background=[("selected", "#2C6FBC")], foreground=[("selected", "black")])

# Define the column headings
tree.heading("Tenant Id", text="Tenant Id")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Birthday",text="Birthday")
tree.heading("Gender",text="Gender")
tree.heading("Email",text="Email")
tree.heading("Contact No",text="Contact No")
tree.heading("Address",text="Address")
tree.heading("Balance",text="Balance")

# Define the column widths
tree.column("Tenant Id", width=100,anchor='n')
tree.column("Name", width=150,anchor='n')
tree.column("Age", width=80,anchor='n')
tree.column("Birthday", width=150,anchor='n')
tree.column("Gender", width=100,anchor='n')
tree.column("Email", width=140,anchor='n')
tree.column("Contact No", width=110,anchor='n')
tree.column("Address", width=150,anchor='n')
tree.column("Balance", width=100,anchor='n')


# Insert some sample data
sample_data = [
    (1, "John Doe", 28, "1996-03-15", "Male", "johndoe@example.com", "123-456-7890", "123 Main St, Anytown, USA",
     1200.50),
    (2, "Jane Smith", 32, "1992-07-22", "Female", "janesmith@example.com", "234-567-8901", "456 Elm St, Othertown, USA",
     850.75),
    (3, "Mike Johnson", 45, "1979-01-05", "Male", "mikejohnson@example.com", "345-678-9012", "789 Oak St, Anycity, USA",
     450.00),
    (4, "Emily Davis", 27, "1997-11-30", "Female", "emilydavis@example.com", "456-789-0123",
     "321 Pine St, Othercity, USA", 1050.25),
    (5, "Robert Brown", 35, "1988-05-17", "Male", "robertbrown@example.com", "567-890-1234",
     "654 Maple St, Sometown, USA", 625.40),
    (6, "Sarah Wilson", 29, "1995-09-12", "Female", "sarahwilson@example.com", "678-901-2345",
     "987 Birch St, Yourtown, USA", 980.60),
    (7, "David Lee", 41, "1983-04-21", "Male", "davidlee@example.com", "789-012-3456", "123 Cedar St, Theirtown, USA",
     720.90),
    (8, "Laura Clark", 26, "1998-02-28", "Female", "lauraclark@example.com", "890-123-4567",
     "456 Spruce St, Ourtown, USA", 810.80),
    (
    9, "James White", 50, "1974-08-14", "Male", "jameswhite@example.com", "901-234-5678", "789 Willow St, Hiscity, USA",
    670.55),
    (10, "Linda Harris", 38, "1986-12-06", "Female", "lindaharris@example.com", "012-345-6789",
     "321 Fir St, Hercity, USA", 530.35)
]

for item in sample_data:
    tree.insert("", "end", values=item)

add_frame = tk.Frame(root)
add_frame.place(x=825,y=670)
Login = tk.Button(add_frame,text="Add a New Tenant",font=("times new roman",12,"bold"), pady= 5, padx= 20,background= "#2C6FBC",width=10)
Login.pack()



root.mainloop()