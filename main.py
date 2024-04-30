import tkinter as tk
from tkinter import ttk
from tab_section import create_tab_section
from customer_graph_page import CustGraphPage
from calendar_page import CalendarPage
from deal_graph_page import DealGraphPage
from task_page import TaskWidget

def main():
    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Klaasse CRM")
    root.iconphoto(False, tk.PhotoImage(file="D:/Software development/CRM/logo.png"))  # Change to your company logo path

    # Set window size and position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_geometry = f"{screen_width}x{screen_height}+0+0"
    root.geometry(window_geometry)
    print("Window geometry:", window_geometry)  # Print window geometry

    # Create a modern and sleek theme for the application
    root.configure(bg="#F8F9FA")  # Set a light background color
    style = ttk.Style()
    style.theme_use("default")  # Use the default system theme

    # Create tab section with modern styling
    create_tab_section(root)

    # Add the Customer GraphPage with a modern design
    customer_graph_page = CustGraphPage(root)
    customer_graph_page.grid(row=1, column=0, sticky="nsew")

    # Add the CalendarPage with a modern design
    calendar_page = CalendarPage(root)
    calendar_page.grid(row=1, column=1, sticky="nsew")

    # Add the Deal GraphPage with a modern design
    deal_graph_page = DealGraphPage(root)
    deal_graph_page.grid(row=2, column=0, sticky="nsew")

    # Create and add the task widget with a modern design
    task_widget = TaskWidget(root)
    task_widget.grid(row=2, column=1, sticky="nsew")

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
