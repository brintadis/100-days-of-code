from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def miles_to_km():
    result.config(text=round(int(input.get()) * 1.6))


input = Entry()
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result = Label(text=0)
result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()