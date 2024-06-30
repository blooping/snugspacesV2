import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font
import Accounts
import AddPayment
import AddRental
import Analytics
import Breakdown
import CreateAccount
import Dashboard
import EditAccount
import Login
import Payment
import Rentals
import Tenant

root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.state('zoomed')
root.configure(background='#3A98CC')

#frame para d gumalaw
side_frame = tk.Frame(root, bg="#3A98CC")
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
room_frame = tk.Frame(root,height=10,width=500)
room_frame.place(x=400,y=60)

room_label=tk.Label(room_frame,text="Rooms",bg='#3A98CC',font=('times new roman',20,'bold'))
room_label.pack()

#occupied
occupied_rdbutton=tk.Radiobutton(bg='#3A98CC')
occupied_rdbutton.place(x=1200,y=115)

occupied_frame = tk.Frame(root,height=10,width=500)
occupied_frame.place(x=1225,y=115)

occupied_label=tk.Label(occupied_frame,text="Occupied",bg='#3A98CC',font=('times new roman',12,'bold'))
occupied_label.pack()

#avalable
available_rdbutton=tk.Radiobutton(bg='#3A98CC')
available_rdbutton.place(x=1340,y=115)

available_frame = tk.Frame(root,height=10,width=500)
available_frame.place(x=1360,y=115)

available_label=tk.Label(available_frame,text="Available",bg='#3A98CC',font=('times new roman',12,'bold'))
available_label.pack()

#room list
frame_width =1000
frame_height = 500
bg_color='pink'

# Create a frame to hold the listbox
frame = tk.Frame(root, width=frame_width, height=frame_height,relief="raised",borderwidth=5)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.place(x=430,y=170)

# Create a scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create the Treeview (multi-column listbox)
columns = ("Room No", "Room Rate", "Room Status")
tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=scrollbar.set)
tree.pack(fill="both", expand=True)

# Configure the scrollbar
scrollbar.config(command=tree.yview)

# Define the column headings with specified background and foreground colors
style = ttk.Style()
style.configure("Treeview.Heading", foreground="black", font=("Times new roman", 15, "bold"),relief="raised",borderwidth=5,bd=1)
style.configure("Treeview", foreground="black", fieldbackground="blue", font=("Helvetica", 13))

# Define row stripe colors
style.map("Treeview", background=[("selected", "#2C6FBC")], foreground=[("selected", "black")])

# Define the column headings
tree.heading("Room No", text="Room No")
tree.heading("Room Rate", text="Room Rate")
tree.heading("Room Status", text="Room Status")

# Define the column widths
tree.column("Room No", width=200,anchor='n')
tree.column("Room Rate", width=100,anchor='n')
tree.column("Room Status", width=200,anchor='n')



# Insert some sample data
sample_data = [
    ("210", 300, "Vacant"),
    ("584", 250, "Occupied"),
    ("945", 350, "Occupied"),
    ("856", 280, "Vacant"),
    ("978", 220, "Occupied")
]

for item in sample_data:
    tree.insert("", "end", values=item)




root.mainloop()