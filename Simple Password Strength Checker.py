import re
import random
import string
import tkinter as tk
from tkinter import messagebox

# passarea
def check_password():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()]", password):
        score += 1

    if score >= 4:
        messagebox.showinfo("Result", "Good Password B)")
    else:
        messagebox.showwarning("Result", "Bad Password1!1!")


# Generator 
def generate_password():
    length = 12

    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*()"
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    entry.delete(0, tk.END)
    entry.insert(0, password)

    messagebox.showinfo("Generated Password", "Strong password created!")


# gui
root = tk.Tk()
root.title("Password Security Tool")
root.geometry("350x200")

label = tk.Label(root, text="Enter or Generate Password:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Password", command=check_password)
check_btn.pack(pady=5)

gen_btn = tk.Button(root, text="Generate Password", command=generate_password)
gen_btn.pack(pady=5)

root.mainloop()