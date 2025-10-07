import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')

def other_return_pressed(event):
    print("other Return pressed")


def main():
    window = tk.Tk()
    photo = tk.PhotoImage(file='/home/benji/Projects/MannwhitneyU/IconMWU.png') #LINUX SPECIFIC!
    window.iconphoto(False, photo)

    #window attributes
    window.title("Mann Whitney U test calculation")
    window.attributes('-topmost', 1)
    header = tk.Label(window, text="Hello, World!")
    header.pack()
    
    
    """ ttk.Button(window, text='Rock', command=lambda: select('Rock')).pack()
    ttk.Button(window, text='Paper',command=lambda: select('Paper')).pack()
    ttk.Button(window, text='Scissors', command=lambda: select('Scissors')).pack() """

    btn = ttk.Button(window, text='Save')
    btn.bind('<Return>', return_pressed)
    btn2 = ttk.Button(window, text='other Save')
    btn2.bind('<Return>', other_return_pressed)


    btn.focus()
    btn.pack(expand=True)
    btn2.pack(expand=True)

    window.mainloop()

if __name__=="__main__":
    main()