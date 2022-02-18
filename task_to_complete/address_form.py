import tkinter as tk

lbl_fields = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]

root = tk.Tk()

counter = 0
frm_field = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
frm_field.pack(fill=tk.BOTH, expand=True)
for lbl_field in lbl_fields:
    lbl_create = tk.Label(master=frm_field, text=lbl_field)
    ent_field = tk.Entry(master=frm_field, width=80)
    lbl_create.grid(row=counter, column=0, sticky="e")
    ent_field.grid(row=counter, column=1)
    counter += 1


frm_btns = tk.Frame()
frm_btns.pack(fill=tk.X, expand=True, ipadx=5, ipady=5)
btn_submit = tk.Button(master=frm_btns, text="Submit")
btn_submit.pack(side=tk.RIGHT, ipadx=10)

btn_clear = tk.Button(master=frm_btns, text="Clear")
btn_clear.pack(side=tk.RIGHT, padx=10, ipadx=10)


root.mainloop()
