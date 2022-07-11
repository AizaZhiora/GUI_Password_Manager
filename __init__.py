from tkinter import *
import string
import random
from tkinter import messagebox
import pyperclip


def generate():
    alpha = list(string.ascii_letters)
    number = list(string.digits)
    simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    chars = alpha + number + simbol
    password_input.delete(0, END)
    list_pass = [random.choice(chars) for n in range(15)]
    password_out = ''.join(list_pass)
    print(password_out)
    password_input.insert(0, password_out)
    pyperclip.copy(password_out)


def saver():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if website == "" or password == "":
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered:\nEmail: {email} \n Password: {password}'
                                               f'\nIs it ok to save? ')
        if is_ok:
            with open('file/password.txt', 'a') as file:
                file.write(f'\n{website} | {email} | {password}')
                website_input.delete(0, END)
                password_input.delete(0, END)


window = Tk()
button = Button()
label = Label()

window.title("Password Manager")
window.config(padx=20, pady=20)
window.iconbitmap('logo.ico')

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text='Website: ', font='Arial')
website_label.grid(column=0, row=1)
email_user_label = Label(text='Email/Username: ', font='Arial')
email_user_label.grid(column=0, row=2)
password_label = Label(text='Password: ', font='Arial')
password_label.grid(column=0, row=3, columnspan=1)

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
email_user_input = Entry(width=45)
email_user_input.insert(0, 'example@mail.com')  # If you want to set a default change the email
email_user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=27)
password_input.grid(column=1, row=3)

button_pass = Button(text='Generate Pass', width=14, border=0.5, command=generate)
button_pass.grid(column=2, row=3)

button_add = Button(text='Add', font='Arial', width=10, border=0.5, command=saver)
button_add.grid(column=1, row=4)

window.mainloop()
