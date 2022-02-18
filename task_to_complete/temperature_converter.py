# This is self made version

import tkinter as tk


def convert_to_celsius():
    f_value = ent_fahrenheit.get()
    c_value = (int(f_value) - 32) * 5 / 9
    lbl_celsius["text"] = f"{round(c_value,2)}°C"


root = tk.Tk()

root.title("Fahrenheit to Celsius Converter")
root.rowconfigure(0, minsize=200, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)

frm_fahrenheit = tk.Frame(master=root)
frm_fahrenheit.grid(row=0, column=0)

ent_fahrenheit = tk.Entry(master=frm_fahrenheit)
ent_fahrenheit.pack(side=tk.LEFT)

lbl_fahrenheit = tk.Label(master=frm_fahrenheit, text="°F")
lbl_fahrenheit.pack(side=tk.LEFT)

btn_convert = tk.Button(master=root, text="->", command=convert_to_celsius)
btn_convert.grid(row=0, column=1)


lbl_celsius = tk.Label(master=root, text="°C")
lbl_celsius.grid(row=0, column=2)

root.mainloop()
