from tkinter import Tk, Label, Entry, Button

window = Tk()
window.minsize(width=300, height=100)
window.title("Mile to Km Converter")
window.config(padx=15, pady=5)


def mile_to_km():
    miles = float(text_input.get())
    km = round(miles * 1.609)
    label_3.config(text=f"{km}")


text_input = Entry(width=10)
text_input.focus()
text_input.grid(column=2, row=1)

label_1 = Label(text="Mile")
label_1.grid(column=3, row=1)
label_1.config(padx=25, pady=5)

label_2 = Label(text=f"is equal to")
label_2.grid(column=1, row=2)
label_2.config(padx=25, pady=5)

label_3 = Label(text="0", font=("Arial", 10, "bold"))
label_3.grid(column=2, row=2)

label_4 = Label(text="Km")
label_4.grid(column=3, row=2)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=2, row=3)

window.mainloop(),
