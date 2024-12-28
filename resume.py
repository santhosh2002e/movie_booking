import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import json
import random

class MovieBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Booking System")
        self.root.geometry("900x600")
        
        # Initialize data
        self.load_movie_data()
        self.selected_movie = None
        self.selected_date = None
        self.selected_time = None
        self.selected_seats = []
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create and show main menu
        self.create_main_menu()

    def load_movie_data(self):
        # Sample movie data - in real app, this would come from a database
        self.movies = {
            "Latest Releases": [
                {
                    "title": "The Avatar 3",
                    "rating": "4.5/5",
                    "duration": "2h 45m",
                    "genre": "Action, Sci-Fi",
                    "price": 250,
                    "image": "avatar.jpg",
                    "description": "Return to Pandora in this epic sci-fi adventure."
                },
                {
                    "title": "Fast X",
                    "rating": "4.2/5",
                    "duration": "2h 30m",
                    "genre": "Action, Thriller",
                    "price": 200,
                    "image": "fast_x.jpg",
                    "description": "The Fast saga continues with more action."
                }
            ],
            "Now Showing": [
                {
                    "title": "The Marvel's",
                    "rating": "4.3/5",
                    "duration": "2h 15m",
                    "genre": "Action, Adventure",
                    "price": 220,
                    "image": "marvels.jpg",
                    "description": "Epic superhero adventure."
                },
                {
                    "title": "Dune: Part Two",
                    "rating": "4.7/5",
                    "duration": "2h 40m",
                    "genre": "Sci-Fi, Adventure",
                    "price": 230,
                    "image": "dune.jpg",
                    "description": "The saga continues on Arrakis."
                }
            ],
            "Coming Soon": [
                {
                    "title": "Deadpool 3",
                    "rating": "N/A",
                    "duration": "2h 20m",
                    "genre": "Action, Comedy",
                    "price": 250,
                    "image": "deadpool.jpg",
                    "description": "The merc with a mouth returns."
                }
            ]
        }
        
        # Generate show times and seats
        self.show_times = ["10:00 AM", "1:30 PM", "4:30 PM", "7:30 PM", "10:30 PM"]
        self.seats = self.generate_seats()

    def generate_seats(self):
        seats = {}
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for movie in sum([movies for movies in self.movies.values()], []):
            seats[movie['title']] = {}
            for _ in range(7):  # Next 7 days
                date = (datetime.now() + timedelta(days=_)).strftime("%Y-%m-%d")
                seats[movie['title']][date] = {}
                for time in self.show_times:
                    seat_map = {}
                    for row in rows:
                        for seat_num in range(1, 11):
                            # Randomly mark some seats as booked
                            seat_map[f"{row}{seat_num}"] = random.choice([True, False])
                    seats[movie['title']][date][time] = seat_map
        return seats

    def create_main_menu(self):
        # Clear existing widgets
        for widget in self.main_container.winfo_children():
            widget.destroy()

        # Create header
        header = ttk.Label(self.main_container, text="Movie Booking System",
                          font=('Arial', 24, 'bold'))
        header.pack(pady=20)

        # Create tabs for different movie categories
        tab_control = ttk.Notebook(self.main_container)
        
        for category, movies in self.movies.items():
            tab = ttk.Frame(tab_control)
            tab_control.add(tab, text=category)
            
            # Create movie cards
            for idx, movie in enumerate(movies):
                self.create_movie_card(tab, movie, idx)
        
        tab_control.pack(expand=True, fill='both')

    def create_movie_card(self, parent, movie, idx):
        # Create frame for movie card
        card = ttk.Frame(parent, relief='solid')
        card.grid(row=idx//2, column=idx%2, padx=10, pady=10, sticky='nsew')
        
        # Movie title
        title = ttk.Label(card, text=movie['title'], font=('Arial', 16, 'bold'))
        title.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        # Movie details
        details = f"Rating: {movie['rating']} | Duration: {movie['duration']}\n"
        details += f"Genre: {movie['genre']}\nPrice: ₹{movie['price']}"
        ttk.Label(card, text=details).grid(row=1, column=0, padx=5, pady=5, sticky='w')
        
        # Book button
        ttk.Button(card, text="Book Now",
                  command=lambda m=movie: self.show_booking_page(m)).grid(
                      row=2, column=0, padx=5, pady=5)

    def show_booking_page(self, movie):
        self.selected_movie = movie
        
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()
            
        # Create booking interface
        ttk.Label(self.main_container, text=f"Booking: {movie['title']}",
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        # Date selection
        date_frame = ttk.Frame(self.main_container)
        date_frame.pack(pady=10)
        
        ttk.Label(date_frame, text="Select Date:").pack(side=tk.LEFT, padx=5)
        dates = [(datetime.now() + timedelta(days=x)).strftime("%Y-%m-%d")
                for x in range(7)]
        date_var = tk.StringVar()
        date_combo = ttk.Combobox(date_frame, textvariable=date_var,
                                values=dates, state='readonly')
        date_combo.pack(side=tk.LEFT, padx=5)
        date_combo.set(dates[0])
        
        # Time selection
        time_frame = ttk.Frame(self.main_container)
        time_frame.pack(pady=10)
        
        ttk.Label(time_frame, text="Select Time:").pack(side=tk.LEFT, padx=5)
        time_var = tk.StringVar()
        time_combo = ttk.Combobox(time_frame, textvariable=time_var,
                                values=self.show_times, state='readonly')
        time_combo.pack(side=tk.LEFT, padx=5)
        time_combo.set(self.show_times[0])
        
        # Button to proceed to seat selection
        ttk.Button(self.main_container, text="Select Seats",
                  command=lambda: self.show_seat_selection(
                      date_var.get(), time_var.get())).pack(pady=20)
        
        # Back button
        ttk.Button(self.main_container, text="Back to Movies",
                  command=self.create_main_menu).pack(pady=10)

    def show_seat_selection(self, date, time):
        self.selected_date = date
        self.selected_time = time
        
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()
            
        # Create seat selection interface
        ttk.Label(self.main_container,
                 text=f"Select Seats for {self.selected_movie['title']}",
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        # Show screen
        screen_label = ttk.Label(self.main_container, text="SCREEN",
                               background='lightgray', width=50)
        screen_label.pack(pady=20)
        
        # Create seat grid
        seat_frame = ttk.Frame(self.main_container)
        seat_frame.pack(pady=20)
        
        seats = self.seats[self.selected_movie['title']][date][time]
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            ttk.Label(seat_frame, text=row).grid(row=ord(row)-65, column=0, padx=5)
            for seat_num in range(1, 11):
                seat = f"{row}{seat_num}"
                btn = ttk.Button(seat_frame, text=seat_num,
                               command=lambda s=seat: self.toggle_seat(s))
                btn.grid(row=ord(row)-65, column=seat_num, padx=2, pady=2)
                if seats[seat]:  # If seat is booked
                    btn.state(['disabled'])
        
        # Selected seats and price
        self.selection_label = ttk.Label(self.main_container,
                                       text="Selected: None\nTotal: ₹0")
        self.selection_label.pack(pady=10)
        
        # Proceed to payment button
        self.book_button = ttk.Button(self.main_container, text="Proceed to Payment",
                                    command=self.process_booking, state='disabled')
        self.book_button.pack(pady=10)
        
        # Back button
        ttk.Button(self.main_container, text="Back to Show Selection",
                  command=lambda: self.show_booking_page(self.selected_movie)).pack(pady=10)

    def toggle_seat(self, seat):
        if seat in self.selected_seats:
            self.selected_seats.remove(seat)
        else:
            self.selected_seats.append(seat)
            
        # Update selection label and button state
        total_price = len(self.selected_seats) * self.selected_movie['price']
        self.selection_label.config(
            text=f"Selected: {', '.join(sorted(self.selected_seats))}\n"
                 f"Total: ₹{total_price}")
        
        self.book_button.state(['!disabled'] if self.selected_seats else ['disabled'])

    def process_booking(self):
        # In a real application, this would handle payment processing
        booking_details = {
            'movie': self.selected_movie['title'],
            'date': self.selected_date,
            'time': self.selected_time,
            'seats': self.selected_seats,
            'total': len(self.selected_seats) * self.selected_movie['price']
        }
        
        # Show booking confirmation
        message = f"Booking Confirmed!\n\n"
        message += f"Movie: {booking_details['movie']}\n"
        message += f"Date: {booking_details['date']}\n"
        message += f"Time: {booking_details['time']}\n"
        message += f"Seats: {', '.join(sorted(booking_details['seats']))}\n"
        message += f"Total: ₹{booking_details['total']}"
        
        messagebox.showinfo("Booking Successful", message)
        
        # Return to main menu
        self.selected_seats = []
        self.create_main_menu()

def main():
    root = tk.Tk()
    app = MovieBookingSystem(root)
    root.mainloop()


main()