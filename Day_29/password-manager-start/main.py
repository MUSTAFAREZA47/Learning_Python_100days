from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    password_letter = [random.choice(letters) for char in range(0, nr_letters)]
    # for char in range(0, nr_letters):
    #     password_char = random.choice(letters)
    #     password_list.append(password_char)

    password_symbols = [random.choice(symbols) for sym in range(0, nr_symbols)]
    # for sym in range(0, nr_symbols):
    #     password_sym = random.choice(symbols)
    #     password_list.append(password_sym)

    password_number = [random.choice(numbers) for num in range(0, nr_numbers)]
    # for num in range(0, nr_numbers):
    #     password_num = random.choice(numbers)
    #     password_list.append(password_num)

    password_list = password_letter + password_number + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_text.insert(0, password)
    # password_text.delete(0, END)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website_name = website_text.get()
    user_email = user_text.get()
    user_password = password_text.get()

    if len(website_name) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Warning", message="Please fill the entries.")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                       message=f"These are the details entered: \nEmail: {user_email} \nPassword: "
                                               f"{user_password} \nIs it ok to save?")

        if is_ok:
            with open("../Day_29/password-manager-start/data.txt", "a") as data_file:
                data_file.write(f"{website_name} | {user_email} | {user_password} \n")
                website_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="../Day_29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username: ")
user_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entry
website_text = Entry(width=52)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

user_text = Entry(width=52)
user_text.grid(row=2, column=1, columnspan=2)
user_text.insert(0, "ahmed@gmail.com")

password_text = Entry(width=33)
password_text.grid(row=3, column=1)

# Button
generate_pass_button = Button(text="Generate Password", command=password_generator)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

canvas.mainloop()
