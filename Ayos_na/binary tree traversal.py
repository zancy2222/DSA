import tkinter as tk
from tkinter import messagebox


class BinaryTreeTraversal:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Tree Traversal")
        self.root.geometry("1200x1000")
        self.root.config(bg="#683632")

        # Main frame to center all elements
        main_frame = tk.Frame(self.root, bg="#f8be10", width=1100, height=700)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Input frame for entry and button
        input_frame = tk.Frame(main_frame, bg="#306230")
        input_frame.grid(row=0, column=0, pady=10)

        tk.Label(
            input_frame,
            text="Enter number of levels (1 to 5):",
            bg="#306230",
            fg="white",
            font=("Fixedsys", 15)
        ).grid(row=0, column=0, padx=5, pady=5)

        self.levels_entry = tk.Entry(input_frame, width=10, bg="#EDE6D6", fg="black", font=("Fixedsys", 15))
        self.levels_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            input_frame,
            text="Generate Tree",
            command=self.generate_tree,
            bg="#e0102f",
            fg="white",
            font=("Fixedsys", 15)
        ).grid(row=0, column=2, padx=5, pady=5)

        # Canvas for tree drawing
        self.canvas = tk.Canvas(main_frame, width=1050, height=500, bg="#EDE6D6")
        self.canvas.grid(row=1, column=0, pady=10)

        # Label for traversal results
        self.traversal_label = tk.Label(
            main_frame,
            text="Traversals: None",
            wraplength=1000,
            justify="center",
            bg="#306230",
            fg="white",
            font=("Fixedsys", 15)
        )
        self.traversal_label.grid(row=2, column=0, pady=10)

        self.tree = []

    def generate_tree(self):
        try:
            input_value = self.levels_entry.get()
            if not input_value.isdigit():
                raise ValueError("Input only Integers.")
            levels = int(input_value)
            if not (1 <= levels <= 5):
                raise ValueError("Levels must be between 1 and 5.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Generate the tree
        self.tree = [i + 1 for i in range(2 ** levels - 1)]
        self.draw_tree(levels)
        self.display_traversals()

    def draw_tree(self, levels):
        """Draw the binary tree on the canvas."""
        self.canvas.delete("all")

        canvas_width = 1050
        canvas_height = 500
        node_radius = 20
        level_height = canvas_height // (levels + 1)

        positions = {}  # Store positions of nodes for line connections

        def draw_node(x, y, value):
            """Draw a single node at (x, y) with the given value."""
            self.canvas.create_oval(
                x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="#683632"
            )
            self.canvas.create_text(x, y, text=str(value), font=("Fixedsys", 15), fill="white")

        for level in range(levels):
            num_nodes = 2 ** level
            y = (level + 1) * level_height
            x_spacing = canvas_width // (2 ** level + 1)

            for i in range(num_nodes):
                x = (i + 1) * x_spacing
                index = (2 ** level - 1) + i

                # Draw the current node
                draw_node(x, y, self.tree[index])
                positions[index] = (x, y)

        # Draw connections between nodes
        for index, (x, y) in positions.items():
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child in positions:
                x_left, y_left = positions[left_child]
                self.canvas.create_line(
                    x, y + node_radius, x_left, y_left - node_radius, fill="#683632", width=2
                )

            if right_child in positions:
                x_right, y_right = positions[right_child]
                self.canvas.create_line(
                    x, y + node_radius, x_right, y_right - node_radius, fill="#683632", width=2
                )

    def lrt(self, index):
        """Post-order (LRT) traversal."""
        if index >= len(self.tree):
            return []
        left = self.lrt(2 * index + 1)
        right = self.lrt(2 * index + 2)
        return left + right + [self.tree[index]]

    def tlr(self, index):
        """Pre-order (TLR) traversal."""
        if index >= len(self.tree):
            return []
        left = self.tlr(2 * index + 1)
        right = self.tlr(2 * index + 2)
        return [self.tree[index]] + left + right

    def ltr(self, index):
        """In-order (LTR) traversal."""
        if index >= len(self.tree):
            return []
        left = self.ltr(2 * index + 1)
        right = self.ltr(2 * index + 2)
        return left + [self.tree[index]] + right

    def display_traversals(self):
        lrt_result = self.lrt(0)
        tlr_result = self.tlr(0)
        ltr_result = self.ltr(0)
        self.traversal_label.config(
            text=f"LRT (Post-order): {lrt_result}\nTLR (Pre-order): {tlr_result}\nLTR (In-order): {ltr_result}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryTreeTraversal(root)
    root.mainloop()
