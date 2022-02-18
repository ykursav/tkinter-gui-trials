# place is for putting the element in exact location of coordinate system

import tkinter as tk

root = tk.Tk()

frm_main = tk.Frame(master=root, width=200, height=200)
frm_main.pack()

btn_test = tk.Button(master=frm_main, text="Test_Button", bg="yellow")
btn_test.place(x=0, y=0)


btn_other_loc = tk.Button(master=frm_main, text="Other_Loc")
btn_other_loc.place(x=100, y=100)


root.mainloop()
