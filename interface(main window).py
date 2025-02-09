import subprocess
from tkinter import *

# Function to open a .py file
def open_script(script_name):
    try:
        subprocess.Popen(["python", script_name])
    except FileNotFoundError:
        messagebox.showerror("Error", f"File '{script_name}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = Tk()
root.title("Data Structure and Algorithms")
root.geometry("800x600")
root.configure(bg='#6185f8')

# Font setting
header_font = ("Fixedsys", 35)  # Larger font size for the header
button_font = ("Fixedsys", 17)  # Font for buttons
footer_font = ("Fixedsys", 8)   # Smaller font for footer

# Header Frame
header = Frame(root, bg='#683632', pady=33)
header.pack(fill=X)
header_label = Label(header, text="DATA STRUCTURE AND ALGORITHMS", font=header_font, bg='#683632', fg='#ffffff')
header_label.pack()

# Main Content Frame (centered dynamically)
main_frame = Frame(root, bg='#f8be10', pady=35, padx=35)  # Muted green for content area
main_frame.place(relx=0.5, rely=0.56, anchor=CENTER)

# Buttons for different applications with their associated script names
buttons = [
    ("Tic-Tac-Toe", "TicTacToe.py"),
    ("Binary Tree Traversal", "BinaryTreeTraversal.py"),
    ("Stacks Application", "stack.py"),
    ("Binary Search Tree", "BinarySearchTree.py"),
    ("Queue Application", "queueapp.py"),
    ("Towers of Hanoi", "TowersOfHanoi.py"),
    ("Sorting", "sortingg.py"),
]

# Create buttons with retro design
# Calculate rows and columns for centering
buttons_per_row = 2
row = 0
col = 0

for text, script_name in buttons[:-1]:  # Add all buttons except "Sorting"
    btn = Button(
        main_frame,
        text=text,
        width=30,  # Increased width
        height=3,  # Increased height
        font=button_font,
        bg='#306230',
        fg='#ffffff',
        activebackground='#e0102f',
        activeforeground='#e8f5e9',
        relief="flat",
        command=lambda script_name=script_name: open_script(script_name)
    )
    btn.grid(row=row, column=col, padx=15, pady=15)

    col += 1
    if col >= buttons_per_row:  # Move to the next row
        col = 0
        row += 1

# Add the "Sorting" button centered in the last row
sorting_button = Button(
    main_frame,
    text="Sorting",
    width=30,
    height=3,
    font=button_font,
    bg='#306230',
    fg='#ffffff',
    activebackground='#e0102f',
    activeforeground='#e8f5e9',
    relief="flat",
    command=lambda: open_script("sortingg.py")
)
sorting_button.grid(row=row + 1, column=0, columnspan=buttons_per_row, padx=15, pady=15, sticky="ew")

# Add padding to center content horizontally
for c in range(buttons_per_row):
    main_frame.columnconfigure(c, weight=1)

# Footer Section
footer = Frame(root, bg='#683632', pady=10)  # Adjusted footer padding
footer.pack(side=BOTTOM, fill=X)

# Footer Rights (Centered with smaller font)
Label(footer, text="\u00A9 2025 All Rights Reserved.", font=footer_font, bg='#683632', fg='#9bbc0f').pack()

# Start the application loop
root.mainloop()
