import tkinter as tk

window = tk.Tk()


def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


def handle_click(event):
    print("Button was clicked.")


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

btn = tk.Button(text="Event test")

btn.bind("<Button-1>", handle_click)
btn.pack()

window.mainloop()
