import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x300")
        self.root.config(bg="#2C3E50")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", bg="#2C3E50", fg="#ECF0F1", font=('Arial', 14))
        self.label.pack(pady=10)
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"), bg="#3498DB", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#2980B9")
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"), bg="#2ECC71", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#27AE60")
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"), bg="#E74C3C", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#C0392B")
        self.scissors_button.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="", bg="#2C3E50", fg="#ECF0F1", font=('Arial', 14))
        self.result_label.pack(pady=10)
        
        self.score_label = tk.Label(self.root, text="Score: You 0 - 0 Computer", bg="#2C3E50", fg="#ECF0F1", font=('Arial', 14))
        self.score_label.pack(pady=10)
    
    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You choose: {user_choice},\n Computer choose: {computer_choice}\n{result}")
        
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
