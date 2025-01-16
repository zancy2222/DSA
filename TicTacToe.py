import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("700x700")
        self.root.configure(bg="#e8f5e9")  # Mint Green background

        # Center the window on the screen
        window_width = 700
        window_height = 700
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0}
        self.player_names = {"X": "", "O": ""}

        # Create a frame to hold the grid
        self.grid_frame = tk.Frame(self.root, bg="#683632")
        self.grid_frame.grid(row=2, column=1, padx=20, pady=20)

        # Create turn label
        self.turn_label = tk.Label(self.root, text="", font=("Fixedsys", 18), bg="#e8f5e9", fg="#1b5e20")
        self.turn_label.grid(row=1, column=1, pady=10)

        # Create buttons grid inside the frame
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.grid_frame, text="", font=("Fixedsys", 28), width=5, height=2,
                    command=lambda r=i, c=j: self.on_button_click(r, c), bg="#a5d6a7", relief="raised", bd=3
                )
                self.buttons[i][j].grid(row=i, column=j, padx=8, pady=8)

        # Adjust the layout of the root window
        self.root.grid_rowconfigure(0, weight=1)  # Space above the grid
        self.root.grid_rowconfigure(1, weight=1)  # Center the turn label vertically
        self.root.grid_rowconfigure(2, weight=1)  # Center the grid vertically
        self.root.grid_rowconfigure(3, weight=1)  # Space below the grid
        self.root.grid_columnconfigure(0, weight=1)  # Space to the left of the grid
        self.root.grid_columnconfigure(1, weight=1)  # Center the grid horizontally
        self.root.grid_columnconfigure(2, weight=1)  # Space to the right of the grid

        # Scoreboard Label
        self.score_label = tk.Label(self.root, text="Enter Player Names to Start", font=("Fixedsys", 18), bg="#e8f5e9", fg="#306230")  # Dark Green
        self.score_label.grid(row=3, column=0, columnspan=3, pady=0)

        # Set Player Names Button
        self.start_button = tk.Button(self.root, text="Set Player Names", font=("Fixedsys", 18), command=self.get_player_names, bg="#306230", fg="white")  # Forest Green
        self.start_button.grid(row=4, column=0, columnspan=3, pady=0)

        # Restart Game Button
        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Fixedsys", 18), command=self.restart_game, bg="#306230", fg="white")  # Forest Green
        self.restart_button.grid(row=5, column=0, columnspan=3, pady=10)

        # Exit Game Button
        self.exit_button = tk.Button(self.root, text="Exit Game", font=("Fixedsys", 18), command=self.exit_game, bg="#e0102f", fg="white")  # Dark Red
        self.exit_button.grid(row=6, column=0, columnspan=3, pady=10)

        self.root.mainloop()

    # Function to check for a win and return the winning combination
    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return [(i, 0), (i, 1), (i, 2)]
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return [(0, i), (1, i), (2, i)]
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return [(0, 0), (1, 1), (2, 2)]
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return [(0, 2), (1, 1), (2, 0)]
        return None

    # Function to animate winning buttons
    def animate_winner(self, winning_combination):
        for _ in range(5):  # Flash animation
            for (i, j) in winning_combination:
                self.buttons[i][j].config(bg="#66bb6a")  # Medium Green
            self.root.update()
            time.sleep(0.2)
            for (i, j) in winning_combination:
                self.buttons[i][j].config(bg="#a5d6a7" if self.buttons[i][j]["text"] == "X" else "#a5d6a7")  # Light Green
            self.root.update()
            time.sleep(0.2)

    # Button click handler
    def on_button_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.buttons[row][col].config(bg="#a5d6a7", fg="black", relief="raised", bd=3)

            winning_combination = self.check_winner()
            if winning_combination:
                self.animate_winner(winning_combination)
                messagebox.showinfo("Game Over", f"Congratulations {self.player_names[self.current_player]}!")
                self.scores[self.current_player] += 1
                self.update_scoreboard()
                self.reset_board()
            elif all(button["text"] != "" for row in self.buttons for button in row):
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_turn_label()
        else:
            messagebox.showwarning("Invalid Move", "This spot is already taken!")

    # Reset the board
    def reset_board(self):
        self.current_player = "X"
        self.update_turn_label()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j].config(bg="#a5d6a7", fg="black", relief="raised", bd=3)

    # Reset the entire game
    def restart_game(self):
        self.reset_board()
        self.scores["X"] = 0
        self.scores["O"] = 0
        self.update_scoreboard()

    # Update scoreboard labels
    def update_scoreboard(self):
        if self.player_names["X"] and self.player_names["O"]:
            self.score_label.config(text=f"{self.player_names['X']}: {self.scores['X']}      {self.player_names['O']}: {self.scores['O']}", fg="#1b5e20")  # Dark Green
        else:
            self.score_label.config(text="Enter Player Names to Start", fg="#1b5e20")

    # Update turn label
    def update_turn_label(self):
        if self.player_names["X"] and self.player_names["O"]:
            self.turn_label.config(text=f"{self.player_names[self.current_player]}'s Turn ({self.current_player})", fg="#1b5e20")
        else:
            self.turn_label.config(text="", fg="#1b5e20")

    # Function to open a dialog for player names
    def get_player_names(self):
        name_window = tk.Toplevel(self.root)
        name_window.title("Enter Player Names")
        name_window.geometry("400x300")
        name_window.configure(bg="#e8f5e9")

        def save_names():
            self.player_names["X"] = player_x_name_entry.get()
            self.player_names["O"] = player_o_name_entry.get()
            if not self.player_names["X"] or not self.player_names["O"]:
                messagebox.showwarning("Input Error", "Both players need to enter a name.")
            else:
                name_window.destroy()
                self.update_scoreboard()
                self.update_turn_label()

        tk.Label(name_window, text="Player X Name:", font=("Fixedsys", 14), bg="#e8f5e9").pack(pady=10)
        player_x_name_entry = tk.Entry(name_window, font=("Fixedsys", 14))
        player_x_name_entry.pack(pady=5)

        tk.Label(name_window, text="Player O Name:", font=("Fixedsys", 14), bg="#e8f5e9").pack(pady=10)
        player_o_name_entry = tk.Entry(name_window, font=("Fixedsys", 14))
        player_o_name_entry.pack(pady=5)

        tk.Button(name_window, text="Start Game", font=("Fixedsys", 14), command=save_names, bg="#2e7d32", fg="white").pack(pady=10)

        name_window.mainloop()

    # Exit Game button
    def exit_game(self):
        self.root.quit()

if __name__ == "__main__":
    TicTacToe()
