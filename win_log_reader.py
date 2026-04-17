import tkinter as tk
from tkinter import ttk, messagebox
import win32evtlog
import datetime

# scanner
def scan_logs():
    log_type = combo.get()

    try:
        hand = win32evtlog.OpenEventLog("localhost", log_type)

        flags = (
            win32evtlog.EVENTLOG_BACKWARDS_READ |
            win32evtlog.EVENTLOG_SEQUENTIAL_READ
        )

        events = win32evtlog.ReadEventLog(hand, flags, 0)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    output.delete("1.0", tk.END)

    suspicious_keywords = [
        "failed", "error", "denied", "unauthorized", "invalid"
    ]

    total = 0
    suspicious = 0

    for event in events:
        total += 1

        try:
            time_generated = event.TimeGenerated.Format()
        except:
            time_generated = "Unknown Time"

        event_id = getattr(event, "EventID", "Unknown ID")

        try:
            message = str(event.StringInserts)
        except:
            message = "No message available"

        clean_msg = message.lower()

        is_bad = any(word in clean_msg for word in suspicious_keywords)

        line = f"[{time_generated}] | Event ID: {event_id} | {message}\n"

        if is_bad:
            suspicious += 1
            output.insert(tk.END, "🚨 SUSPICIOUS: " + line + "\n")
        else:
            output.insert(tk.END, line + "\n")

    summary = f"\n--- SUMMARY ---\nTotal Events: {total}\nSuspicious: {suspicious}\n"
    output.insert(tk.END, summary)


# gui
root = tk.Tk()
root.title("Windows Event Viewer Lite (Cyber Tool)")
root.geometry("800x500")

label = tk.Label(root, text="Select Windows Log Type:")
label.pack(pady=5)

combo = ttk.Combobox(root, values=["System", "Application", "Security"])
combo.current(0)
combo.pack(pady=5)

btn = tk.Button(root, text="Scan Logs", command=scan_logs)
btn.pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

scroll = tk.Scrollbar(frame)
scroll.pack(side="right", fill="y")

output = tk.Text(frame, wrap="word", yscrollcommand=scroll.set)
output.pack(fill="both", expand=True)

scroll.config(command=output.yview)

root.mainloop()