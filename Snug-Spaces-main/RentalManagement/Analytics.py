import tkinter as tk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data
from tkinter import ttk

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
resized_analytics = analytics_img.resize((300, 100), Image.LANCZOS)
analytics_img_tk = ImageTk.PhotoImage(resized_analytics)
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




# Main frame for scrollbar
main_frame = tk.Frame(root,bg='blue')
main_frame.place(x=300,height=1000,width=1600)

# Create a canvas
my_canvas = tk.Canvas(main_frame)
my_canvas.place(height=1000,width=1650)

# Create a scrollbar
scrollbar_y = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
scrollbar_y.pack(side='right', fill='y')

# Configure the canvas
my_canvas.configure(yscrollcommand=scrollbar_y.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

# Create another frame inside the canvas
charts_frame = tk.Frame(my_canvas)
charts_frame.pack()

# Add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=charts_frame, anchor="ne",height=1000,width=1650)

#mga graph
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#2C6FBC"])

# Chart 2: Horizontal bar chart of inventory data
fig1, ax1 = plt.subplots()
ax1.barh(list(inventory_data.keys()), inventory_data.values())
ax1.set_title("Today's Tenant")
ax1.set_ylabel("")
# plt.show()

# Chart 3: Pie chart of product data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values())
ax2.set_title("Monthly Tenats")
ax2.set_ylabel("")
# plt.show()

# Chart 4: Line chart of sales by year
fig3, ax3 = plt.subplots()
ax3.barh(list(inventory_data.keys()), inventory_data.values())
ax3.set_title("Checkout")
ax3.set_ylabel("")
# plt.show()

# Chart 5: Area chart of inventory by month
fig4, ax4 = plt.subplots()
ax4.barh(list(inventory_data.keys()), inventory_data.values())
ax4.set_title("Rooms")
ax4.set_ylabel("")
# plt.show()


upper_frame = tk.Frame(charts_frame,bg='white')
upper_frame.pack(fill="both", expand=True)

room_label=tk.Label(upper_frame,text="Analytics",bg='white',font=('times new roman',20,'bold'))
room_label.pack()


#available rooom
avail_img = Image.open("Rental Management images/Rental.png")
resized_avail = avail_img.resize((300, 100), Image.LANCZOS)
avail_img_tk = ImageTk.PhotoImage(resized_avail)



canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)





root.mainloop()