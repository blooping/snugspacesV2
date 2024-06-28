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
payment_frame = tk.Frame(root,height=10,width=500)
payment_frame.place(x=325,y=60)
payment_label=tk.Label(payment_frame,text="Payment",bg='white',font=('times new roman',20,'bold'))
payment_label.pack()


#search entry for payment
searchpayentry_frame = tk.Frame(root, bg="white")
searchpayentry_frame.place(x=835,y=70)
searchpay=tk.Entry(searchpayentry_frame,background="#D9D9D9",width=12,borderwidth=2,font=("helvica",13),relief='raised')
searchpay.pack()


#search button

searchbut_frame= tk.Frame(root,bg='white')
searchbut_frame.place(x=950,y=65)

searchpay_img = Image.open("Rental Management images/Google Web Search.png")
resized_searchpay = searchpay_img.resize((35,35), Image.LANCZOS)
searchpay_img_tk = ImageTk.PhotoImage(resized_searchpay)
searchpay_button = tk.Button(searchbut_frame, image=searchpay_img_tk,borderwidth=0,bg='white',relief='raised')
searchpay_button.pack()


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
columns = ("Tenant Id", "Name", "Due Date","Total Rent Due","Amount Paid","Payment Date")
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
tree.heading("Due Date", text="Due Date")
tree.heading("Total Rent Due",text="Total Rent Due")
tree.heading("Amount Paid",text="Amount Paid")
tree.heading("Payment Date",text="Payment Date")

# Define the column widths
tree.column("Tenant Id", width=100,anchor='n')
tree.column("Name", width=150,anchor='n')
tree.column("Due Date", width=80,anchor='n')
tree.column("Total Rent Due", width=200,anchor='n')
tree.column("Amount Paid", width=100,anchor='n')
tree.column("Payment Date", width=200,anchor='n')




# Insert some sample data
sample_data = [
(1, "John Doe", 1200.50, "Credit Card", "2023-06-01", "2023-01-01", "2024-01-01"),
    (2, "Jane Smith", 850.75, "Bank Transfer", "2023-06-02", "2022-07-01", "2023-07-01"),
    (3, "Mike Johnson", 450.00, "Cash", "2023-06-03", "2022-01-01", "2023-01-01"),
    (4, "Emily Davis", 1050.25, "Credit Card", "2023-06-04", "2023-02-01", "2024-02-01"),
    (5, "Robert Brown", 625.40, "Debit Card", "2023-06-05", "2022-05-01", "2023-05-01"),
    (6, "Sarah Wilson", 980.60, "Bank Transfer", "2023-06-06", "2022-09-01", "2023-09-01"),
    (7, "David Lee", 720.90, "Credit Card", "2023-06-07", "2022-04-01", "2023-04-01"),
    (8, "Laura Clark", 810.80, "Cash", "2023-06-08", "2023-02-01", "2024-02-01"),
    (9, "James White", 670.55, "Debit Card", "2023-06-09", "2021-08-01", "2022-08-01"),
    (10, "Linda Harris", 530.35, "Bank Transfer", "2023-06-10", "2022-12-01", "2023-12-01")
]

for item in sample_data:
    tree.insert("", "end", values=item)


#generate invoice frame
gen_frame = tk.Frame(root)
gen_frame.place(x=825,y=670)
gen = tk.Button(gen_frame,text="Generate Invoice",font=("times new roman",12,"bold"), pady= 5, padx= 20,background= "#2C6FBC",width=10)
gen.pack()



root.mainloop()