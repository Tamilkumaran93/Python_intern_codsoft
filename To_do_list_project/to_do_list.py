import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.config(bg="#2C3E50")

        self.tasks = []

        self.frame = tk.Frame(self.root, bg="#2C3E50")
        self.frame.pack(pady=10)

        self.tasks_frame = tk.Frame(self.frame, bg="#34495E")
        self.tasks_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.on_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.entry_task = tk.Entry(self.root, width=50, font=('Arial', 14), bg="#ECF0F1", fg="#2C3E50")
        self.entry_task.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#1ABC9C", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#16A085")
        self.add_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Selected Tasks", command=self.delete_selected_tasks, bg="#E74C3C", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#C0392B")
        self.delete_task_button.pack(pady=5)

    def on_scroll(self, *args):
        for widget in self.tasks_frame.winfo_children():
            widget.yview(*args)

    def add_task(self):
        task = self.entry_task.get()
        if task != "":
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.tasks_frame, text=task, variable=var, onvalue=True, offvalue=False, bg="#34495E", fg="#ECF0F1", selectcolor="#2C3E50", font=('Arial', 12), activebackground="#34495E", command=lambda: self.remove_task(task, var, cb))
            cb.pack(anchor='w', pady=2)
            self.tasks.append((task, var, cb))
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
        self.update_scroll_region()

    def delete_selected_tasks(self):
        for task, var, cb in self.tasks[:]:
            if var.get():
                cb.destroy()
                self.tasks.remove((task, var, cb))
        self.update_scroll_region()

    def remove_task(self, task, var, cb):
        if var.get():
            cb.destroy()
            self.tasks.remove((task, var, cb))
            self.update_scroll_region()

    def update_scroll_region(self):
        self.tasks_frame.update_idletasks()
        self.tasks_frame.config(scrollregion=self.tasks_frame.bbox())

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()



