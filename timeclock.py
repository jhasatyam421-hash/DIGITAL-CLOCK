import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Wall Clock")
root.geometry("960x260")
root.configure(bg="#000000")
root.resizable(False, False)
root.attributes("-topmost", True)

# Main panel
panel = tk.Frame(root, bg="#030303", padx=18, pady=16)
panel.pack(fill="both", expand=True)

# Days list on the left side
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_labels = []
panel.columnconfigure(1, weight=1)

for i, day in enumerate(weekdays):
    lbl = tk.Label(
        panel,
        text=day,
        font=("Segoe UI", 18, "bold"),
        fg="#d8d8d8",
        bg="#030303",
        anchor="w",
        justify="left",
        padx=8,
    )
    lbl.grid(row=i, column=0, sticky="w", pady=2)
    day_labels.append(lbl)

# Time display on the right
clock_frame = tk.Frame(panel, bg="#030303")
clock_frame.grid(row=0, column=1, rowspan=7, sticky="nsew", padx=(25, 10), pady=8)

# AM/PM indicator
ampm = tk.Label(
    clock_frame,
    text="PM",
    font=("Segoe UI", 14, "bold"),
    fg="#dfe7df",
    bg="#030303",
)
ampm.pack(anchor="w", padx=6)

# Time label
clock = tk.Label(
    clock_frame,
    text="12:00:00",
    font=("Segoe UI", 88, "bold"),
    fg="#2efc5d",
    bg="#030303",
    justify="center",
    padx=6,
)
clock.pack(anchor="center")

# Date label below the time
calendar = tk.Label(
    clock_frame,
    text="APR 15",
    font=("Segoe UI", 22, "bold"),
    fg="#c8f9d0",
    bg="#030303",
    padx=10,
    pady=6,
)
calendar.place(relx=1.0, rely=0.78, anchor="e")


def update_clock():
    weekday_index = int(strftime("%w"))  # Sunday=0 so convert below
    weekday_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    day_text = strftime("%a")
    current_day = day_text
    active_index = weekday_names.index(current_day)

    for idx, label in enumerate(day_labels):
        label.config(fg="#d8d8d8" if idx != active_index else "#2efc5d")

    current_time = strftime("%I:%M:%S")
    clock.config(text=current_time)
    ampm.config(text=strftime("%p"))
    calendar.config(text=strftime("%b %d").upper())
    root.after(1000, update_clock)


update_clock()
root.mainloop()
