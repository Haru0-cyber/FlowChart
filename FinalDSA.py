import tkinter as tk
from tkinter import simpledialog, messagebox
class TaskManager():
    def __init__(self, create):
        self.create = create
        self.create.title("Task Manager")
        self.tasks = []

        self.create_account_frame = tk.Frame(self.create)
        self.login_account_frame = tk.Frame(self.create)
        self.main_gui_frame = tk.Frame(self.create)

        self.create_account()
        self.login_account()
        self.main_gui()

        self.create_account_frame.grid(row=0, column=0)

    def create_account(self):
        tk.Label(self.create_account_frame, text="Create your Account", foreground="black", relief="solid", background="grey").grid(row=0, padx=90, pady=5, column=0, sticky="w")

        tk.Label(self.create_account_frame, text="Create Username:", relief="groove", foreground="black", background="grey").grid(row=1, padx=10, pady=5, column=0, sticky="w")
        self.create_user = tk.Entry(self.create_account_frame)
        self.create_user.grid(row=1, padx=110, pady=5, column=0, sticky="w")

        tk.Label(self.create_account_frame, text="Create password:",relief="groove", foreground="black", background="grey").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.create_pass = tk.Entry(self.create_account_frame, show="*")
        self.create_pass.grid(row=2, column=0, padx=110, pady=5, sticky="w")

        tk.Button(self.create_account_frame, text="Create account", command=self.create_acc, background="grey", foreground="white",relief="groove").grid(row=3, column=0, padx=100, pady=5, sticky="w")

    def login_account(self):
        tk.Label(self.login_account_frame, text="Login Your Account", foreground="black", relief="solid", background="grey").grid(row=0, column=0, padx=100, pady=5, sticky="w")

        tk.Label(self.login_account_frame, text="Enter Username:", relief="groove", foreground="black", background="grey").grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.login_user = tk.Entry(self.login_account_frame)
        self.login_user.grid(row=1, column=0, padx=120, pady=5, sticky="w")

        tk.Label(self.login_account_frame, text="Enter Password:", relief="groove", foreground="black", background="grey").grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.login_password = tk.Entry(self.login_account_frame, show="*")
        self.login_password.grid(row=2, column=0, padx=120, pady=5, sticky="w")

        tk.Button(self.login_account_frame, text="Login Account", command=self.login_acc, relief="groove", background="grey", foreground="white").grid(row=3, column=0, padx=100, pady=5, sticky="w")


    def main_gui(self):
        tk.Label(self.main_gui_frame, text="Listy: Smart Task", relief="groove").grid(row=0, column=0, padx=50, pady=5, sticky="w")
        tk.Button(self.main_gui_frame, text="Add Task", command=self.add_task, relief="groove", background="black", foreground="white").grid(row=1, column=0, padx=10, pady=5,sticky="ew")
        tk.Button(self.main_gui_frame, text="View Task", command=self.view_task, relief="groove", background="black", foreground="white").grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Edit Task", command=self.edit_task, relief="groove", background="black", foreground="white").grid(row=3, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Delete Task", command=self.delete_task, relief="groove", background="black", foreground="white").grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="View Schedule", command=self.view_sched, relief="groove", background="black", foreground="white").grid(row=5, column=0, padx=10, pady=5, sticky="ew")
        tk.Button(self.main_gui_frame, text="Logout", command=self.logout, relief="groove", background="red", foreground="white").grid(row=6, column=0, padx=10, pady=5, sticky="ew")


    def create_acc(self):
        self.user_create = self.create_user.get()
        self.pass_create = self.create_pass.get()
        messagebox.showinfo("Create Account", "Successfully Created an account!")
        self.create_account_frame.grid_forget()
        self.login_account_frame.grid(row=0, column=0)

    def login_acc(self):
        if self.login_user.get() == self.user_create and self.login_password.get() == self.pass_create:
            messagebox.showinfo("Login", "Successfully login your account.")
            self.login_account_frame.grid_forget()
            self.main_gui_frame.grid(row=0, column=0)
        else:
            messagebox.showerror("Login", "Invalid input!")

    def add_task(self):
        name = simpledialog.askstring("Name", "Name of the Task: ")
        deadline = simpledialog.askstring("Deadline", "Deadline of the Task: ")
        if name and deadline:
            self.tasks.append((name, deadline))
            messagebox.showinfo("Add Task", "Successfully added to View Task.")
            return

    def view_task(self):
        if self.tasks:
            value = "\n".join([f"Name: {name} - Deadline: {deadline}" for name, deadline in self.tasks])
            messagebox.showinfo("Task", value)
        else:
            messagebox.showinfo("Task", "No Task Yet.")

    def edit_task(self):
        if self.tasks:
            edit = simpledialog.askstring("Edit", "Task to be edit: ")
            for i, (name, deadline) in enumerate(self.tasks):
                if name == edit:
                    change_name = simpledialog.askstring("Change", "Change Task Name: ")
                    change_deadline = simpledialog.askstring("Change", "Change Task Deadline: ")
                    self.tasks[i] = ((change_name, change_deadline))
                    messagebox.showinfo("Edit", "Successfully Changed")
                return
            messagebox.showinfo("Invalid", "Invalid Name")
    
    
    
    
    def delete_task(self):
        if self.tasks:
            delete = simpledialog.askstring("Delete", "Remove Task: ")
            for i, (name, deadline) in enumerate(self.tasks):
                if name == delete:
                    self.tasks.pop(i)
                    messagebox.showinfo("Delete", "Successfully deleted.")
                else:
                    messagebox.showinfo("Delete", "Invalid input.")

    def view_sched(self):
        schedule = {
            1: "Monday\n8:00 - 10:00 AM - Science, Technology and Society\n10:00 - 11:00 AM - Vacant\n11:00 - 12:00 PM - Reading in Philippine History\n1:00 - 3:00 PM - Pathfit",
            2: "Tuesday\n7:00 - 10:00 AM - Data Structure and Algorithm\n10:00 - 1:00 PM - Filipino sa Iba't ibang Disiplina\n1:00 - 2:00 PM - Vacant\n2:00 - 4:00 PM - Reading in Philippine History",
            3: "Wednesday\n10:00 - 12:00 PM - Data Structure and Algorithm\n12:00 - 1:00 PM - Vacant\n1:00 - 4:00 PM - Computer Programming",
            4: "Thursday\n11:00 - 12:00 PM - Science, Technology and Society\n12:00 - 1:00 PM - Vacant\n1:00 - 4:00 PM - Linear Algebra\n4:00 - 6:00 PM - Computer Programming"
        }
        messagebox.showinfo("Schedule", "Monday = 1 | Tuesday = 2 | Wednesday = 3 | Friday = 4")
        num = simpledialog.askinteger("Schedule", "Enter a number from 1-4: ")
        
        if num in schedule:
            messagebox.showinfo("Schedule", schedule[num])
        else:
            messagebox.showerror("Invalid", "Invalid input please try again.")

    def logout(self):
        messagebox.showinfo("Logout", "Thank you for using me!")
        self.main_gui_frame.grid_forget()
        self.create_account_frame.grid(row=0, column=0)

if __name__ == "__main__":
    create = tk.Tk()
    apk = TaskManager(create)
    create.mainloop()
                 




















   
            


