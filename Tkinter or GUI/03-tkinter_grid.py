from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)



def button_clicked():

    input_val = input.get()
    my_label.config(text=input_val)


#Label

my_label = Label(text="That is my Label.", font=("Arial", 20, "bold"))
my_label.grid(column=5, row=0)

my_label.config(text="new text.")



# Button

button = Button(text="Click", command=button_clicked)
button.grid(row=1, column=7)



# Entry

input = Entry(width=20)
input.grid(row=1, column=1)






window.mainloop()