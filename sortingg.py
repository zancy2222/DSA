import tkinter as tk
from tkinter import messagebox
import random
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms Visualizer")
        self.root.geometry("1000x600")
        self.root.resizable(True, True)
        self.data = []

        # Canvas for visualization
        self.canvas = tk.Canvas(self.root, width=1000, height=400, bg="white")
        self.canvas.place(relx=0.5, rely=0.3, anchor="center")

        # Control frame
        self.control_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.control_frame.place(relx=0.5, rely=0.8, anchor="center")

        # Entry for data
        self.entry = tk.Entry(self.control_frame, width=60, font=("Fixedsys", 14))
        self.entry.grid(row=0, column=0, padx=10, pady=5)

        # Button for random data generation
        tk.Button(self.control_frame, text="Generate Random Data", command=self.generate_data, bg="#306230", fg="white", font=("Fixedsys", 12), height=2).grid(row=0, column=1, padx=10, pady=5)

        # Dropdown menu for algorithm selection
        self.algorithm_selection = tk.StringVar(value="Bubble")
        tk.OptionMenu(self.control_frame, self.algorithm_selection, "Bubble", "Insertion", "Selection", "Merge", "Shell", "Quick", "Heap").grid(row=0, column=2, padx=10, pady=5)

        # Button to start sorting
        tk.Button(self.control_frame, text="Start Sorting", command=self.start_sorting, bg="#6185f8", fg="white", font=("Fixedsys", 12), height=2).grid(row=1, column=1, padx=10, pady=5)

    def generate_data(self):
        """Generates random integers and populates the entry field."""
        self.data = [random.randint(1, 100) for _ in range(30)]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, " ".join(map(str, self.data)))

    def start_sorting(self):
        """Starts the sorting process after validating input."""
        try:
            self.data = list(map(int, self.entry.get().strip().split()))
            if len(self.data) != 30:
                raise ValueError("You must enter exactly 30 integers.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        algorithm = self.algorithm_selection.get()
        if algorithm == "Bubble":
            self.bubble_sort()
        elif algorithm == "Insertion":
            self.insertion_sort()
        elif algorithm == "Selection":
            self.selection_sort()
        elif algorithm == "Merge":
            self.merge_sort(0, len(self.data) - 1)
        elif algorithm == "Shell":
            self.shell_sort()
        elif algorithm == "Quick":
            self.quick_sort(0, len(self.data) - 1)
        elif algorithm == "Heap":
            self.heap_sort()

    def draw_data(self, color="#683632"):
        """Displays the data as book spines on the canvas with labels above each spine."""
        self.canvas.delete("all")
        canvas_height = 411
        canvas_width = 1000
        spine_width = canvas_width / len(self.data)

        for i, value in enumerate(self.data):
            x0 = i * spine_width
            y0 = canvas_height - value * 4
            x1 = (i + 1) * spine_width
            y1 = canvas_height

            # Draw the "book spine" for the element
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

            # Draw the label above the "book spine"
            self.canvas.create_text((x0 + x1) / 2, y0 - 10, text=str(value), font=("Fixedsys", 8), fill="black")

        self.root.update_idletasks()

    def bubble_sort(self):
        """Bubble Sort implementation."""
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data(color="#683632")
                    time.sleep(0.1)
        self.draw_data(color="#683632")

    def insertion_sort(self):
        """Insertion Sort implementation."""
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
                self.draw_data(color="#683632")
                time.sleep(0.1)
            self.data[j + 1] = key
        self.draw_data(color="#683632")

    def selection_sort(self):
        """Selection Sort implementation."""
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_data(color="#683632")
            time.sleep(0.1)
        self.draw_data(color="#683632")

    def merge_sort(self, left, right):
        """Merge Sort implementation."""
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        left_copy = self.data[left:mid + 1]
        right_copy = self.data[mid + 1:right + 1]

        l = r = 0
        for i in range(left, right + 1):
            if l < len(left_copy) and (r >= len(right_copy) or left_copy[l] <= right_copy[r]):
                self.data[i] = left_copy[l]
                l += 1
            else:
                self.data[i] = right_copy[r]
                r += 1
            self.draw_data(color="#683632")
            time.sleep(0.1)

    def shell_sort(self):
        """Shell Sort implementation."""
        gap = len(self.data) // 2
        while gap > 0:
            for i in range(gap, len(self.data)):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j - gap] > temp:
                    self.data[j] = self.data[j - gap]
                    j -= gap
                    self.draw_data(color="#683632")
                    time.sleep(0.1)
                self.data[j] = temp
            gap //= 2
        self.draw_data(color="#683632")

    def quick_sort(self, low, high):
        """Quick Sort implementation."""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] < pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.draw_data(color="#683632")
                time.sleep(0.1)
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        return i + 1

    def heap_sort(self):
        """Heap Sort implementation."""
        n = len(self.data)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0)
            self.draw_data(color="#683632")
            time.sleep(0.1)
        self.draw_data(color="#683632")

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.data[left] > self.data[largest]:
            largest = left
        if right < n and self.data[right] > self.data[largest]:
            largest = right

        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(n, largest)


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
