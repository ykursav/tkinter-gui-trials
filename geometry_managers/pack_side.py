import tkinter as tk

root = tk.Tk()

# stacks under each other by order
# fill is responsive that is great actually
# expandable frames
frm_biggest = tk.Frame(master=root, width=200, height=200, background="green")
frm_biggest.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm_mid = tk.Frame(master=root, width=100, height=100, background="aquamarine")
frm_mid.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frm_small = tk.Frame(master=root, width=50, height=50, bg="coral")
frm_small.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


root.mainloop()
