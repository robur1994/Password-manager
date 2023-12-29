from tkinter import *
import pandas as pd
from data import number, symbol, alfa
import random
from tkinter import messagebox
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def convert_pass():
    list_pass = []
    write_box_pass.delete(0, 'end')
    for i in range(3):
        list_pass.append(str(random.choice(alfa)))
        list_pass.append(str(random.choice(symbol)))
        list_pass.append(str(random.choice(number)))
        random.shuffle(list_pass)
    list_pass = ''.join(list_pass)
    pyperclip.copy(list_pass)
    write_box_pass.insert(0, string=list_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_site = write_box_web.get()
    emile = write_box_emile.get()
    password = write_box_pass.get()

    if len(emile) > 0 and len(password) > 0 and len(web_site) > 0:
        is_ok = messagebox.askokcancel(title=web_site,
                                       message=f"You entered this details:\n emile: {emile}\n password:"
                                               f" {password} \n Its ok to save? ")
        if is_ok:
            with open("password_file.txt", "a") as file:
                file.write(f"{web_site} | {emile} | {password} \n")
            write_box_web.delete(0, 'end')
            write_box_pass.delete(0, 'end')
            write_box_pass.delete(0, 'end')
    else:
        messagebox.showinfo(title="Empty info", message="Please don`t let any field`s empty")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0,)

#writed text program label
web_lab = Label(text="Website:")
web_lab.grid(column=0, row=2)
emile_lab = Label(text="Emile/username: ")
emile_lab.grid(column=0, row=3)
password_lab = Label(text="Password: ")
password_lab.grid(column=0, row=4)

#button widghet
gen_pass_button = Button(text="Gen pass", width=8, font=("Arial",7,"normal"), command=convert_pass)
gen_pass_button.grid(column=2, row=4,)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=2)

#entry widghet
write_box_web = Entry(width=35)
write_box_web.focus()
write_box_web.grid(column=1, row=2, columnspan=2)
write_box_emile = Entry(width=35)
write_box_emile.insert(END, string="robur1994@google.com")
write_box_emile.grid(column=1, row=3, columnspan=2)
emile_get = write_box_emile.get()
write_box_pass = Entry(width=26)
write_box_pass.grid(column=1, row=4)
pass_get = write_box_pass.get()






window.mainloop()