import tkinter as tk
from tkcalendar import Calendar


class CalendarPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")
        self.parent = parent

        # Create a calendar widget
        cal = Calendar(self, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
