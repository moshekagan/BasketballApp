from tkinter import *
import tkinter.ttk as ttk

from League import League


def handel_create_game_click():
    print("You need to implement me...")


league = League()

win = Tk()
win.title("My NBA League")
win.geometry("1000x600")
title = Label(win, text="My NBA App", font=("Ariel Bold", 50), fg="purple")
title.grid(column=0, row=0)

status_label = Label(win, text="Welcome to my NBA app")
status_label.grid(column=0, row=1)

status_label = Label(win, text="Create new game:", fg="blue")
status_label.grid(column=0, row=2)

teams_combo_1 = ttk.Combobox(win, values=[])
teams_combo_1.grid(row=3, column=0)

teams_combo_2 = ttk.Combobox(win, values=[])
teams_combo_2.grid(row=3, column=1)

btn = Button(win, text="Create Game", width=10, height=2, command=handel_create_game_click)
btn.grid(row=3, column=3)

win.mainloop()
print("App end")
