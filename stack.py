from tkinter import *
from tkinter import messagebox

class Garage:
    def __init__ (self):
        self.capacity = 10
        self.stack = []
        self.arrival_count = 0
        self.departure_count = 0

    # Adding arriving cars in the stack
    def park_car(self, plate_number):
        self.arrival_count
        if len(self.stack) < self.capacity:
            self.stack.append(plate_number)
            self.arrival_count += 1
            return True
        return False
    
    # Utilizing LIFO function of stack for departure
    def depart_car(self, plate_number):
        self.departure_count
        if plate_number in self.stack:
            self.temp_stack = []     # Temporary stack where cars will be placed when a car below them will depart
            while self.stack[-1] != plate_number:
                self.temp_stack.append(self.stack.pop())
            self.stack.pop()  # Remove the target car
            self.departure_count += 1
            # Return the other cars back to the stack
            while self.temp_stack:
                self.stack.append(self.temp_stack.pop())
            return True
        return False
    
class ParkingApp:
    def __init__ (self, root):
        self.garage = Garage()
        self.root = root
        self.root.title("Stacks Application")
        self.root.geometry("500x400")
        self.root.configure(bg='#f8be10')

        # Entry of plate numbers
        self.entry_label = Label (self.root, text="Enter Car Plate Number:", font=("Fixedsys", 17), bg='#f8be10', fg='#ffffff')
        self.entry_label.grid(row=0, column=0, padx=10)

        self.plate_entry = Entry (self.root, font=("Fixedsys", 15))
        self.plate_entry.grid(row=0, column=1, padx=25)

        # Arrival
        self.arrival_button = Button (self.root, text="Arrival", 
                         font=("Fixedsys", 9), 
                         width=15, height=2,
                         bg='#306230', fg='#ffffff',
                         activebackground='#e0102f',
                         activeforeground='#e8f5e9', 
                         relief="flat", command=self.handle_arrival
                         )
        self.arrival_button.grid(row=1, column=0, pady=8)

        # Departure
        self.depart_button = Button (self.root, text="Departure", 
                        font=("Fixedsys", 9), 
                        width=15, height=2, 
                        bg='#306230', fg='#ffffff',
                        activebackground='#e0102f',
                        activeforeground='#e8f5e9',
                        relief="flat", command=self.handle_departure
                        )
        self.depart_button.grid(row=1, column=1, pady=8)

        self.status_label = Label (self.root, text="Parking Garage Status", font=("Fixedsys", 19), bg='#f8be10')
        self.status_label.grid(row=2, pady=10, columnspan=2)

        # List of cars arrived in the garage will be displayed here
        self.status_display = Text(self.root, height=10, width=55, state="disabled", font="Fixedsys")
        self.status_display.grid(row=3, columnspan=2)

        # Display the number of cars arrived and departed from the garage
        self.counter = Label (self.root, text="Arrivals: 0 | Departures: 0", font=("Fixedsys", 8), bg='#f8be10', fg='#ffffff')
        self.counter.grid(row=4, columnspan=2, pady=5)

        self.exit_button = Button (self.root, text='Exit Application',
                    font=("Fixedsys", 9), 
                    width=15, height=2, 
                    bg='#306230', fg='#ffffff',
                    activebackground='#e0102f',
                    activeforeground='#e8f5e9',
                    relief="flat", command=self.exit_app
                    )
        self.exit_button.grid(row=5, columnspan=2, pady=5, ipadx=5)

    def handle_arrival(self):
        plate_number = self.plate_entry.get().strip()
        if plate_number:
            if self.garage.park_car(plate_number):
                messagebox.showinfo("Success", f"Car {plate_number} parked successfully.")
            else:
                messagebox.showerror("Error", "Garage is full!")
        else:
            messagebox.showerror("Error", "Please enter a valid plate number.")
        self.update_display()

    def handle_departure(self):
        plate_number = self.plate_entry.get().strip()
        if plate_number:
            if self.garage.depart_car(plate_number):
                messagebox.showinfo("Success", f"Car {plate_number} departed successfully.")
            else:
                messagebox.showerror("Error", f"Car {plate_number} is not in the garage.")
        else:
            messagebox.showerror("Error", "Please enter a valid plate number.")
        self.update_display()

    def update_display(self):
        # Update the garage status display
        self.status_display.config(state="normal")
        self.status_display.delete(1.0, END)
        self.status_display.insert(END, "Cars in Garage:\n")
        for car in reversed(self.garage.stack):
            self.status_display.insert(END, f"{car}\n")
        self.status_display.config(state="disabled")

        # Update counters
        self.counter.config(
            text=f"Arrivals: {self.garage.arrival_count} | Departures: {self.garage.departure_count}"
        )

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = ParkingApp(root)
    root.mainloop()