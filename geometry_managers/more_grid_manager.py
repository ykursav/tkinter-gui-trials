import tkinter as tk

root = tk.Tk()
root.columnconfigure(0, minsize=200)
root.rowconfigure([0, 1], minsize=150)

# "n" or "N" to align to the top-center part of the cell
# "e" or "E" to align to the right-center side of the cell
# "s" or "S" to align to the bottom-center part of the cell
# "w" or "W" to align to the left-center side of the cell
lbl_001 = tk.Label(text="A")
lbl_001.grid(row=0, column=0, sticky="ne")

lbl_002 = tk.Label(text="B")
lbl_002.grid(row=1, column=0, sticky="nw")


root.mainloop()
