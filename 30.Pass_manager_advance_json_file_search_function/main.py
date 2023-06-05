from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_random = [random.choice(letters) for _ in range(random.randint(8, 10))]
    number_random = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbol_random = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = letter_random + number_random + symbol_random
    random.shuffle(password_list)
    password_final = "".join(password_list)
    password.insert(0,password_final)
    pyperclip.copy(password_final)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    new_data = {
        website.get(): {
            "email" : email.get(),
            "password" : password.get()
        }
    }
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Error", message="Cannot leave fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # read file
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file)
        else:
            # update file
            data.update(new_data)

            with open("data.json", "w") as file:
                # write file
                json.dump(data, file, indent=4)
        finally:
                website.delete(0,END)
                password.delete(0,END)

def find_password():
    try:
        with open("data.json","r") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        try:
            website_data = data_dict[website.get()]
        except KeyError:
            messagebox.showinfo(title="Error", message=f"No details about {website.get()} found ")
        else:
            messagebox.showinfo(title=website.get(), message=f"Email: {website_data['email']}\n\nPassword: {website_data['password']} ")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

logo = Canvas(width=200, height=200)
img = PhotoImage(file ="logo.png")
logo.create_image(100,100, image= img)
logo.grid(column=2,row=1)

website_text = Label(text="Website:")
website_text.grid(column=1,row=2)

website = Entry(width=33)
website.focus()
website.grid(column=2,row=2)

email_text = Label(text="Email/Username:")
email_text.grid(column=1,row=3)

email = Entry(width=49)
email.insert(0, "siddhant.autofill@gmail.com")
email.grid(column=2,row=3, columnspan=2)

password_text = Label(text="Password:")
password_text.grid(column=1,row=4)

password = Entry(width=33)
password.grid(column=2,row=4)

generate = Button(text="Generate Button", command=generate_password)
generate.grid(column=3,row=4)

add_button = Button(text="Add", width=42, command=add_data)
add_button.grid(column=2,row=5, columnspan=2)

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=3,row=2)
window.mainloop()
