from tkinter import *


def convert():
    kilometer = 1.60934 * float(miles.get())
    converted["text"] = round(kilometer)

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=300, height=100)
window.config(padx=15, pady=15)

# Entry
miles = Entry()
miles.grid(column=1, row=0)
miles.config(width=20)

# Label
miles_text = Label(text="  Miles")
miles_text.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0,row=1)

converted = Label(text="0")
converted.grid(column=1,row=1)

kilo_text = Label(text="KM")
kilo_text.grid(column=2,row=1)

button = Button(text="Convert", command=convert)
button.grid(column=1,row=2)

window.mainloop()
