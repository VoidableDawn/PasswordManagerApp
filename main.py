import json
from tkinter import *
from tkinter import messagebox

import pyperclip

import password_manager


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    password_entry.insert(0, password_manager.generate_password())
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_entry.get().title()
    username = email_entry.get()
    password = password_entry.get()

    if len(website) > 0 and len(username) > 0 and len(password) > 0:

        okay_to_save = messagebox.askokcancel(title = website, message = f"These are the details you entered for "
                                                                         f"{website}:\n\n"
                                                                         f"Email: {username}\nPassword: {password}"
                                                                         f"\n\nis it okay to save?")
        if okay_to_save:
            details_dict = {
                website: {
                    "username": username,
                    "password": password
                }
            }
            try:
                with open(file = "data.json", mode = "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file = "data.json", mode = "w") as data_file:
                    json.dump(details_dict, data_file, indent = 4)
            else:
                data.update(details_dict)
                with open(file = "data.json", mode = 'w') as data_file:
                    json.dump(data, data_file, indent = 4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
                messagebox.showinfo(title = "Success", message = "Details saved successfully!")

    else:
        messagebox.showerror(title = "Entry error", message = "You cannot leave any fields empty!")


# ---------------------------- FIND DETAILS ------------------------------- #

def find_password():
    website = website_entry.get().title()
    if len(website) < 1:
        messagebox.showwarning(title = "Warning", message = "Website field is empty!")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title = "Error", message = "Your database is empty!\n"
                                                              "Add password details first.")
        else:
            if website not in data:
                messagebox.showwarning(title = "Error",
                                       message = f"No password details for {website} in your database\n"
                                                 f"Add password for this site first.")
            else:
                messagebox.showinfo(title = f"{website} details", message = f"Username: {data[website]['username']}\n"
                                                                            f"Password: {data[website]['password']}")
                pyperclip.copy(data[website]['password'])
                messagebox.showinfo(message = "Password copied to clipboard")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 40)
window.minsize(width = 400, height = 350)

# # Canvas Widget
canvas = Canvas(width = 150, height = 150)
canvas.grid(column = 1, row = 0)
my_image = PhotoImage(file = "logo.png")
canvas.create_image(80, 60, image = my_image)

# Website Label
website_label = Label(text = "Website:")
website_label.grid(column = 0, row = 1)

# Email/Username Label
email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row = 2)

# Password Label
password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)

# Website Entry
website_entry = Entry(width = 25)
website_entry.grid(column = 1, row = 1, pady = 5, sticky = "w")
website_entry.focus()

# Email/Username Entry
email_entry = Entry(width = 45, )
email_entry.insert(0, "aadeybolar@gmail.com")
email_entry.grid(column = 1, columnspan = 2, row = 2, pady = 5, sticky = "w")

# Password Entry
password_entry = Entry(width = 25)
password_entry.grid(column = 1, row = 3, pady = 5, sticky = "w")

# Generate Password Button
generate_button = Button(text = "Generate Password", width = 15, command = generate)
generate_button.grid(row = 3, column = 2, sticky = "e")

# Add Button
add_button = Button(text = "Add", width = 38, command = save_details)
add_button.grid(column = 1, row = 4, columnspan = 2, pady = 5, sticky = "w")

# Search Button
search_button = Button(text = "Search", width = 15, command = find_password)
search_button.grid(column = 2, row = 1)

window.mainloop()
