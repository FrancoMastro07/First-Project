from tkinter import *
from tkinter import messagebox
import sqlite3

#----------------------database-code----------------------------------------------#

def connection():	

	connection=sqlite3.connect("CRUD")
	slider=connection.cursor()
	
	try:

		slider.execute(""" 

		CREATE TABLE USERSDATA (

			ID INTEGER PRIMARY KEY AUTOINCREMENT, 
			NAME VARCHAR(50),
			PASSWORD VARCHAR(50),
			SURNAME VARCHAR(10),
			ADDRESS VARCHAR(50),
			COMMENTS VARCHAR(100))

			""")

		messagebox.showinfo("CRUD", "The database was succesfully created")


	except:
	
		messagebox.showwarning("CRUD", "A database has already been created")	

	connection.close()

	
def quit():

	quit_value=messagebox.askokcancel("Quit", "Do you want to quit?")

	if quit_value==True:

		root.destroy()

def delete_fields():

	if True:

		Id.set("")
		Name.set("")
		Password.set("") 
		Surname.set("")
		Address.set("")
		comments_text.delete("1.0", END)

#--------------root----------------------------------------------#

root=Tk()

#--------interface-----------------------------------------------#

root.title("CRUD")
root.resizable(0,0)
root.iconbitmap("database.ico")
root.geometry("300x600")

bar_menu=Menu(root)
root.config(menu=bar_menu, width=300, height=300)

#--------------menu----------------------------------------------#

menu_BBDD=Menu(bar_menu, tearoff=0)
menu_BBDD.add_command(label="Connect", command=connection)
menu_BBDD.add_command(label="Quit", command=quit)
bar_menu.add_cascade(label="BBDD", menu=menu_BBDD)

menu_delete=Menu(bar_menu, tearoff=0)
menu_delete.add_command(label="Delete fields", command=delete_fields)
bar_menu.add_cascade(label="Delete", menu=menu_delete)

menu_CRUD=Menu(bar_menu, tearoff=0)
menu_CRUD.add_command(label="Create")
menu_CRUD.add_command(label="Read")
menu_CRUD.add_command(label="Update")
menu_CRUD.add_command(label="Delete")
bar_menu.add_cascade(label="CRUD", menu=menu_CRUD)

menu_help=Menu(bar_menu, tearoff=0)
menu_help.add_command(label="License")
menu_help.add_command(label="????")
bar_menu.add_cascade(label="Help", menu=menu_help)

#-------frame------------------------------------------------------#

myframe=Frame(root, width=1200, height=600)
myframe.pack()
myframe.config()

#--------entry-and-scrollbar------------------------------------------#

Id=StringVar()
id_text=Entry(myframe, textvariable=Id)
id_text.grid(row=0, column=1)
id_text.config(bg="#A9EBBB", justify="center")

Name=StringVar()
name_text=Entry(myframe, textvariable=Name)
name_text.grid(row=1, column=1)
name_text.config(bg="#A9EBBB", justify="center")

Password=StringVar()
password_text=Entry(myframe, textvariable=Password)
password_text.grid(row=2, column=1)
password_text.config(bg="#A9EBBB", justify="center", show="*")

Surname=StringVar()
surname_text=Entry(myframe, textvariable=Surname)
surname_text.grid(row=3, column=1)
surname_text.config(bg="#A9EBBB", justify="center")

Address=StringVar()
address_text=Entry(myframe, textvariable=Address)
address_text.grid(row=4, column=1)
address_text.config(bg="#A9EBBB", justify="center")

comments_text=Text(myframe, width=16, height=5)
comments_text.grid(row=5, column=1)
comments_text.config(bg="#A9EBBB")

scrollvert=Scrollbar(myframe, command=comments_text.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")
comments_text.config(yscrollcommand=scrollvert.set)

#----------label--------------------------------------------------------#

id_label=Label(myframe, text="Id: ")
id_label.grid(row=0, column=0, sticky="s", padx=30, pady=30)

name_label=Label(myframe, text="Name: ")
name_label.grid(row=1, column=0, sticky="s", padx=30 , pady=30)

password_label=Label(myframe, text="Password: ")
password_label.grid(row=2, column=0, sticky="s", padx=30 , pady=30)

surname_label=Label(myframe, text="Surname: ")
surname_label.grid(row=3, column=0, sticky="s", padx= 30 , pady=30)

address_label=Label(myframe, text="Address: ")
address_label.grid(row=4, column=0, sticky="s", padx=30 , pady=30)

comments_label=Label(myframe, text="Comments: ")
comments_label.grid(row=5, column=0, sticky="s", padx=30 , pady=30)

#------------button------------------------------------------------------#

button_create=Button(root, text="Create")
button_create.pack(side="left", padx=15, pady=15)

button_read=Button(root, text="Read")
button_read.pack(side="left", padx=15, pady=15)

button_delete=Button(root, text="Delete")
button_delete.pack(side="right", padx=15, pady=15)

button_update=Button(root, text="Update")
button_update.pack(side="right", padx=15, pady=15)

#----------------end---------------------------------------------------------------#

root.mainloop()



