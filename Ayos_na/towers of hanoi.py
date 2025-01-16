import tkinter as tk
from tkinter import messagebox


class TowersOfHanoi:
    def __init__(self, root):
        self.root = root
        self.root.title("Towers of Hanoi")
        self.root.geometry("1000x700")  # Increased size
        self.root.resizable(True, True)

        # Set default font to Fixedsys with size 14
        self.root.option_add("*Font", "Fixedsys 14")

        # Main frame to center everything vertically and horizontally
        main_frame = tk.Frame(self.root, bg="#f8be10")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Canvas for visualizing towers and disks
        self.canvas = tk.Canvas(main_frame, width=1000, height=580, bg="#f8be10", highlightthickness=0)  # Larger canvas
        self.canvas.pack()

        # Control buttons frame (for tower selection buttons)
        control_frame = tk.Frame(main_frame, bg="#f8be10")
        control_frame.pack(pady=0)

        # Tower selection buttons with larger size
        self.tower_buttons = []
        for i in range(3):
            button = tk.Button(
                control_frame, text=f"Tower {i + 1}", command=lambda i=i: self.select_tower(i), bg="#306230", fg="white", width=12, height=2  # Larger buttons
            )
            button.grid(row=0, column=i, padx=20)
            self.tower_buttons.append(button)

        # Reset button with larger size
        self.reset_button = tk.Button(main_frame, text="Reset", command=self.reset, bg="#e0102f", fg="white", width=12, height=2)  # Larger reset button
        self.reset_button.pack(pady=20)

        # Initialize game state
        self.towers = [[], [], []]
        self.move_count = 0
        self.num_disks = 5
        self.selected_tower = None
        self.create_disks(self.num_disks)
        self.draw_towers()

    def create_disks(self, num_disks):
        """Create disks on the first tower."""
        self.towers[0] = list(range(1, num_disks + 1))  # Reverse the order (smaller on top)

    def draw_towers(self):
        """Draw the towers and disks."""
        self.canvas.delete("all")

        # Draw poles (larger separation between them)
        for i in range(3):
            x = 250 + i * 250  # Increased separation between towers
            self.canvas.create_line(x, 150, x, 550, width=7, fill="#306230")  # Thicker poles

        # Draw disks (larger disks)
        for tower_index, tower in enumerate(self.towers):
            x_center = 250 + tower_index * 250
            for level, disk in enumerate(tower):
                width = disk * 30  # Larger disks
                y = 550 - (len(tower) - level - 1) * 30  # Adjusted height for reversed disks
                self.canvas.create_rectangle(
                    x_center - width, y - 30, x_center + width, y, fill="#98FB98", outline="black"
                )

        self.canvas.update()

    def select_tower(self, tower_index):
        """Handle tower selection for moving disks."""
        if self.selected_tower is None:
            # Select source tower
            if self.towers[tower_index]:
                self.selected_tower = tower_index
                self.tower_buttons[tower_index].config(bg="#683632")
            else:
                messagebox.showwarning("Invalid Move", "Selected tower is empty.")
        else:
            # Select target tower and perform move
            if tower_index == self.selected_tower:
                messagebox.showwarning("Invalid Move", "Cannot move to the same tower.")
            elif not self.towers[tower_index] or self.towers[self.selected_tower][0] < self.towers[tower_index][0]:
                self.move_disk(self.selected_tower, tower_index)
            else:
                messagebox.showwarning("Invalid Move", "Cannot place larger disk on top of a smaller disk.")

            # Reset selection
            if self.selected_tower is not None:
                self.tower_buttons[self.selected_tower].config(bg="#306230")
            self.selected_tower = None

    def move_disk(self, source, target):
        """Move a disk from source tower to target tower."""
        self.towers[target].insert(0, self.towers[source].pop(0))  # Move the topmost disk
        self.move_count += 1
        self.draw_towers()

        # Check for win condition
        if len(self.towers[2]) == self.num_disks:
            messagebox.showinfo("Towers of Hanoi", f"You completed the game in {self.move_count} moves!")

    def reset(self):
        """Reset the game state."""
        self.towers = [[], [], []]
        self.create_disks(self.num_disks)
        self.move_count = 0
        self.selected_tower = None
        self.draw_towers()
        for button in self.tower_buttons:
            button.config(bg="#306230")


if __name__ == "__main__":
    root = tk.Tk()
    app = TowersOfHanoi(root)
    root.mainloop()
