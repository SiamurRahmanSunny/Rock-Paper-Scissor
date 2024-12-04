import tkinter as tk
from tkinter import messagebox
import random

root= tk.Tk()
root.title("RPS")
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(bg="orange")

# VARIABLES
player_name = tk.StringVar()
buttons = ["ROCK", "PAPER", "SCISSOR"]
ai_choose_list = ["ROCK", "PAPER", "SCISSOR"]
# VARIABLES

def check(index):
    global ai_choose
    ai_choose = random.choice(ai_choose_list)
    print(index)
    print(ai_choose)
    if index == ai_choose:
        messagebox.showinfo("Feedback", f"Draw AI Choosed {ai_choose}")
    elif (index == "ROCK" and ai_choose == "SCISSOR") or \
            (index == "PAPER" and ai_choose == "ROCK") or \
            (index == "SCISSOR" and ai_choose == "PAPER"):
        messagebox.showinfo("Feedback", f"You Win! AI chose {ai_choose}")
    else:
        messagebox.showinfo("Feedback", f"You Lose! AI chose {ai_choose}")

def submit_name():
    if player_name.get() == "":
        messagebox.showerror("Error", "Please enter a name")
    else:
        design_instance.l1.config(text=f"Welcome {player_name.get()} Have A Nice Game!")
        for widget in design_instance.f5.winfo_children():
            widget.destroy()
        messagebox.showinfo("Success", "Welcome " + player_name.get())
        for i,button in enumerate(buttons):
            rps_button = tk.Button(
                design_instance.f5,
                text=button,
                font=("arial", 20, "bold"),
                bg="red",
                borderwidth=0,
                command=lambda idx=button: check(idx)
            )
            rps_button.pack(pady=5)

class design:
    def __init__(self,master):
        self.f1 = tk.Frame(master, bg="red")
        self.f2 = tk.Frame(master, bg="red")
        self.f3 = tk.Frame(master, bg="red")
        self.f4 = tk.Frame(master, bg="red")
        self.f5 = tk.Frame(master, bg="orange")
        self.l1 = tk.Label(self.f1, text="Welcome To Rock-Paper-Scissors Game Programmed By Python", bg="red", font=("Arial", 14))
        self.l2 = tk.Label(self.f2, text="  ", bg="red", font=("Arial", 16))
        self.l3 = tk.Label(self.f3, text="  ", bg="red", font=("Arial", 16))
        self.l4 = tk.Label(self.f5, text="Enter Your Name: ", bg="orange", font=("Arial", 16))
        self.l5 = tk.Entry(self.f5, textvariable=player_name, bg="grey", font=("Arial", 16))
        self.b1 = tk.Button(self.f4, text="Submit", bg="red", font=("Arial", 16), borderwidth=0, command=submit_name)
        self.f1.pack(side="top", fill="x")
        self.f2.pack(side="left", fill="y")
        self.f3.pack(side="right", fill="y")
        self.f4.pack(side="bottom", fill="x")
        self.f5.pack(side="top", fill="x")
        self.l1.pack(side="top")
        self.l2.pack(side="left")
        self.l3.pack(side="right")
        self.l4.pack(side="left")
        self.l5.pack(side="left")
        self.b1.pack(side="bottom", fill="x")

design_instance = design(root)

root.mainloop()