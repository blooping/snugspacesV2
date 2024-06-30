import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import font
from tkcalendar import DateEntry
import Accounts
import AddRental
import Analytics
import Breakdown
import CreateAccount
import Dashboard
import EditAccount
import Login
import Payment
import Rentals
import Room
import Tenant


# Root properties
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Snugspaces")

    # Window dimensions
    w = 725
    h = 450

    # Get the screen resolution of computer
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # Get window x & y position
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Center the window
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #root_label = tk.Label(root, text = "%dx%d+%d+%d" % (w, h, x, y),bg='white',font=('times new roman',24,'bold'))
    #root_label.pack()

    # this removes the maximize button
    root.resizable(0,0)
    root.configure(background='#4b7cdc')

# Cancel button
back_frame = tk.Frame(root, bg = 'white')
back_frame.place(x = "10", y = "10")

back_label = tk.Label(back_frame, text = " Cancel", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 12, 'bold'))
back_label.pack()

# Payment Details label
add_frame = tk.Frame(root, bg="white")
add_frame.place(x="50", y = "60")

add_label = tk.Label(add_frame, text = "Payment Details", bg = '#4b7cdc', fg = 'white', font = ('times new roman', 24, 'bold'))
add_label.pack()

# Tenant Name Label
tenantName_frame = tk.Frame(root, bg="#4b7cdc")
tenantName_frame.place(x="-30", y="125")

tenantName_label = tk.Label(tenantName_frame,text="Tenant Name", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
tenantName_label.pack()

# Tenant Name picture para soft edges
tenantName_pic = Image.open ("Rental Management images/long rectangle.png")
resized = tenantName_pic.resize((220,25),Image.Resampling.LANCZOS)
tenantName_pic = ImageTk.PhotoImage(resized)
tenantName_label = tk.Label(tenantName_frame, image = tenantName_pic,borderwidth=0,bg="#4b7cdc")
tenantName_label.pack(padx = (100, 0))

# Tenant Name entry
tenantNameEntry_frame = tk.Frame(root, bg="#4b7cdc")
tenantNameEntry_frame.place(x=80,y=155)
tenantName = tk.Entry(tenantNameEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
tenantName.pack()

# Total Rent Due Label
totRentDue_frame = tk.Frame(root, bg="#4b7cdc")
totRentDue_frame.place(x="-15", y="200")

totRentDue_label = tk.Label(totRentDue_frame,text="Total Rent Due", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
totRentDue_label.pack()

# Total Rent Due picture para soft edges
totRentDue_pic = Image.open ("Rental Management images/long rectangle.png")
resized = totRentDue_pic.resize((220,25),Image.Resampling.LANCZOS)
totRentDue_pic = ImageTk.PhotoImage(resized)
totRentDue_label = tk.Label(totRentDue_frame, image = totRentDue_pic,borderwidth=0,bg="#4b7cdc")
totRentDue_label.pack(padx = (85, 0))

# Total Rent Due entry
totRentDueEntry_frame = tk.Frame(root, bg="#4b7cdc")
totRentDueEntry_frame.place(x=80,y=230)
totRentDue = tk.Entry(totRentDueEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
totRentDue.pack()

# Due Date Label
dueDate_frame = tk.Frame(root, bg="#4b7cdc")
dueDate_frame.place(x="75", y="275")

dueDate_label = tk.Label(dueDate_frame,text="Due Date", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
dueDate_label.pack()

# Due Date entry
dueDateEntry_frame = tk.Frame(root, height=10, width=500,bg="white",borderwidth=0)
dueDateEntry_frame.place(x=85,y=305)

dueDateEntry= DateEntry(dueDateEntry_frame, font=('helvica',12))
dueDateEntry.pack()

# Amount to be Paid Label
amountPaid_frame = tk.Frame(root, bg="#4b7cdc")
amountPaid_frame.place(x="365", y="200")

amountPaid_label = tk.Label(amountPaid_frame,text="Amount to be Paid", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
amountPaid_label.pack()

# Amount to be Paid picture para soft edges
amountPaid_pic = Image.open ("Rental Management images/long rectangle.png")
resized = amountPaid_pic.resize((220,25),Image.Resampling.LANCZOS)
amountPaid_pic = ImageTk.PhotoImage(resized)
amountPaid_label = tk.Label(amountPaid_frame, image = amountPaid_pic,borderwidth=0,bg="#4b7cdc")
amountPaid_label.pack(padx = (55, 0))

# Amount to be paid entry
amountPaidEntry_frame = tk.Frame(root, bg="#4b7cdc")
amountPaidEntry_frame.place(x=445,y=230)
amountPaid = tk.Entry(amountPaidEntry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
amountPaid.pack()

# Date of Payment label
dateOfPayment_frame = tk.Frame(root, bg="#4b7cdc")
dateOfPayment_frame.place(x="425", y="275")

dateOfPayment = tk.Label(dateOfPayment_frame,text="Date of Payment", bg = '#4b7cdc', fg = 'white' , font=('times new roman',14,'bold'))
dateOfPayment.pack()

# Date of Payment entry
dateOfPayment_frame = tk.Frame(root, height=10, width=500,bg="white",borderwidth=0)
dateOfPayment_frame.place(x=435,y=305)

dateOfPaymentEntry= DateEntry(dateOfPayment_frame, font=('helvica',12))
dateOfPaymentEntry.pack()

# Confirm button
button_frame = tk.Frame(root)
button_frame.place(x=550, y=375)
createAcc_button = tk.Button(button_frame, text = 'Confirm', fg = 'white', bg = '#2c6fbc', font = (("Times New Roman"),14), width = 8)
createAcc_button.pack()

root.mainloop()