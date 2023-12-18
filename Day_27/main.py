import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I am label", font=("Times New Roman", 35, "bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="New Text")



def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got Clicked!")


button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=2, row=2)

new_botton = tkinter.Button(text="Click Me")
new_botton.grid(column=3, row=1)

text_input = tkinter.Entry()
text_input.grid(column=4, row=3)


window.mainloop()
