import tkinter as tk

root = tk.Tk()

# stacks under each other by order
frm_biggest = tk.Frame(master=root, width=200, height=200, background="green")
frm_biggest.pack()

frm_mid = tk.Frame(master=root, width=100, height=100, background="aquamarine")
frm_mid.pack()

frm_small = tk.Frame(master=root, width=50, height=50, bg="coral")
frm_small.pack()


root.mainloop()
