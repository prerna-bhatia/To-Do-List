import tkinter as tk
from tkinter import ttk, messagebox
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List ✅")
        self.root.geometry("500x500")
        self.root.configure(bg="#735DA5")  # Light gray background
        
        self.tasks = []
        self.filename = "tasks.txt"
        self.load_tasks()

        # 🌟 Apply ttk theme
        self.style = ttk.Style()
        self.style.theme_use("clam")  # 'clam', 'alt', 'default', 'classic'

        # 🔹 Heading Label
        ttk.Label(root, text="📝 To-Do List", font=("Times new roman", 18, "bold"), background="#f4f4f4").pack(pady=10)

        # 🔹 Entry Field for Task Input
        self.task_entry = ttk.Entry(root, width=50, font=("Arial", 14))
        self.task_entry.pack(pady=20)

        # 🔹 Button Frame
        button_frame = tk.Frame(root, bg="#D3C5E5")
        button_frame.pack(pady=5)

        # 🔹 Add Task Button
        self.add_btn = ttk.Button(button_frame, text="➕ Add Task", command=self.add_task, style="Accent.TButton")
        self.add_btn.grid(row=0, column=0, padx=5)

        # 🔹 Mark Done Button
        self.done_btn = ttk.Button(button_frame, text="✔️ Mark as Done", command=self.mark_done, style="Accent.TButton")
        self.done_btn.grid(row=0, column=1, padx=5)

        # 🔹 Remove Task Button
        self.remove_btn = ttk.Button(button_frame, text="🗑️ Remove Task", command=self.remove_task, style="Accent.TButton")
        self.remove_btn.grid(row=0, column=2, padx=5)

        # 🔹 Task List (Listbox with Scrollbar)
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.task_listbox = tk.Listbox(frame, width=50, height=10, font=("Arial", 12), bg="white", fg="black")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # 🔹 Update Task List
        self.update_listbox()

    # 🛠 Add Task Function
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.save_tasks()
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    # 🛠 Mark Task as Done
    def mark_done(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["done"] = True
            self.save_tasks()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as done!")

    #Remove Task Function
    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.save_tasks()
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to remove!")

    # Update Task List UI
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✔️ Done" if task["done"] else "❌ Pending"
            self.task_listbox.insert(tk.END, f"{index}. {task['task']} - {status}")

    # Save Tasks to File
    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                status = "Done" if task["done"] else "Pending"
                file.write(f"{task['task']} | {status}\n")

    # 🛠 Load Tasks from File
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    task, status = line.strip().split(" | ")
                    self.tasks.append({"task": task, "done": status == "Done"})

    

# Run Application
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
