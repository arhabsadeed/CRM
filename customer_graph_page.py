import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class CustGraphPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")
        self.parent = parent

        # Sample data
        customers = ['Customer A', 'Customer B', 'Customer C', 'Customer D', 'Customer E']
        num_customers = [20, 35, 30, 25, 40]

        # Create a bar graph
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(customers, num_customers, color='skyblue')
        ax.set_xlabel('Customers')
        ax.set_ylabel('Number of Customers')
        ax.set_title('Number of Customers')
        ax.tick_params(axis='x', rotation=45)
        fig.tight_layout()

        # Convert the matplotlib figure to a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # Display the graph on the frame
        canvas.get_tk_widget().pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
