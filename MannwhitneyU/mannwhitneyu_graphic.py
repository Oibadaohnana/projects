from scipy.stats import mannwhitneyu
import tkinter as tk
from tkinter import ttk


def create_window():
    window = tk.Tk()
    window.title("Mann-Whitney U Test Calculator")
    window.geometry("600x600")
    window.resizable(False, False)
    

    Header = ttk.Label(window,
                text="Mann-Whitney U Test",
                font=("Serif", 16, "bold"))
    Header.grid(row=0, columnspan=3,sticky="n", padx=10)

    
    Group_A_Widget =  ttk.Label(window,
                text="Group A Values (Space separated):",
                anchor="n")
    Group_A_Widget.grid(row=1, columnspan=3, sticky="n",padx=5)
    
    entry_a = ttk.Entry(window)
    entry_a.grid(row=2, columnspan=3, padx=5, sticky="n")

    
    Group_B_Widget = ttk.Label(window,
                text="Group B Values (Space separated):",
                anchor="n")
    Group_B_Widget.grid(row=3, columnspan=3, sticky="n", padx=5)
    
    entry_b = ttk.Entry(window)
    entry_b.grid(row=4, columnspan=3, padx=5, sticky="n")

    
    mannwhitneyu_method = tk.StringVar(value="auto")
    mannwhitneyu_alternative = tk.StringVar(value="two-sided")
    

    method_select_asymptotic = tk.Button(window,
                text="Asymptotic method",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_method.set("asymptotic"),update_method_widget(window, mannwhitneyu_method)))
    method_select_asymptotic.grid(row=5,column=2,padx=5,pady=5)

    method_select_exact = tk.Button(window,
                text="Exact method",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_method.set("exact"),update_method_widget(window, mannwhitneyu_method)))
    method_select_exact.grid(row=5,column=1,padx=5,pady=5)

    method_select_auto = tk.Button(window,
                text="Auto method (Default)",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_method.set("auto"),update_method_widget(window, mannwhitneyu_method)))
    method_select_auto.grid(row=5,column=0,padx=5,pady=5)

    Alternative_Text_Widget =  ttk.Label(window,
                text="Expectation of Group A compared to Group B:",
                anchor="n")
    Alternative_Text_Widget.grid(row=7, columnspan=3, sticky="n",padx=5)

    alternativ_select_less = tk.Button(window,
                text="less",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_alternative.set("less"),update_alternative_widget(window, mannwhitneyu_alternative)))
    alternativ_select_less.grid(row=8,column=1,padx=5,pady=5)

    alternativ_select_more = tk.Button(window,
                text="greater",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_alternative.set("greater"),update_alternative_widget(window, mannwhitneyu_alternative)))
    alternativ_select_more.grid(row=8,column=2,padx=5,pady=5)

    alternativ_select_two_sided = tk.Button(window,
                text="two-sided/equal (Default)",
                background="#f0f0f0",
                activebackground="#a0a0a0",
                command=lambda: (mannwhitneyu_alternative.set("two-sided"),update_alternative_widget(window, mannwhitneyu_alternative)))
    alternativ_select_two_sided.grid(row=8,column=0,padx=5,pady=5)



    Calculate_Button = tk.Button(window, 
                text="Calculate",
                command = lambda: mannwhitneyu_calc(entry_a, entry_b, window, mannwhitneyu_method.get(),mannwhitneyu_alternative.get()))
    Calculate_Button.grid(row=12,columnspan=3,pady=20 )
    window.bind('<Return>', lambda event: mannwhitneyu_calc(entry_a, entry_b, window, mannwhitneyu_method.get(),mannwhitneyu_alternative.get()))

    
    
    window.grid_columnconfigure(1, weight=1)
    return window

def update_method_widget(window, mannwhitneyu_method):
    for widget in window.grid_slaves(row=6):
        widget.destroy()
    method_Label= ttk.Label(window, text=f"Method: {mannwhitneyu_method.get()}")
    method_Label.grid(row=6, column= 1, pady=5, padx=5)

def update_alternative_widget (window, mannwhitneyu_alternative):
    for widget in window.grid_slaves(row=9):
        widget.destroy()
    alternative_Label = ttk.Label(window, text=f"Alternative: {mannwhitneyu_alternative.get()}")
    alternative_Label.grid(row=9, column=1, pady= 5,padx=5)

def mannwhitneyu_calc(entry_a, entry_b, window, mannwhitneyu_method, mannwhitneyu_alternative):
    group_a = [float(x) for x in entry_a.get().split(" ")]
    group_b = [float(x) for x in entry_b.get().split(" ")]
    U1, p = mannwhitneyu(group_a, group_b, alternative=mannwhitneyu_alternative,method=mannwhitneyu_method)
    nx,ny = len(group_a), len(group_b)
    U2 = nx*ny - U1
    print(f"alternative = {mannwhitneyu_alternative}")
    print(f"method: {mannwhitneyu_method}")
    print(f"the P value is: {p}")
    print(U1, U2)
    show_result(window, p, U1,U2)
    return p , U1 , U2

def show_result(window, p, U1, U2):
    text_Label = ttk.Label(window, text="Results:")
    text_Label.grid(row=10, column=1, pady=10)
    result_text = f"P Value: {p}\nU1: {U1}\nU2: {U2}"
    result_widget = tk.Text(window,
                    background="#f0f0f0",
                    font="Arial",
                    height=4,
                    )
    result_widget.insert("1.0", result_text)
    result_widget.grid(row=11, column=1)
    

def main():
    window = create_window()  
    window.mainloop()

if __name__ == "__main__":
    main()