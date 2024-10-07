import tkinter as tk
from PIL import ImageTk, Image
from time import strftime

root = tk.Tk()
root.title("Greetings willage people!!!!")
root.geometry("1000x600")
root.resizable(True, True)
root.attributes("-alpha", 0.95)

photo = ImageTk.PhotoImage(Image.open("Halle_small.jpg"))
root.iconphoto(False, photo)

greetings = tk.Label(root,
                     text="Welcome to the Tkinter tutorial!",
                     font=("Arial", 25))

about_tkinter = tk.Label(foreground="black", 
                         background="cyan",
                         bd=14, #bd = border width
                         font=("Times New Roman", 20))

about_tkinter.config(text = "Standard Python interface to the Tk GUI toolkit shipped with Python!")

def time():
    string = strftime("%H:%M:%S %p")
    time_label.config(text = string)
    time_label.after(1000, time)
    
time_label = tk.Label(root, font=("calibri", 30, "bold"))
image_label = tk.Label(root , image = photo, text = "Market Analysis", compound = "top")

greetings.pack()
about_tkinter.pack()
time_label.pack(anchor = "c") #anchor = "c" centers the text both horizontally as well as vertically
time()
image_label.pack()

root.mainloop()


