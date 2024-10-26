from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Warning", message="You do not empty any fields!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email : {email} \nPassword : {password} \nIs it OK to Save?")

        if is_ok:
            with open("/home/sumon/Documents/Python/Tkinter or GUI/Password Manager App/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager.")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="/home/sumon/Documents/Python/Tkinter or GUI/Password Manager App/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website : ")
web_label.grid(row=1, column=0)

web_entry = Entry(width=45)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Username/Email : ")
email_label.grid(row=2, column=0)

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sumon@gmail.com")


pass_label = Label(text="Password : ")
pass_label.grid(row=3, column=0)

pass_entry = Entry(width=25)
pass_entry.grid(row=3, column=1)

pass_genarate_button = Button(text="Genarate Password", command=generate_password)
pass_genarate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()