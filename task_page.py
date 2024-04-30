import tkinter as tk

class TaskWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")
        self.parent = parent

        # Create a label for the heading
        self.heading_label = tk.Label(self, text="Tasks", font=("Helvetica", 14, "bold"), bg="#ECF0F1")
        self.heading_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Create a text area to display pending tasks
        self.pending_tasks_text = tk.Text(self, height=10, width=50)
        self.pending_tasks_text.grid(row=1, column=0, padx=10, pady=5)

        # Insert sample pending tasks
        self.insert_sample_tasks()

    def insert_sample_tasks(self):
        sample_tasks = [
            "Complete project proposal",
            "Prepare presentation slides",
            "Send follow-up emails to clients"
        ]

        # Insert sample tasks into the text area
        for task in sample_tasks:
            self.pending_tasks_text.insert(tk.END, f"{task}\n")
