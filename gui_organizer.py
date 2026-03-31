import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import get_category

selected_folder = ""

# ==========================
# STYLES
# ==========================
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#3a86ff"
ACCENT = "#8338ec"

FONT = ("Segoe UI", 10)
TITLE_FONT = ("Segoe UI", 14, "bold")

# ==========================
# FUNCTIONS
# ==========================
def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_label.config(text=f"📁 {selected_folder}")


def preview_files():
    if not selected_folder:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    preview_text.delete(1.0, tk.END)

    for filename in os.listdir(selected_folder):
        file_path = os.path.join(selected_folder, filename)

        if os.path.isfile(file_path):
            category = get_category(filename)
            if category:
                preview_text.insert(tk.END, f"→ {filename}  ➜  {category}\n")


def organize_files():
    if not selected_folder:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    moved_count = 0

    for filename in os.listdir(selected_folder):
        file_path = os.path.join(selected_folder, filename)

        if os.path.isfile(file_path):
            category = get_category(filename)

            if category:
                target_folder = os.path.join(selected_folder, category)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))
                moved_count += 1

    messagebox.showinfo("Done", f"Organized {moved_count} files successfully!")


# ==========================
# GUI SETUP
# ==========================
root = tk.Tk()
root.title("NahstyDev's File Organizer")
root.geometry("600x450")
root.configure(bg=BG_COLOR)

# ==========================
# HEADER
# ==========================
title_label = tk.Label(
    root,
    text="NahstyDev's File Organizer",
    font=TITLE_FONT,
    bg=BG_COLOR,
    fg=ACCENT
)
title_label.pack(pady=10)

# ==========================
# SELECT BUTTON
# ==========================
select_btn = tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    bg=BTN_COLOR,
    fg="white",
    font=FONT,
    relief="flat",
    padx=10,
    pady=5
)
select_btn.pack(pady=5)

# ==========================
# FOLDER LABEL
# ==========================
folder_label = tk.Label(
    root,
    text="No folder selected",
    bg=BG_COLOR,
    fg=FG_COLOR,
    font=FONT
)
folder_label.pack(pady=5)

# ==========================
# BUTTON FRAME
# ==========================
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

preview_btn = tk.Button(
    button_frame,
    text="Preview",
    command=preview_files,
    bg=ACCENT,
    fg="white",
    font=FONT,
    relief="flat",
    padx=10,
    pady=5
)
preview_btn.grid(row=0, column=0, padx=10)

organize_btn = tk.Button(
    button_frame,
    text="Organize",
    command=organize_files,
    bg="#06d6a0",
    fg="black",
    font=FONT,
    relief="flat",
    padx=10,
    pady=5
)
organize_btn.grid(row=0, column=1, padx=10)

# ==========================
# PREVIEW BOX
# ==========================
preview_text = tk.Text(
    root,
    height=15,
    bg="#2a2a2a",
    fg="#eaeaea",
    insertbackground="white",
    font=("Consolas", 10),
    relief="flat"
)
preview_text.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

# ==========================
# RUN
# ==========================
root.mainloop()