from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)



def button_clicked():

    input_val = input.get()
    my_label.config(text=input_val)


#Label

my_label = Label(text="That is my Label.", font=("Arial", 20, "bold"))
my_label.place(x=0, y=0)

my_label.config(text="new text.")



# Button

button = Button(text="Click", command=button_clicked)
button.place(x=120, y=50)



# Entry

input = Entry()
input.pack()






window.mainloop()