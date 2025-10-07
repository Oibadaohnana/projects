import tkinter as tk
from tkinter import ttk

def calculate():
    # Get input values
    group_a = entry_a.get()
    group_b = entry_b.get()

    # (For now) just show what was entered
    result_label.config(text=f"Group A: {group_a}\nGroup B: {group_b}")

def main():
    window = tk.Tk()
    window.title("Mann-Whitney U Test Calculator")
    window.geometry("400x250")
    window.resizable(False, False)

    # === Title ===
    ttk.Label(window, text="Mann-Whitney U Test", font=("Arial", 16, "bold")).pack(pady=10)

    # === Group A Input ===
    frame_a = ttk.Frame(window)
    frame_a.pack(pady=5, padx=10, fill="x")
    ttk.Label(frame_a, text="Group A Values (comma-separated):").pack(anchor="w")
    global entry_a
    entry_a = ttk.Entry(frame_a)
    entry_a.pack(fill="x")

    # === Group B Input ===
    frame_b = ttk.Frame(window)
    frame_b.pack(pady=5, padx=10, fill="x")
    ttk.Label(frame_b, text="Group B Values (comma-separated):").pack(anchor="w")
    global entry_b
    entry_b = ttk.Entry(frame_b)
    entry_b.pack(fill="x")

    # === Calculate Button ===
    ttk.Button(window, text="Calculate", command=calculate).pack(pady=10)

    # === Result Label ===
    global result_label
    result_label = ttk.Label(window, text="", foreground="blue", justify="center")
    result_label.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
