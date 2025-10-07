import tkinter as tk
from tkinter import ttk
from scipy.stats import mannwhitneyu

def mannwhitneyu_calc(group_a, group_b):
    # Perform Mann-Whitney U test
    U1, p = mannwhitneyu(group_a, group_b, method="asymptotic")

    nx, ny = len(group_a), len(group_b)
    U2 = nx * ny - U1

    # Display results
    result_label_calc.config(
        text=f"U1 = {U1:.3f}\nU2 = {U2:.3f}\np-value = {p:.4f}"
    )

def calculate():
    try:
        # Get input values and convert to floats
        group_a = [float(x) for x in entry_a.get().split(",") if x.strip()]
        group_b = [float(x) for x in entry_b.get().split(",") if x.strip()]

        result_label.config(text=f"Group A: {group_a}\nGroup B: {group_b}")

        mannwhitneyu_calc(group_a, group_b)

    except ValueError:
        result_label.config(text="⚠️ Please enter numeric, comma-separated values.")

def create_window():
    global entry_a, entry_b, result_label, result_label_calc

    root = tk.Tk()
    root.title("Mann-Whitney U Test Calculator")
    root.geometry("400x500")
    root.resizable(False, False)

    ttk.Label(root, text="Mann-Whitney U Test", font=("Arial", 16, "bold")).pack(pady=10)

    # === Group A Input ===
    frame_a = ttk.Frame(root)
    frame_a.pack(pady=5, padx=10, fill="x")
    ttk.Label(frame_a, text="Group A Values (comma-separated):").pack(anchor="w")
    entry_a = ttk.Entry(frame_a)
    entry_a.pack(fill="x")

    # === Group B Input ===
    frame_b = ttk.Frame(root)
    frame_b.pack(pady=5, padx=10, fill="x")
    ttk.Label(frame_b, text="Group B Values (comma-separated):").pack(anchor="w")
    entry_b = ttk.Entry(frame_b)
    entry_b.pack(fill="x")

    # === Calculate Button ===
    ttk.Button(root, text="Calculate", command=calculate).pack(pady=10)

    # === Result Labels ===
    result_label = ttk.Label(root, text="", foreground="blue", justify="center")
    result_label.pack(pady=5)

    result_label_calc = ttk.Label(root, text="", foreground="black", justify="center")
    result_label_calc.pack(pady=5)

    root.mainloop()

def main():
    create_window()

if __name__ == "__main__":
    main()
