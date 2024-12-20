from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def genarate_password():
    letrasmai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letrasmin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ["!","#","$","%","&","(",")","*","+"]
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    min = [choice(letrasmin) for _ in range(randint(4,8))]
    mai = [choice(letrasmai) for _ in range(randint(2,4))]
    sim = [choice(simbolos) for _ in range(randint(1,3))]
    num = [choice(numeros) for _ in range(randint(1,3))]

    v_senha = min + mai + sim + num
    shuffle(v_senha)
    senha = "".join(v_senha)
    password_entry.insert(0,senha)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_add():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You can't leave fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                try:
                    data = json.load(data_file)
                except json.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            data = {}
        data.update(new_data)

        with open("data.json", mode="w") as data_file:
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()
        messagebox.showinfo(title="Success", message="Password saved successfully.")


def search_website():
    find = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
        if find in data:
            email = data[find]["email"]
            password = data[find]["password"]
            messagebox.showinfo(title=find, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Website not found.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()  #Faz com que ao inicializar a app, ele ja esteja selecionado para digitar

website_button = Button(text="Search",width=15,command=search_website)
website_button.grid(row=1,column=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2,column=0)

user_entry = Entry(width=40)
user_entry.grid(row=2,column=1,columnspan=2)




password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,columnspan=1)

generate_button = Button(text="Generate Password",command=genarate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=34, command=button_add)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()