import tkinter as tk

window_frames = tk.Tk()

BORDER_TYPES = {
    "sunken": tk.SUNKEN,
    "no_border": tk.FLAT,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for border_name, border_type in BORDER_TYPES.items():
    frame_loop = tk.Frame(
        master=window_frames,
        relief=border_type,
        borderwidth=4,
        padx=10,
        pady=10,
        bg="white",
    )
    frame_loop.pack(side=tk.RIGHT)
    button = tk.Button(
        master=frame_loop,
        text=border_name,
        activebackground="yellow",
        background="red",
        padx=10,
        pady=10,
    )
    button.pack(side=tk.TOP)


window_frames.mainloop()
