import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__ (self, create):
        self.create = create
        self.create.title("Listify Smart Schedule")
        self.tasks = []

        self.create_account_frame = tk.Frame(self.create)
        self.login_frame = tk.Frame(self.create)
        self.main_gui_frame = tk.Frame(self.create)

        self.create_account_widgets()
        self.login_widgets()
        self.main_gui_widgets()

        self.create_account_frame.grid(row=0, column=0)

    def create_account_widgets(self):
        tk.Label(self.create_account_frame, text="Create your Email: ").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.create_user = tk.Entry(self.create_account_frame)
        self.create_user.grid(row=0, column=0, padx=30, pady=5, sticky="w")

        tk.Label(self.create_account_frame, text="Create your PIN: ").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.create_pin = tk.Entry(self.create_account_frame, show="*")
        self.create_pin.grid(row=1, column=0, padx=30, pady=5, sticky="w")

        tk.Button(self.create_account_frame, text="Create", command = self.create_account).grid(row=3, column=0, padx=20, pady=5, sticky="w")


    def login_widgets(self):
        tk.Label(self.login_frame, text="Enter your Email: ").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.login_user = tk.Entry(self.login_frame)
        self.login_user.grid(row=0, column=0, padx=20, pady=5, sticky="w")

        tk.Label(self.login_frame, text="Enter your PIN: ").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.login_pin = tk.Entry(self.login_frame, show="*")
        self.login_pin.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, padx=20, pady=5, sticky="w")

    def main_gui_widgets(self):
        tk.Button(self.main_gui_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="View Task", command=self.view_task).grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Edit Task", command=self.edit_task).grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Delete Task", command=self.delete_task).grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="View Schedule", command=self.view_schedule).grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Logout", command=self.logout).grid(row=5, column=0, padx=10, pady=5, sticky="ew")

    def create_account(self):
        self.user = self.create_user.get()
        self.pin = self.create_pin.get()
        messagebox.showinfo("Info", "Successfully created an account!")
        self.create_account_frame.grid_forget()
        self.login_frame.grid(row=0, column=0)

    def login(self):
        if self.login_user.get() == self.user and self.login_pin.get() == self.pin:
            messagebox.showinfo("Info", "Successfully login your account!")
            self.create_account_frame.grid_forget()
            self.main_gui_frame.grid(row=0, column=0)
        else:
            messagebox.showerror("Error", "Invalid input!")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Task To Do:")
        deadline = simpledialog.askstring("Add Deadline", "Deadline:")
        if task and deadline:
            self.tasks.append((task, deadline))
            messagebox.showinfo("Info", "Task Added to View Task")

    def view_task(self):
        if self.tasks:
            value = "\n".join([f"Task: {task}, Deadline: {deadline}" for task, deadline in self.tasks])
            messagebox.showinfo("Task", value)
        else:
            messagebox.showinfo("Task", "There's no task to do yet!")
    
    def edit_task(self):
        if self.tasks:
            edit_task = simpledialog.askstring("Edit", "Name of the task: ")
            for i, (task, deadline) in enumerate(self.tasks):
                if task == edit_task:
                    new_name = simpledialog.askstring("Change", "Edit Name: ")
                    new_deadline = simpledialog.askstring("Change", "Edit Deadline: ")
                    self.tasks[i] = (new_name, new_deadline)
                    messagebox.showinfo("Success", "Successfully changed the task.")
                    return
            messagebox.showerror("Error", "Invalid Input!")
        else:
            messagebox.showinfo("Edit Task", "There's no task to be edit yet.")
    
    def delete_task(self):
        if self.tasks:
            delete_task = simpledialog.askstring("Delete", "Name of the Task:")
            for i, (task, deadline) in enumerate(self.tasks):
                if task == delete_task:
                    self.tasks.pop(i)
                    messagebox.showinfo("Success", "Successfully deleted")
                    return
            messagebox.showerror("Error", "Tasks not found!")
        else:
            messagebox.showinfo("Info", "No task to delete.")

    def view_schedule(self):
        schedule = {
            1: "Monday\n8:00 - 10:00 AM - Science, Technology and Society\n10:00 - 11:00 AM - Vacant\n11:00 - 12:00 PM - Reading in Philippine History\n1:00 - 3:00 PM - Pathfit",
            2: "Tuesday\n7:00 - 10:00 AM - Data Structure and Algorithm\n10:00 - 1:00 PM - Filipino sa Iba't ibang Disiplina\n1:00 - 2:00 PM - Vacant\n2:00 - 4:00 PM - Reading in Philippine History",
            3: "Wednesday\n10:00 - 12:00 PM - Data Structure and Algorithm\n12:00 - 1:00 PM - Vacant\n1:00 - 4:00 PM - Computer Programming",
            4: "Thursday\n11:00 - 12:00 PM - Science, Technology and Society\n12:00 - 1:00 PM - Vacant\n1:00 - 4:00 PM - Linear Algebra\n4:00 - 6:00 PM - Computer Programming"
        }
        pick_num = simpledialog.askinteger("Schedule", "Enter number from 1-4:")
        if pick_num in schedule:
            messagebox.showinfo("Schedule", schedule[pick_num])
        else:
            messagebox.showerror("Error", "Invalid enter of number!")
    
    def logout(self):
        self.main_gui_frame.grid_forget()
        self.login_frame.grid(row=0, column=0)

    

    


               


    
    

                








if __name__ == "__main__":
    create = tk.Tk()
    app = TaskManager(create)
    create.mainloop()