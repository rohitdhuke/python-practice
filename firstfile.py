import tkinter as tk
from logging import disable

window = tk.Tk()
def disable_window():
    window.attributes("-disabled", True)
window.title("My First App")
window.geometry("600x200")
label = tk.Label(window, text="Hello, World!")
label.pack()
button = tk.Button(window, text="Click Me")
button.pack()
button2 = tk.Button(window, text="Disable Window", command=disable_window)
button2.pack()
button3 = tk.Button(window, text="Close", command=window.destroy)
button3.pack()
window.mainloop()