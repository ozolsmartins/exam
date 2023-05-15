import tkinter as tk
from datetime import datetime, timedelta
class AgeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Age Calculator")
        self.label = tk.Label(master, text="Enter your birthdate (yyyy-mm-dd):")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.year_button = tk.Button(master, text="Years Lived", command=self.show_years)
        self.year_button.pack()
        self.second_button = tk.Button(master, text="Seconds Lived", command=self.show_seconds)
        self.second_button.pack()
        self.hour_button = tk.Button(master, text="Hours Lived", command=self.show_hours)
        self.hour_button.pack()
        self.age_label = tk.Label(master, text="")
        self.age_label.pack()
    def show_years(self):
        birthdate = datetime.strptime(self.entry.get(), "%Y-%m-%d")
        age = (datetime.now() - birthdate) // timedelta(days=365.2425)
        self.age_label.config(text=f"You are {age} years old.")
    def show_seconds(self):
        birthdate = datetime.strptime(self.entry.get(), "%Y-%m-%d")
        age = (datetime.now() - birthdate).total_seconds()
        self.age_label.config(text=f"You have lived for {age:,} seconds.")
    def show_hours(self):
        birthdate = datetime.strptime(self.entry.get(), "%Y-%m-%d")
        age = (datetime.now() - birthdate).total_seconds() / 3600
        self.age_label.config(text=f"You have lived for {age:.2f} hours.")

root = tk.Tk()
my_gui = AgeCalculator(root)
root.mainloop()

