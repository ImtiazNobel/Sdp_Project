import tkinter as tk
from tkinter import messagebox
from screens.main_screen import MainScreen


class LoginScreen:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.display_login()

    def display_login(self):
        self.clear_frame()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def authenticate():
            username = username_entry.get()
            password = password_entry.get()

            if username == "admin" and password == "admin123":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                MainScreen(self.root, self.db, admin=True)
            else:
                self.db.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
                if self.db.cursor.fetchone():
                    messagebox.showinfo("Login Successful", f"Welcome, {username}!")
                    MainScreen(self.root, self.db, admin=False)
                else:
                    messagebox.showerror("Login Failed", "Invalid credentials!")

        def register():
            self.display_register()

        tk.Button(self.root, text="Login", command=authenticate).pack(pady=10)
        tk.Button(self.root, text="Register", command=register).pack(pady=5)

    def display_register(self):
        self.clear_frame()

        tk.Label(self.root, text="Register", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="New Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="New Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def register_user():
            username = username_entry.get()
            password = password_entry.get()

            if username and password:
                try:
                    self.db.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    self.db.connection.commit()
                    messagebox.showinfo("Success", "Registration successful!")
                    self.display_login()
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error", "Username already exists!")
            else:
                messagebox.showerror("Error", "Fields cannot be empty!")

        tk.Button(self.root, text="Register", command=register_user).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.display_login).pack()
