import tkinter as tk
from tkinter import messagebox
import random


class Node:
    """Class for a BST node."""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Tree")
        self.root.geometry("1000x800")
        self.root.configure(bg="#683632")  # Light yellow background for the main window

        # Control frame
        frame = tk.Frame(self.root, bg="#683632")
        frame.pack(pady=20)

        tk.Label(
            frame, text="Enter integers (max 30):",
            bg="#683632", fg="white", font=("Fixedsys", 9)  # Removed "bold"
        ).grid(row=0, column=0, padx=5, pady=0)

        self.input_entry = tk.Entry(frame, width=40, bg="#FFFBCC", font=("Fixedsys", 14))
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            frame, text="Generate BST", command=self.generate_bst,
            bg="#FFD54F", fg="#5B5B5B", font=("Fixedsys", 9),  # Removed "bold"
            activebackground="#FFE082"
        ).grid(row=0, column=2, padx=5, pady=0)

        tk.Button(
            frame, text="Generate 30 Random Integers", command=self.generate_random_integers,
            bg="#FFD54F", fg="#5B5B5B", font=("Fixedsys", 9),  # Removed "bold"
            activebackground="#FFE082"
        ).grid(row=1, column=0, columnspan=3, pady=0)

        # Canvas for drawing the tree
        self.canvas = tk.Canvas(self.root, bg="#FFFBCC", width=1500, height=600)
        self.canvas.pack(pady=0)

        # Binary tree data
        self.bst_root = None

        # Footer Frame (for BST and Traversals)
        footer_frame = tk.Frame(self.root, bg="#683632")
        footer_frame.pack(side="bottom", fill="x", pady=2)

        self.tree_label = tk.Label(
            footer_frame, text="BST: None", wraplength=1300, justify="left",
            bg="#f8be10", fg="#683632", font=("Fixedsys", 5)
        )
        self.tree_label.pack(pady=5)

        self.traversal_label = tk.Label(
            footer_frame, text="Traversals: None", wraplength=1300, justify="left",
            bg="#f8be10", fg="#683632", font=("Fixedsys", 5)
        )
        self.traversal_label.pack(pady=5)

    def insert(self, root, key):
        """Insert a node into the BST."""
        if root is None:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def generate_bst(self):
        try:
            data = list(map(int, self.input_entry.get().strip().split()))
            if len(data) > 30:
                raise ValueError("Maximum of 30 integers allowed.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Clear canvas
        self.canvas.delete("all")

        # Create the BST
        self.bst_root = None
        for num in data:
            self.bst_root = self.insert(self.bst_root, num)

        self.tree_label.config(text=f"BST Root: {data}")
        self.display_traversals()
        self.draw_tree(self.bst_root, 500, 50, 200)

    def generate_random_integers(self):
        """Generate 30 random integers and populate the BST."""
        random_data = random.sample(range(1, 99), 30)
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, " ".join(map(str, random_data)))
        self.generate_bst()

    def lrt(self, root):
        """Post-order (LRT) traversal."""
        return self.lrt(root.left) + self.lrt(root.right) + [root.val] if root else []

    def tlr(self, root):
        """Pre-order (TLR) traversal."""
        return [root.val] + self.tlr(root.left) + self.tlr(root.right) if root else []

    def ltr(self, root):
        """In-order (LTR) traversal."""
        return self.ltr(root.left) + [root.val] + self.ltr(root.right) if root else []

    def display_traversals(self):
        lrt_result = self.lrt(self.bst_root)
        tlr_result = self.tlr(self.bst_root)
        ltr_result = self.ltr(self.bst_root)
        self.traversal_label.config(
            text=f"LRT (Post-order): {lrt_result}\nTLR (Pre-order): {tlr_result}\nLTR (In-order): {ltr_result}"
        )

    def get_depth(self, node):
        """Get the depth of the tree."""
        if node is None:
            return 0
        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        return max(left_depth, right_depth) + 1

    def draw_tree(self, node, x, y, x_offset, level=0):
        """Draw the binary tree on the canvas with dynamic spacing and small nodes."""
        if node:
            # Calculate dynamic size and spacing based on the tree depth
            tree_depth = self.get_depth(self.bst_root)
            dynamic_x_offset = max(30, 250 // tree_depth)  # Smaller horizontal offset for compactness
            dynamic_vertical_spacing = max(90, 120 - (tree_depth * 5))  # Smaller vertical spacing

            # Draw the node with dynamically adjusted size
            node_size = 12
            self.canvas.create_oval(
                x - node_size, y - node_size, x + node_size, y + node_size,
                fill="#FFE082", outline="#FFC107"
            )
            self.canvas.create_text(
                x, y, text=str(node.val), fill="#5B5B5B", font=("Fixedsys", 12)
            )

            # Adjust spacing to avoid overcrowding
            x_offset = max(x_offset, dynamic_x_offset)
            vertical_spacing = dynamic_vertical_spacing

            # Avoid overlap by adding space between branches
            if node.left:
                # Draw line to the left child with adjusted offset
                left_x = x - x_offset
                left_y = y + vertical_spacing
                self.canvas.create_line(
                    x, y + node_size, left_x, left_y - node_size,
                    fill="#FFC107", width=2
                )
                self.draw_tree(node.left, left_x, left_y, x_offset // 1.5, level + 1)

            if node.right:
                # Draw line to the right child with adjusted offset
                right_x = x + x_offset
                right_y = y + vertical_spacing
                self.canvas.create_line(
                    x, y + node_size, right_x, right_y - node_size,
                    fill="#FFC107", width=2
                )
                self.draw_tree(node.right, right_x, right_y, x_offset // 1.5, level + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = BinarySearchTree(root)
    root.mainloop()