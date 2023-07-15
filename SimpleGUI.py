import random
import tkinter as tk
from tkinter import messagebox, StringVar
from time import time


class RPSGame:
    def __init__(self):
        self.total_plays = 0
        self.user_winnings = 0
        self.total_play_time = 0
        self.options = ['ROCK', 'PAPER', 'SCISSORS']
        self.user_play = 0
        self.name = ''
        self.fname = ''
        self.create_window()

    def play(self, user_choice):
        self.total_plays += 1
        pc_play = random.choice(self.options)
        self.user_play = self.options.index(user_choice) + 1
        pc_play_index = self.options.index(pc_play) + 1

        if self.user_play == pc_play_index:
            result = 'THAT\'S A TIE BUDDY!'
        elif (self.user_play == 1 and pc_play_index == 3) or (self.user_play == 2 and pc_play_index == 1) or (self.user_play == 3 and pc_play_index == 2):
            self.user_winnings += 1
            result = "YOU WIN!"
        else:
            result = "YOU LOSE!"
        messagebox.showinfo(
            "RESULT", f"YOU CHOSE {user_choice}, PC CHOSE {pc_play}. {result}")

    def get_name(self):
        self.name = self.ent_name.get().upper()
        self.gender = self.ent_gender.get().upper()
        if self.gender.lower() == 'm':
            self.fname = 'MR. ' + self.name.capitalize().split(" ")[0]
        elif self.gender.lower() == 'f':
            self.fname = 'MS. ' + self.name.capitalize().split(" ")[0]
        else:
            messagebox.showinfo("ERROR", "PLEASE ENTER 'M' OR 'F'")
        self.lbl_name['text'] = "Welcome, " + self.fname + "!"

    def create_window(self):
        self.root = tk.Tk()
        self.root.title('ROCK, PAPER, SCISSORS')
        self.root.geometry("500x300")
        self.root.configure(background='black')

        # Use the Calibri font, size 12 and bold
        font_format = ("Calibri", 12, "bold")

        # Added additional padding
        for _ in range(2):
            lbl_empty = tk.Label(self.root, text=" ", bg='black')
            lbl_empty.pack(anchor='center')

        self.lbl_name = tk.Label(
            self.root, text="TYPE YOUR NAME BUDDY: ", bg='black', fg='white', font=font_format)
        self.lbl_name.pack(anchor='center')

        self.ent_name = tk.Entry(self.root, font=font_format)
        self.ent_name.pack(anchor='center')

        self.lbl_gender = tk.Label(
            self.root, text="CHOOSE YOUR GENDER (M/F): ", bg='black', fg='white', font=font_format)
        self.lbl_gender.pack(anchor='center')

        self.ent_gender = tk.Entry(self.root, font=font_format)
        self.ent_gender.pack(anchor='center')

        # Added padding before the "Submit" button
        lbl_empty = tk.Label(self.root, text=" ", bg='black')
        lbl_empty.pack(anchor='center')

        self.btn_name = tk.Button(
            self.root, text="SUBMIT", command=self.get_name, font=font_format)
        self.btn_name.pack(anchor='center')

        lbl_empty = tk.Label(self.root, text=" ", bg='black')
        lbl_empty.pack(anchor='center')

        self.btn_frame = tk.Frame(self.root, bg='black')
        self.btn_frame.pack(anchor='center')

        self.btn_rock = tk.Button(
            self.btn_frame, text="ROCK", command=lambda: self.play("ROCK"), font=font_format)
        self.btn_rock.pack(side='left', padx=5)  # Added space between buttons
        self.btn_paper = tk.Button(
            self.btn_frame, text="PAPER", command=lambda: self.play("PAPER"), font=font_format)
        # Added space between buttons
        self.btn_paper.pack(side='left', padx=5)
        self.btn_scissors = tk.Button(
            self.btn_frame, text="SCISSORS", command=lambda: self.play("SCISSORS"), font=font_format)
        # Added space between buttons
        self.btn_scissors.pack(side='left', padx=5)

        self.root.mainloop()


RPSGame()
