import tkinter as tk
from tkinter import messagebox

class MovieTheaterPOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Theater POS System")
        self.root.geometry("500x400")

        # Movie list and pricing
        self.movies = {
            "Avatar 2": 8.75,
            "Spider-Man: No Way Home": 8.75,
            "The Batman": 8.75,
            "Minions: Rise of Gru": 8.75,
            "Top Gun: Maverick": 8.75,
            "Jurassic World Dominion": 8.75,
            "Black Panther: Wakanda Forever": 8.75,
            "Thor: Love and Thunder": 8.75,
            "Doctor Strange in the Multiverse of Madness": 8.75,
            "Puss in Boots: The Last Wish": 8.75
        }
        
        # Variables
        self.selectedMovie = tk.StringVar()
        self.ticketQuantity = tk.IntVar(value=1)
        self.totalPrice = tk.DoubleVar(value=0.0)

        self.create_widgets()

    def create_widgets(self):
        # Movie Selection
        movieLabel = tk.Label(self.root, text="Select Movie:")
        movieLabel.pack(pady=10)
        
        movieMenu = tk.OptionMenu(self.root, self.selectedMovie, *self.movies.keys())
        self.selectedMovie.set("Select Movie")
        movieMenu.pack(pady=10)

        # Ticket Quantity
        ticketLabel = tk.Label(self.root, text="Number of Tickets:")
        ticketLabel.pack(pady=10)

        ticketQuantityEntry = tk.Entry(self.root, textvariable=self.ticketQuantity)
        ticketQuantityEntry.pack(pady=5)
        
        # Calculate Total Button
        calcButton = tk.Button(self.root, text="Calculate Total", command=self.calculate_total)
        calcButton.pack(pady=20)

        # Total Price Display
        totalLabel = tk.Label(self.root, text="Total Price:")
        totalLabel.pack(pady=10)

        totalDisplay = tk.Label(self.root, textvariable=self.totalPrice)
        totalDisplay.pack(pady=10)

        # Purchase Button
        purchaseButton = tk.Button(self.root, text="Make Purchase", command=self.make_purchase)
        purchaseButton.pack(pady=20)

    def calculate_total(self):
        # Get selected movie and ticket quantity
        selectedMovie = self.selectedMovie.get()
        ticketQuantity = self.ticketQuantity.get()

        if selectedMovie == "Select Movie":
            messagebox.showerror("Error", "Please select a movie.")
            return

        if ticketQuantity <= 0:
            messagebox.showerror("Error", "Please enter a valid ticket quantity.")
            return

        # Calculate total price
        moviePrice = self.movies[selectedMovie]
        total = moviePrice * ticketQuantity
        self.totalPrice.set(f"${total:.2f}")

    def make_purchase(self):
        # Final purchase
        total = self.totalPrice.get()
        
        if total <= 0:
            messagebox.showerror("Error", "Please calculate the total before making a purchase.")
            return

        messagebox.showinfo("Success", f"Purchase successful! Total amount: {total}")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    posSystem = MovieTheaterPOS(root)
    root.mainloop()