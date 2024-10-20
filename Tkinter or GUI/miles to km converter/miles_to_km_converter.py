
from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_result.config(text=str(km))


window = Tk()
window.title("ML to KM converter.")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=350)


miles_input = Entry(width=15)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="Is Equal To ")
equal_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)








window.mainloop()