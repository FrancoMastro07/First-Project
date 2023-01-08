from tkinter import *

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
menu_BBDD.add_command(label="Connect")
menu_BBDD.add_command(label="Quit")
bar_menu.add_cascade(label="BBDD", menu=menu_BBDD)

menu_delete=Menu(bar_menu, tearoff=0)
menu_delete.add_command(label="Delete fields")
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

miframe=Frame(root, width=1200, height=600)
miframe.pack()
miframe.config()

#--------entry-and-scrollbar------------------------------------------#

id_text=Entry(miframe)
id_text.grid(row=0, column=1)
id_text.config(bg="#A9EBBB", justify="center")

name_text=Entry(miframe)
name_text.grid(row=1, column=1)
name_text.config(bg="#A9EBBB", justify="center")

password_text=Entry(miframe)
password_text.grid(row=2, column=1)
password_text.config(bg="#A9EBBB", justify="center", show="*")

surname_text=Entry(miframe)
surname_text.grid(row=3, column=1)
surname_text.config(bg="#A9EBBB", justify="center")

address_text=Entry(miframe)
address_text.grid(row=4, column=1)
address_text.config(bg="#A9EBBB", justify="center")

comments_text=Text(miframe, width=16, height=5)
comments_text.grid(row=5, column=1)
comments_text.config(bg="#A9EBBB")

scrollvert=Scrollbar(miframe, command=comments_text.yview)
scrollvert.grid(row=5, column=2, sticky="nsew")
comments_text.config(yscrollcommand=scrollvert.set)

#----------label--------------------------------------------------------#

id_label=Label(miframe, text="Id: ")
id_label.grid(row=0, column=0, sticky="s", padx=30, pady=30)

name_label=Label(miframe, text="Name: ")
name_label.grid(row=1, column=0, sticky="s", padx=30 , pady=30)

password_label=Label(miframe, text="Password: ")
password_label.grid(row=2, column=0, sticky="s", padx=30 , pady=30)

surname_label=Label(miframe, text="Surname: ")
surname_label.grid(row=3, column=0, sticky="s", padx= 30 , pady=30)

address_label=Label(miframe, text="Address: ")
address_label.grid(row=4, column=0, sticky="s", padx=30 , pady=30)

comments_label=Label(miframe, text="Comments: ")
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

#----end---------------------------------------------------------------#

root.mainloop()