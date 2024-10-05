import tkinter as tk
from random import randint
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")
root.config(bg="#f4f4f4")

# Generate a random number between 1 and 100
random_number = randint(1, 100)

# Reset the game
def reset_game():
    global random_number
    random_number = randint(1, 100)
    guess_entry.delete(0, tk.END)
    feedback_label.config(text="Guess a number between 1 and 100!")
    guess_button.config(state="normal")
    guess_entry.config(state="normal")

# Handle the guess input
def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            feedback_label.config(text="Please enter a number between 1 and 100!", fg="red")
        elif guess < random_number:
            feedback_label.config(text="Too low! Try again.", fg="orange")
        elif guess > random_number:
            feedback_label.config(text="Too high! Try again.", fg="orange")
        else:
            feedback_label.config(text=f"Congratulations! You guessed the number {random_number}!", fg="green")
            guess_button.config(state="disabled")
            guess_entry.config(state="disabled")
            messagebox.showinfo("Number Guessing Game", f"Well done! You guessed the number {random_number}!")
    except ValueError:
        feedback_label.config(text="Invalid input! Enter a number.", fg="red")

# Creating the UI components
title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=20)

instructions_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Helvetica", 14), bg="#f4f4f4", fg="#555")
instructions_label.pack(pady=10)

# Entry box for the number guess
guess_entry = tk.Entry(root, font=("Helvetica", 16), width=10)
guess_entry.pack(pady=10)

# Button to submit the guess
guess_button = tk.Button(root, text="Submit Guess", font=("Helvetica", 14), bg="#00b3b3", fg="#ffffff", command=check_guess)
guess_button.pack(pady=10)

# Feedback label
feedback_label = tk.Label(root, text="Start guessing...", font=("Helvetica", 14), bg="#f4f4f4", fg="#333")
feedback_label.pack(pady=20)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), bg="#ff6666", fg="#ffffff", command=reset_game)
reset_button.pack(pady=10)

# Run the main loop
root.mainloop()
