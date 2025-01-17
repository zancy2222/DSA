import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("700x700")
root.configure(bg="#e8f5e9")  # Mint Green background

# Center the window
window_width, window_height = 700, 700
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Game state variables
buttons = [[None for _ in range(3)] for _ in range(3)]
scores = {"X": 0, "O": 0}
player_names = {"X": "Player X", "O": "Player O"}
current_player = "X"

# Functions
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return [(i, 0), (i, 1), (i, 2)]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return [(0, i), (1, i), (2, i)]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return [(0, 0), (1, 1), (2, 2)]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return [(0, 2), (1, 1), (2, 0)]
    return None

def reset_board():
    global current_player
    current_player = "X"
    turn_label.config(text=f"{player_names[current_player]}'s Turn ({current_player})")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#a5d6a7", state=tk.NORMAL)

def on_button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col].config(text=current_player, state=tk.DISABLED, bg="#66bb6a")
        winning_combination = check_winner()
        if winning_combination:
            for (i, j) in winning_combination:
                buttons[i][j].config(bg="#ffcc80")
            messagebox.showinfo("Game Over", f"{player_names[current_player]} Wins!")
            scores[current_player] += 1
            update_scoreboard()
            reset_board()
        elif all(button["text"] != "" for row in buttons for button in row):
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"{player_names[current_player]}'s Turn ({current_player})")

def update_scoreboard():
    scoreboard_label.config(text=f"{player_names['X']}: {scores['X']}    {player_names['O']}: {scores['O']}")

def set_player_names():
    def save_names():
        player_names["X"] = player_x_name_entry.get() or "Player X"
        player_names["O"] = player_o_name_entry.get() or "Player O"
        name_window.destroy()
        update_scoreboard()

    name_window = tk.Toplevel(root)
    name_window.title("Set Player Names")
    name_window.geometry("300x200")
    name_window.configure(bg="#e8f5e9")

    tk.Label(name_window, text="Player X Name:", bg="#e8f5e9").pack(pady=10)
    player_x_name_entry = tk.Entry(name_window)
    player_x_name_entry.pack()

    tk.Label(name_window, text="Player O Name:", bg="#e8f5e9").pack(pady=10)
    player_o_name_entry = tk.Entry(name_window)
    player_o_name_entry.pack()

    tk.Button(name_window, text="Save", command=save_names).pack(pady=10)

def restart_game():
    global scores
    scores = {"X": 0, "O": 0}
    update_scoreboard()
    reset_board()

# Layout
title_label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#e8f5e9", fg="#1b5e20")
title_label.pack(pady=20)

scoreboard_label = tk.Label(root, text="", font=("Arial", 16), bg="#e8f5e9", fg="#1b5e20")
scoreboard_label.pack(pady=10)

turn_label = tk.Label(root, text="", font=("Arial", 18), bg="#e8f5e9", fg="#1b5e20")
turn_label.pack(pady=10)

grid_frame = tk.Frame(root, bg="#e8f5e9")
grid_frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            grid_frame, text="", font=("Arial", 24), width=5, height=2, bg="#a5d6a7",
            command=lambda r=i, c=j: on_button_click(r, c)
        )
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

button_frame = tk.Frame(root, bg="#e8f5e9")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Set Player Names", command=set_player_names, bg="#2e7d32", fg="white").pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Restart Game", command=restart_game, bg="#d32f2f", fg="white").pack(side=tk.LEFT, padx=10)

# Start the game
update_scoreboard()
reset_board()
root.mainloop()
