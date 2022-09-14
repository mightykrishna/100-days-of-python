from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_label_entry.get()
    email=email_entry.get()
    passwordget=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":passwordget,
        }
    }

    if len(website)==0 or len(passwordget)==0:
        messagebox.showinfo(title="OOPS",message="please make sure you haven't left any fields empty.")
    else:
        try:

            with open("data.json","r") as data_file:
                #json.dump(new_data,data_file,indent=4)
                #reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                data.update(new_data)

                json.dump(data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_label_entry.delete(0,END)
            password_entry.delete(0,END)


#-------------------------------FIND PASSWORD-------------------------
def find_password():
    website=website_label_entry.get()
    try:

        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="NO Data FIle Found")
    else:
            if website in data:
                emial=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {emial}\npassword: {password}\n")
            else:
                messagebox.showinfo(title="ERror",message="fNO details for {website} exists")
# --    -------------------------- UI SETUP -------------------------------
#  #

window=Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

website_label=Label(text="Website")
website_label.grid(column=0,row=1)

email_username=Label(text="Email/username")
email_username.grid(column=0,row=2)

password=Label(text="Password")
password.grid(column=0,row=3)

#ENTRIES
website_label_entry=Entry(width=21)
website_label_entry.grid(row=1,column=1,columnspan=2)
website_label_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"saurabhpandeyjmp@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#BUTTONS
generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)
add_button=Button(text="ADD",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button=Button(text="Search",command=find_password)
search_button.grid(row=1,column=2,)
canvas=Canvas(height=200,width=200)
logo=PhotoImage(file="logo.jpeg")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

window.mainloop()
