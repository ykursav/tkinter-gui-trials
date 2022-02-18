import tkinter as tk
from random import randrange


def roll_dice():
    lbl_value["text"] = str(randrange(1, 7))


root = tk.Tk()


root.columnconfigure(0, minsize=50, weight=1)
root.rowconfigure([0, 1], minsize=50, weight=1)


btn_roll = tk.Button(master=root, text="Roll the dice", command=roll_dice)
btn_roll.grid(row=0, column=0, sticky="nsew")


lbl_value = tk.Label(master=root, text="")
lbl_value.grid(row=1, column=0, stick="nsew")

root.mainloop()
