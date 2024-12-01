import tkinter as tk
from database import Database
from screens.login_screen import LoginScreen


class MovieBookingApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Movie Ticket Booking System")
        self.db = Database()  # Database connection setup
        LoginScreen(self.root, self.db)  # Start with the login screen

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MovieBookingApp()
    app.run()
