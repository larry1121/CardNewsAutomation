import tkinter as tk
from tkinter import ttk

# Import your existing functions
from main import generate_images, confirm_and_upload

def on_generate_images_click():
    url = url_entry.get()
    folder_name = generate_images(url)
    folder_name_var.set(f"Folder name: {folder_name}")

def on_confirm_and_upload_click():
    folder_name = folder_name_var.get().replace("Folder name: ", "")
    confirm_and_upload(folder_name)

# Create the Tkinter window
root = tk.Tk()
root.title("My GUI App")

# Create and place labels and buttons
url_label = ttk.Label(root, text="Blog URL:")
url_label.grid(column=0, row=0)

url_entry = ttk.Entry(root)
url_entry.grid(column=1, row=0)

generate_images_button = ttk.Button(root, text="Generate Images", command=on_generate_images_click)
generate_images_button.grid(column=2, row=0)

folder_name_var = tk.StringVar()
folder_name_label = ttk.Label(root, textvariable=folder_name_var)
folder_name_label.grid(column=1, row=1)

confirm_and_upload_button = ttk.Button(root, text="Confirm and Upload", command=on_confirm_and_upload_click)
confirm_and_upload_button.grid(column=2, row=1)

# Start the Tkinter event loop
root.mainloop()
