import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Snugspaces")
root.geometry("1290x832")
root.configure(background='white')

#add frame para d gumalaw
add_frame = tk.Frame(root, bg="white")
add_frame.place(x=100,y=50)

add_label=tk.Label(add_frame,text="Add a New Rental",bg='white',font=('times new roman',25,'bold'))
add_label.pack()

#tenant details label
details_frame = tk.Frame(root, bg="white")
details_frame.place(x=120,y=110)
details_label=tk.Label(details_frame,text="Tenant Details",bg='white',font=('times new roman',22,'bold'))
details_label.pack()

#first name label
first_frame = tk.Frame(root, bg="white")
first_frame.place(x=120,y=150)
first_label=tk.Label(first_frame,text="First Name",bg='white',font=('times new roman',15,'bold'))
first_label.pack(padx=(0,150))

#first Name picture para soft edges
first_pic = Image.open ("Rental Management images/long rectangle.png")
resized = first_pic.resize((250,35),Image.Resampling.LANCZOS)
first_pic = ImageTk.PhotoImage(resized)
first_label = tk.Label(first_frame, image=first_pic,borderwidth=0,bg="white")
first_label.pack(pady=(15,0))

#frirst name entry
firstentry_frame = tk.Frame(root, bg="white")
firstentry_frame.place(x=140,y=203)
first=tk.Entry(firstentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
first.pack()


#Middle name label
middle_frame = tk.Frame(root, bg="white")
middle_frame.place(x=460,y=150)
middle_label=tk.Label(middle_frame,text="Middle Name",bg='white',font=('times new roman',15,'bold'))
middle_label.pack(padx=(0,130))

#Middle Name picture para soft edges
middle_pic = Image.open ("Rental Management images/long rectangle.png")
resized = middle_pic.resize((250,35),Image.Resampling.LANCZOS)
middle_pic = ImageTk.PhotoImage(resized)
middle_label = tk.Label(middle_frame, image=middle_pic,borderwidth=0,bg="white")
middle_label.pack(pady=(15,0))

#middle name entry
middleentry_frame = tk.Frame(root, bg="white")
middleentry_frame.place(x=480,y=203)
middle=tk.Entry(middleentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
middle.pack()


#Last name label
last_frame = tk.Frame(root, bg="white")
last_frame.place(x=810,y=150)
last_label=tk.Label(last_frame,text="Last Name",bg='white',font=('times new roman',15,'bold'))
last_label.pack(padx=(0,140))

#Last Name picture para soft edges
last_pic = Image.open ("Rental Management images/long rectangle.png")
resized = last_pic.resize((250,35),Image.Resampling.LANCZOS)
last_pic = ImageTk.PhotoImage(resized)
last_label = tk.Label(last_frame, image=last_pic,borderwidth=0,bg="white")
last_label.pack(pady=(15,0))

#Last name entry
lastentry_frame = tk.Frame(root, bg="white")
lastentry_frame.place(x=830,y=203)
last=tk.Entry(lastentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
last.pack()


#Age label
age_frame = tk.Frame(root, bg="white")
age_frame.place(x=120,y=260)
age_label=tk.Label(age_frame,text="Age",bg='white',font=('times new roman',17,'bold'))
age_label.pack(padx=(0,150))

#age picture para soft edges
age_pic = Image.open ("Rental Management images/small rectangle.png")
resized = age_pic.resize((100,35),Image.Resampling.LANCZOS)
age_pic = ImageTk.PhotoImage(resized)
age_label = tk.Label(age_frame, image=age_pic,borderwidth=0,bg="white")
age_label.pack(pady=(15,0),padx=(0,100))

#age name entry
ageentry_frame = tk.Frame(root, bg="white")
ageentry_frame.place(x=140,y=312)
age=tk.Entry(ageentry_frame,background="#D9D9D9",width=6,borderwidth=0,font=("helvica",13))
age.pack()

#Birthday label
bday_frame = tk.Frame(root, bg="white")
bday_frame.place(x=460,y=260)
bday_label=tk.Label(bday_frame,text="Birthday",bg='white',font=('times new roman',15,'bold'))
bday_label.pack(padx=(0,160))

#Birthday picture para soft edges
bday_pic = Image.open ("Rental Management images/long rectangle.png")
resized = bday_pic.resize((150,35),Image.Resampling.LANCZOS)
bday_pic = ImageTk.PhotoImage(resized)
bday_label = tk.Label(bday_frame, image=bday_pic,borderwidth=0,bg="white")
bday_label.pack(pady=(16,0),padx=(0,90))

#Bday entry
bdayentry_frame = tk.Frame(root, height=10, width=500,bg="white",borderwidth=0)
bdayentry_frame.place(x=480,y=313)
def on_entry_click(event):
    """Function that gets called whenever entry is clicked."""
    if entry.get() == 'mm/dd/yyyy':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='grey')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'mm/dd/yyyy')
        entry.config(fg='grey')

entry = tk.Entry(bdayentry_frame, fg='gray',bg="#D9D9D9",borderwidth=0,font=('helvica',12),width=10)
entry.insert(0, 'mm/dd/yyyy')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack()

#gender label
gender_frame = tk.Frame(root,height=10,width=500,bg='white',borderwidth=0)
gender_frame.place(x=800,y=260)
gender_label=tk.Label(gender_frame,text="Gender",bg='white',font=('times new roman',15,'bold'))
gender_label.pack()

#gender pic frame
gindir_frame= tk.Frame(root,height=10,width=500,bg='white',borderwidth=0)
gindir_frame.place(x=800,y=300)

# gender drop down frame
genmenu_frame= tk.Frame(root, height=10, width=500,bg='#D9D9D9',borderwidth=0)
genmenu_frame.place(x=803,y=302)
#gender menu
selected_option = tk.StringVar()
selected_option.set("Male")
options = ["Male", "Female", "Others", "Prefer Not to say"]
option_menu = tk.OptionMenu(genmenu_frame, selected_option, *options)
option_menu.configure(borderwidth=0,width=13,font=('Helvica',12),bg='#D9D9D9',highlightbackground='#D9D9D9',)
option_menu.pack()

#Gender picture para soft edges
gender_pic = Image.open ("Rental Management images/long rectangle.png")
resized = gender_pic.resize((170,35),Image.Resampling.LANCZOS)
gender_pic = ImageTk.PhotoImage(resized)
gender_label = tk.Label(gindir_frame, image=gender_pic,borderwidth=0,bg="white")
gender_label.pack(pady=(0,0))

#email label
email_frame = tk.Frame(root, bg="white")
email_frame.place(x=120,y=368)
email_label=tk.Label(email_frame,text="Email",bg='white',font=('times new roman',15,'bold'))
email_label.pack(padx=(0,280))

#email picture para soft edges
email_pic = Image.open ("Rental Management images/long rectangle.png")
resized = email_pic.resize((250,35),Image.Resampling.LANCZOS)
email_pic = ImageTk.PhotoImage(resized)
email_label = tk.Label(email_frame, image=email_pic,borderwidth=0,bg="white")
email_label.pack(pady=(15,0),padx=(0,100))

#email entry
emailentry_frame = tk.Frame(root, bg="white")
emailentry_frame.place(x=140,y=418)
email=tk.Entry(emailentry_frame,background="#D9D9D9",width=23,borderwidth=0,font=("helvica",13))
email.pack()

#contact number label
contact_frame = tk.Frame(root, bg="white")
contact_frame.place(x=460,y=368)
contact_label=tk.Label(contact_frame,text="Contact Number",bg='white',font=('times new roman',15,'bold'))
contact_label.pack(padx=(0,170))

#Contact number picture para soft edges
contact_pic = Image.open ("Rental Management images/long rectangle.png")
resized = contact_pic.resize((250,35),Image.Resampling.LANCZOS)
contact_pic = ImageTk.PhotoImage(resized)
contact_label = tk.Label(contact_frame, image=contact_pic,borderwidth=0,bg="white")
contact_label.pack(pady=(15,0),padx=(0,60))

#contact entry
contactentry_frame = tk.Frame(root, bg="white")
contactentry_frame.place(x=480,y=418)
contact=tk.Entry(contactentry_frame,background="#D9D9D9",width=20,borderwidth=0,font=("helvica",13))
contact.pack()

#Address label
address_frame = tk.Frame(root, bg="white")
address_frame.place(x=120,y=468)
address_label=tk.Label(address_frame,text="Address",bg='white',font=('times new roman',17,'bold'))
address_label.pack(padx=(0,280))

#streetlabel
street_label=tk.Label(address_frame,text="Street",bg='white',font=('times new roman',15,'bold'))
street_label.pack(padx=(0,280))

#street picture para soft edges
street_pic = Image.open ("Rental Management images/long rectangle.png")
resized = street_pic.resize((180,35),Image.Resampling.LANCZOS)
street_pic = ImageTk.PhotoImage(resized)
street_label = tk.Label(address_frame, image=street_pic,borderwidth=0,bg="white")
street_label.pack(pady=(15,0),padx=(0,159))

#street entry
streetentry_frame = tk.Frame(root, bg="white")
streetentry_frame.place(x=155,y=548)
street=tk.Entry(streetentry_frame,background="#D9D9D9",width=17,borderwidth=0,font=("helvica",13))
street.pack()



#Barangay frame
brgy_frame = tk.Frame(root, bg="white")
brgy_frame.place(x=350,y=498)

#Barangay label
brgy_label=tk.Label(brgy_frame,text="Barangay",bg='white',font=('times new roman',15,'bold'))
brgy_label.pack(padx=(0,285))

#Barangay picture para soft edges
brgy_pic = Image.open ("Rental Management images/long rectangle.png")
resized = brgy_pic.resize((180,35),Image.Resampling.LANCZOS)
brgy_pic = ImageTk.PhotoImage(resized)
brgy_label = tk.Label(brgy_frame, image=brgy_pic,borderwidth=0,bg="white")
brgy_label.pack(pady=(15,0),padx=(0,199))

#Barangay entry
brgyentry_frame = tk.Frame(root, bg="white")
brgyentry_frame.place(x=370,y=548)
brgy=tk.Entry(brgyentry_frame,background="#D9D9D9",width=17,borderwidth=0,font=("helvica",13))
brgy.pack()


#City frame
city_frame = tk.Frame(root, bg="white")
city_frame.place(x=560,y=498)

#City label
city_label=tk.Label(city_frame,text="City",bg='white',font=('times new roman',15,'bold'))
city_label.pack(padx=(0,335))

#City picture para soft edges
city_pic = Image.open ("Rental Management images/long rectangle.png")
resized = city_pic.resize((180,35),Image.Resampling.LANCZOS)
city_pic = ImageTk.PhotoImage(resized)
city_label = tk.Label(city_frame, image=city_pic,borderwidth=0,bg="white")
city_label.pack(pady=(15,0),padx=(0,199))

#city entry
cityentry_frame = tk.Frame(root, bg="white")
cityentry_frame.place(x=580,y=548)
city=tk.Entry(cityentry_frame,background="#D9D9D9",width=17,borderwidth=0,font=("helvica",13))
city.pack()

#Province frame
prov_frame = tk.Frame(root, bg="white")
prov_frame.place(x=780,y=498)

#Province label
prov_label=tk.Label(prov_frame,text="Province",bg='white',font=('times new roman',15,'bold'))
prov_label.pack(padx=(0,302))

#Province picture para soft edges
prov_pic = Image.open ("Rental Management images/long rectangle.png")
resized = prov_pic.resize((180,35),Image.Resampling.LANCZOS)
prov_pic = ImageTk.PhotoImage(resized)
prov_label = tk.Label(prov_frame, image=prov_pic,borderwidth=0,bg="white")
prov_label.pack(pady=(15,0),padx=(0,199))

#Province entry
proventry_frame = tk.Frame(root, bg="white")
proventry_frame.place(x=800,y=548)
prov=tk.Entry(proventry_frame,background="#D9D9D9",width=17,borderwidth=0,font=("helvica",13))
prov.pack()


#Zip code frame
zip_frame = tk.Frame(root, bg="white")
zip_frame.place(x=1000,y=498)

#Zip code label
zip_label=tk.Label(zip_frame,text="Zip Code",bg='white',font=('times new roman',15,'bold'))
zip_label.pack(padx=(0,240))

#Zip code picture para soft edges
zip_pic = Image.open ("Rental Management images/small rectangle.png")
resized = zip_pic.resize((100,35),Image.Resampling.LANCZOS)
zip_pic = ImageTk.PhotoImage(resized)
zip_label = tk.Label(zip_frame, image=zip_pic,borderwidth=0,bg="white")
zip_label.pack(pady=(15,0),padx=(0,220))

#Zip code  entry
zipentry_frame = tk.Frame(root, bg="white")
zipentry_frame.place(x=1030,y=548)
zip=tk.Entry(zipentry_frame,background="#D9D9D9",width=6,borderwidth=0,font=("helvica",13))
zip.pack()


#Lease Term Start date label
strt_frame = tk.Frame(root, bg="white")
strt_frame.place(x=120,y=600)
strt_label=tk.Label(strt_frame,text="Lease Term Start Date",bg='white',font=('times new roman',15,'bold'))
strt_label.pack(padx=(0,280))

#Lease Term Start Date picture para soft edges
strt_pic = Image.open ("Rental Management images/long rectangle.png")
resized = strt_pic.resize((180,35),Image.Resampling.LANCZOS)
strt_pic = ImageTk.PhotoImage(resized)
strt_label = tk.Label(strt_frame, image=strt_pic,borderwidth=0,bg="white")
strt_label.pack(pady=(15,0),padx=(0,298))

#Lease Term Start Date entry
strtentry_frame = tk.Frame(root, bg="white")
strtentry_frame.place(x=145,y=650)
strt=tk.Entry(strtentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
strt.pack()


#Lease Term End date label
end_frame = tk.Frame(root, bg="white")
end_frame.place(x=355,y=600)
end_label=tk.Label(end_frame,text="Lease Term End Date",bg='white',font=('times new roman',15,'bold'))
end_label.pack(padx=(0,280))

#Lease Term Start End picture para soft edges
end_pic = Image.open ("Rental Management images/long rectangle.png")
resized = end_pic.resize((180,35),Image.Resampling.LANCZOS)
end_pic = ImageTk.PhotoImage(resized)
end_label = tk.Label(end_frame, image=end_pic,borderwidth=0,bg="white")
end_label.pack(pady=(15,0),padx=(0,298))

#Lease Term Start End entry
endentry_frame = tk.Frame(root, bg="white")
endentry_frame.place(x=375,y=650)
end=tk.Entry(endentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
end.pack()


#Downpayment label
down_frame = tk.Frame(root, bg="white")
down_frame.place(x=585,y=600)
down_label=tk.Label(down_frame,text="Down Payment",bg='white',font=('times new roman',15,'bold'))
down_label.pack(padx=(0,340))

#Downpayment picture para soft edges
down_pic = Image.open ("Rental Management images/long rectangle.png")
resized = down_pic.resize((180,35),Image.Resampling.LANCZOS)
down_pic = ImageTk.PhotoImage(resized)
down_label = tk.Label(down_frame, image=down_pic,borderwidth=0,bg="white")
down_label.pack(pady=(15,0),padx=(0,298))

#Downpayment entry
downentry_frame = tk.Frame(root, bg="white")
downentry_frame.place(x=610,y=650)
down=tk.Entry(downentry_frame,background="#D9D9D9",width=10,borderwidth=0,font=("helvica",15))
down.pack()

#Add A tenant frame
add_frame = tk.Frame(root, bg="white")
add_frame.place(x=1000,y=658)

add = tk.Button(add_frame,text="Add a tenant",font=("times new roman",14,"bold"), pady= 5, padx= 15,background= "#2C6FBC",width=10)
add.pack()



root.mainloop()