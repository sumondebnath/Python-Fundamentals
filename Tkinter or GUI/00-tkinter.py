import tkinter

window = tkinter.Tk()

window.title("GUI")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="That is my Label.", font=("Arial", 20, "bold"))
# my_label.pack(expand=True)
# my_label.pack(side="left")
# my_label.pack(side="right")
# my_label.pack(side="top")
# my_label.pack(side="bottom")
my_label.pack()

# my_label["text"] = "new Text."
my_label.config(text="new text.")



# Button

def button_clicked():
    # print("got clicked.")
    # my_label.config(text="Button Got Clicked.")

    input_val = input.get()
    my_label.config(text=input_val)

button = tkinter.Button(text="Click", command=button_clicked)
button.pack()



# Entry

input = tkinter.Entry()
input.pack()






window.mainloop()