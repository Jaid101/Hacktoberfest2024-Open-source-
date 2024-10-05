import tkinter as tk
from tkinter import messagebox

# Initialize the window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x450")
root.config(bg="#f4f4f4")

# Game variables
player = "X"
buttons = [[None, None, None], [None, None, None], [None, None, None]]

# Switch between players
def switch_player():
    global player
    player = "O" if player == "X" else "X"

# Check if there is a winner
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            highlight_winner([buttons[row][0], buttons[row][1], buttons[row][2]])
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            highlight_winner([buttons[0][col], buttons[1][col], buttons[2][col]])
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True

    return False

# Highlight the winning buttons
def highlight_winner(winning_buttons):
    for button in winning_buttons:
        button.config(bg="lightgreen")

# Check if it's a draw
def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# Button click handler
def button_click(r, c):
    global player
    if buttons[r][c]["text"] == "" and not check_winner():
        buttons[r][c]["text"] = player
        buttons[r][c].config(state="disabled")
        
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {player} wins!")
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        else:
            switch_player()
            status_label.config(text=f"Player {player}'s turn")

# Reset the game
def reset_game():
    global player
    player = "X"
    status_label.config(text="Player X's turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state="normal", bg="#ffffff")

# Creating the UI
status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 16), bg="#f4f4f4", fg="#333")
status_label.pack(pady=20)

# Frame for the Tic-Tac-Toe grid
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

# Create 3x3 grid of buttons
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(frame, text="", font=("Helvetica", 20), width=5, height=2, 
                                  bg="#ffffff", fg="#333", 
                                  command=lambda r=r, c=c: button_click(r, c))
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Helvetica", 14), bg="#ff6666", fg="#ffffff", command=reset_game)
reset_button.pack(pady=20)

# Run the application
root.mainloop()
