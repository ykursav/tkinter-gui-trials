import tkinter as tk

root = tk.Tk()

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for k in range(4):
        frm = tk.Frame(master=root, relief=tk.GROOVE, borderwidth=2, padx=10, pady=10)
        frm.grid(row=i, column=k, padx=10, pady=10)
        label = tk.Label(master=frm, text=f"row {i}\n col {k}")
        label.pack(fill=tk.BOTH, expand=True)

root.mainloop()
