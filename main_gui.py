import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar
from PIL import Image, ImageTk
import os
import subprocess
import logging
import config

# Import your existing functions
from main import generate_images, confirm_and_display

from tkinter import filedialog





def on_open_folder_click():
    folder_name = folder_name_var.get().replace("Folder name: ", "")
    if os.path.exists(folder_name):
        subprocess.run(['open', folder_name] if os.name == 'posix' else ['explorer', folder_name])
    else:
        log_text_handler(f"Folder {folder_name} does not exist.")

# Function to display log messages in Tkinter Text widget
def log_text_handler(msg):
    log_text.insert(tk.END, msg + '\n')
    log_text.see(tk.END)

# Custom logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().addHandler(logging.StreamHandler(stream=type('TkinterLogStream', (object,), {'write': log_text_handler})))

import traceback

def on_generate_images_click():
    try:
        url = url_entry.get()
        folder_name = generate_images(url)
        folder_name_var.set(f"Folder name: {folder_name}")
    except OSError as e:
        log_text_handler(f"파일 저장 오류: {e} ,cwd : {os.getcwd()}")
    except Exception as e:
        tb = traceback.format_exc()  # 에러의 트레이스백을 문자열로 가져옵니다.
        logging.error(f"Image generation error: {e}\n{tb}")  # 에러와 트레이스백을 로깅합니다.
        log_text_handler(f"Error during image generation: {e}\n{tb}")  # 사용자 인터페이스에도 표시합니다.

def on_confirm_and_display_click():
    try:
        folder_name = folder_name_var.get().replace("Folder name: ", "")
        photos, caption = confirm_and_display(folder_name)

        # Clear existing widgets in the canvas
        for widget in canvas_frame.winfo_children():
            widget.destroy()

        y_position = 0
        for photo_path in photos:
            img = Image.open(photo_path)
            img = img.resize((200, 200), Image.ANTIALIAS)  # Resize for display
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(canvas_frame, image=img)
            img_label.image = img
            img_label.grid(row=0, column=y_position)
            y_position += 1

        # Display caption
        suggested_caption_var.set(f"Suggested caption: {caption}")
    except Exception as e:
        tb = traceback.format_exc()
        logging.error(f"Confirmation and display error: {e}\n{tb}")
        log_text_handler(f"Error during confirmation and display: {e}\n{tb}")


# Create the Tkinter window
root = tk.Tk()
# 아이콘 변경
root.iconbitmap('bugdict_icon.ico')
root.title("CardNewsAutomation")

# Configure the grid to expand as window resizes
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

main_frame = tk.Frame(root)
main_frame.grid(sticky='news')

# Configure the main frame to expand
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Create and place labels, buttons, and Text widget inside a frame
control_frame = tk.Frame(main_frame)
control_frame.grid(row=0, column=0, sticky='nw')

url_label = ttk.Label(control_frame, text="Blog URL:")
url_label.grid(row=0, column=0)

url_entry = ttk.Entry(control_frame)
url_entry.grid(row=0, column=1)

generate_images_button = ttk.Button(control_frame, text="Generate Images", command=on_generate_images_click)
generate_images_button.grid(row=0, column=2)

folder_name_var = tk.StringVar()
folder_name_label = ttk.Label(control_frame, textvariable=folder_name_var)
folder_name_label.grid(row=1, column=0)

confirm_and_display_button = ttk.Button(control_frame, text="Confirm and Display", command=on_confirm_and_display_click)
confirm_and_display_button.grid(row=1, column=1)

open_folder_button = ttk.Button(control_frame, text="Open Folder", command=on_open_folder_click)
open_folder_button.grid(row=1, column=2)

# Scrollable Canvas for images
canvas = Canvas(main_frame)
canvas.grid(row=1, column=0, sticky='nsew')

scrollbar = Scrollbar(main_frame, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.grid(row=2, column=0, sticky='ew')

canvas_frame = tk.Frame(canvas)
canvas_frame.grid(row=0, column=0, sticky='nsew')

canvas.create_window((0, 0), window=canvas_frame, anchor='nw')
canvas_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.configure(xscrollcommand=scrollbar.set)

#save dir
def ask_directory():
    """ 사용자가 디렉토리를 선택할 수 있는 대화상자를 엽니다. """
    return filedialog.askdirectory()
def set_save_directory():
    """ 사용자가 선택한 디렉토리를 저장합니다. """
    directory = ask_directory()
    if directory:
        save_directory.set(directory)
        config.set_save_path(directory)
        
        folder_name_var.set(f"Folder name: {directory}")
        log_text_handler(f"Save directory set to: {directory}")

choose_dir_button = ttk.Button(control_frame, text="Choose Save Directory", command=set_save_directory)
choose_dir_button.grid(row=1, column=3)
save_directory = tk.StringVar()





# Additional UI elements
suggested_caption_var = tk.StringVar()
suggested_caption_label = ttk.Label(main_frame, textvariable=suggested_caption_var)
suggested_caption_label.grid(row=3, column=0)

log_text = tk.Text(main_frame, wrap=tk.WORD, width=50, height=10)
log_text.grid(row=4, column=0, sticky='nsew')

# Start the Tkinter event loop
root.mainloop()