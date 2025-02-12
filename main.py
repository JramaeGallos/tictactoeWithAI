# Jramae A. Gallos
# CMSC 170 X4L
# Exercise 10

import tkinter as tk
from minmax import *
from PIL import Image, ImageTk
import time
from tkinter import messagebox

# class that holds the gui of the game
# root window - user prompt
# sub window - tictactoe screen game
class GUI:
    def __init__(self):
        self.board= {}
        self.root= tk.Tk()
        self.design()

        self.frame= tk.Frame(self.root)
        self.input_button(self.frame)

        self.root.mainloop()
    
    # function that initialized the design of the ui
    def design(self):
        self.root.geometry("300x100")
        self.root.title("K Means Clustering")
    
    # function that holds the input buttons
    def input_button(self, frame):
        self.labelA= tk.Label(self.root, text="What do you want to play?", font=('Arial', 12))
        self.labelA.pack(padx=60, pady=10, anchor='w')

        self.btn1= tk.Button(frame, text="X", font=("Arial", 12), bg='gray', command= self.set_X)
        self.btn1.grid(row=2, column=1)

        self.btn2= tk.Button(frame, text="O", font=("Arial", 12), bg='gray', command= self.set_O)
        self.btn2.grid(row=2, column=2)

        self.btn3= tk.Button(frame, text="Exit", font=("Arial", 12), bg='gray', command= self.set_exit)
        self.btn3.grid(row=2, column=3)

        frame.pack(padx=100, pady=10, anchor= 'w')
    
    # function that is called when the x button is clicked
    def set_X(self):
        self.start_game("X")
    
    # function that is called when the O button is clicked
    def set_O(self):
        self.start_game("O")
    
    # function that is called when the exit button is clicked
    def set_exit(self):
        self.root.quit()
    
    # function that is called when a tile is clicked
    def action(self, val, player):
        if is_free(self.board, val) == True:
            self.board[val] = player
            self.var.set(1)
            self.game_frame.destroy()
            self.update_board()

    def alert(self, message):
        show_method= getattr(messagebox, 'show{}'.format('info'))
        show_method("Game Over", message)
    
    # function that updates the board in the window when changes are made by the user
    def update_board_user(self, player):         
        self.game_frame= tk.Frame(self.game)

        r_cnt=0
        c_cnt=0

        for r in self.board.keys():
            if self.board[r] == "X":
                self.button= tk.Button(self.game_frame, image=self.x_btn, command= lambda m=r: self.action(m, player))
            elif self.board[r] == "O":
                self.button= tk.Button(self.game_frame, image=self.o_btn, command= lambda m=r: self.action(m, player))
            else:
                self.button= tk.Button(self.game_frame, image=self.emp_btn, command= lambda m=r: self.action(m, player))
            
            c_cnt = r%3
            if r <= 2: r_cnt=0
            elif r <= 5: r_cnt=1
            elif r <= 8: r_cnt=2
            self.button.grid(row=r_cnt, column=c_cnt)

        self.game_frame.pack(padx=50, pady=30, anchor= 'w')
    
    # function that updates the board in the window when changes are made by the ai
    def update_board(self):         
        self.game_frame= tk.Frame(self.game)

        r_cnt=0
        c_cnt=0

        # set the widgets in the screen
        for r in self.board.keys():
            if self.board[r] == "X":
                self.button= tk.Button(self.game_frame, image=self.x_btn)
            elif self.board[r] == "O":
                self.button= tk.Button(self.game_frame, image=self.o_btn)
            else:
                self.button= tk.Button(self.game_frame, image=self.emp_btn)
            
            c_cnt = r%3
            if r <= 2: r_cnt=0
            elif r <= 5: r_cnt=1
            elif r <= 8: r_cnt=2
            self.button.grid(row=r_cnt, column=c_cnt)

        self.game_frame.pack(padx=50, pady=30, anchor= 'w')

        # checks if the current state of the board is in won state
        result = get_winner(self.board)
        if result[0] == True:
            if result[1] != None:
                self.alert(f"Player {result[1]} won the game!")
                exit()
            else:
                self.alert("Draw! ")
                exit()
        else: 
            self.game_frame.destroy()

    # function that creates a new window to start the tictactoe game
    def start_game(self, user):
        self.game= tk.Toplevel(self.root)
        self.game.geometry("500x500")
        self.game.title("TicTacToe Game")

        emp_image= Image.open('empty_tile.png')
        emp_img= emp_image.resize((130, 130))
        self.emp_btn= ImageTk.PhotoImage(emp_img)
    
        o_image= Image.open('o_tile.png')
        o_img= o_image.resize((130, 130))
        self.o_btn= ImageTk.PhotoImage(o_img)
        
        x_image= Image.open('x_tile.png')
        x_img= x_image.resize((130, 130))
        self.x_btn= ImageTk.PhotoImage(x_img)

        self.board= init_board
        # wait variable
        self.var= tk.IntVar()

        # X player always plays first
        if user == "X":
            ai = "O"
            while not get_winner(self.board)[0]:
                print(self.board)
                # wait for user move
                self.update_board_user(user)
                self.button.wait_variable(self.var)
                
                # ai move
                # update window
                self.board= ai_move(self.board, ai) 
                self.update_board()
        else:
            ai = "X"
            while not get_winner(self.board)[0]:
                print(self.board)
                # ai move 
                self.board= ai_move(self.board, ai)  
                self.update_board()

                # wait for user move
                self.update_board_user(user)
                self.button.wait_variable(self.var)
        
GUI()