import tkinter as tk
from tkinter import filedialog
import os

# Function to open a file and perform operations on it
def open_and_clean_file():
    # Open a file dialog to select the file
    file_path = filedialog.askopenfilename(title="Select a File")
    
    # Perform some operations on the file (in this case, we'll simply read and write back)
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
        
        # Here, you can perform any operations on 'data'
        cleaned_data = data.strip()  # Example: removing any leading/trailing spaces
        
        # Save the cleaned file with a "_cleaned" suffix
        directory, file_name = os.path.split(file_path)
        name, ext = os.path.splitext(file_name)
        cleaned_file_path = os.path.join(directory, f"{name}_cleaned{ext}")
        
        with open(cleaned_file_path, 'w') as cleaned_file:
            cleaned_file.write(cleaned_data)
        
        print(f"File cleaned and saved at: {cleaned_file_path}")

# Setup tkinter window
root = tk.Tk()
root.title("File Cleaner")
root.geometry("300x100")

# Button to trigger the file open and clean process
open_file_btn = tk.Button(root, text="Open and Clean File", command=open_and_clean_file)
open_file_btn.pack(pady=20)

# Run the application
root.mainloop()