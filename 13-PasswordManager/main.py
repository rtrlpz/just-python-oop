from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    new_data = {website: {
        'email': email,
        'password': password,
    }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Warning!', message="Don't leave any fields empty.")

    else:
        try:
            with open('passwords.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open('passwords.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open('passwords.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find the Data ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('passwords.json') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No password.json File Found')

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                       f'Password: {password}')

        else:
            messagebox.showinfo(title='Error', message=f'No data for {website}, exists.')


# ---------------------------- UI SETUP ------------------------------- #
# 1. Window Set Up:
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# 2. Canvas Set Up:
canvas = Canvas(height=300, width=300)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(150, 150, image=logo_image)
canvas.grid(row=0, column=1)

# 3. Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# 4. Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, pady=10)
email_username_entry.insert(END, 'Leandro.rtrlpz@gmail.com')

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2, pady=10)

# 5. Buttons
generate_password_button = Button(text='Generate Password', width=29, command=generate_password)
generate_password_button.grid(row=4, column=1, pady=10)

add_button = Button(text='Add', width=29, command=save)
add_button.grid(row=5, column=1, columnspan=3, pady=10)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=6, column=1, pady=10)

window.mainloop()
