import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    target = entry.get()

    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445]

    open_ports = []
    closed_ports = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        messagebox.showerror("Error", "Invalid host or IP")
        return

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)

        s.close()

    message = f"Target: {target} ({ip})\n\n"

    message += "OPEN PORTS:\n"
    message += ", ".join(map(str, open_ports)) if open_ports else "None"

    message += "\n\nCLOSED PORTS:\n"
    message += ", ".join(map(str, closed_ports)) if closed_ports else "None"

    messagebox.showinfo("Scan Results", message)


# GUI setup
root = tk.Tk()
root.title("Simple Port Scanner")
root.geometry("350x150")

label = tk.Label(root, text="Enter IP or Website:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Scan Ports", command=scan_ports)
button.pack(pady=10)

root.mainloop()