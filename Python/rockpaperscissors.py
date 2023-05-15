from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

score = [0, 0, 0]
health = 3

def display(player, computer):
  movesLabel.config(text=player + " vs " + computer)
  healthLabel.config(text="Health: " + str(health))

def rockPaperScissors(player):
  global health
  
  movesLabel.config(text=player + " vs ")

  moves = ["rock", "paper", "scissors"]
  computer = random.choice(moves)
  
  if player == computer:
    score[1] += 1
  elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    score[0] +=1
  else:
    score[2] += 1
    health -= 1
  
  movesLabel.after(1000, lambda: display(player, computer))  
    
  if health == 0:
    messagebox.showinfo("You lost", "Score: " + str(score[0]) + "-" + str(score[1]) + "-" + str(score[2]))
    window.destroy()
    
# Window
window = Tk()
window.geometry("400x400")
window.title("Rock, paper, scissors")
window.config(background="white")


# # Buttons
rock = Button(window,
                font=("Visby",13, "bold"),
                text="Rock",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("rock"))

rock.place(x=40, y=40)

paper = Button(window,
                font=("Visby",13, "bold"),
                text="Paper",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("paper"))

scissors = Button(window,
                font=("Visby",13, "bold"),
                text="Scissors",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=lambda: rockPaperScissors("scissors"))


paper.place(x=160, y=40)
scissors.place(x=280, y=40)

# Labels
movesLabel = Label(window,
             font=("Visby",15, "bold"),
             text="",
             background="white",
             relief=FLAT)
movesLabel.place(x=120, y =150)

healthLabel = Label(window,
             font=("Visby",15, "bold"),
             text="Health: 3",
             background="white",
             relief=FLAT)
healthLabel.pack(side=BOTTOM)


window.mainloop()