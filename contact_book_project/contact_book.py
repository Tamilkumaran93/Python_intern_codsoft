import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")
        self.root.config(bg="#2C3E50")
        
        self.contacts = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Contact Manager", bg="#2C3E50", fg="#ECF0F1", font=('Arial', 18))
        self.label.pack(pady=10)
        
        self.frame = tk.Frame(self.root, bg="#34495E")
        self.frame.pack(pady=20)
        
        self.name_label = tk.Label(self.frame, text="Name:", bg="#34495E", fg="#ECF0F1", font=('Arial', 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.name_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(self.frame, text="Phone Number:", bg="#34495E", fg="#ECF0F1", font=('Arial', 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.phone_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(self.frame, text="Email:", bg="#34495E", fg="#ECF0F1", font=('Arial', 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.email_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(self.frame, text="Address:", bg="#34495E", fg="#ECF0F1", font=('Arial', 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.address_entry = tk.Entry(self.frame, font=('Arial', 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, bg="#1ABC9C", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#16A085")
        self.add_button.pack(pady=10)
        
        self.search_label = tk.Label(self.root, text="Search:", bg="#2C3E50", fg="#ECF0F1", font=('Arial', 12))
        self.search_label.pack(pady=10)
        
        self.search_entry = tk.Entry(self.root, font=('Arial', 12))
        self.search_entry.pack()
        
        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact, bg="#3498DB", fg="white", font=('Arial', 12), bd=0, highlightthickness=0, activebackground="#2980B9")
        self.search_button.pack(pady=5)
        
        self.contacts_listbox = tk.Listbox(self.root, font=('Arial', 12), width=50, height=10)
        self.contacts_listbox.pack(pady=10)
        
        self.view_contacts()
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.clear_entries()
            self.view_contacts()
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Name and Phone Number are required.")
    
    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
    
    def search_contact(self):
        query = self.search_entry.get().lower()
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if query in contact['Name'].lower() or query in contact['Phone']:
                self.contacts_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    
    def clear_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
    
    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            contact = self.contacts[index]
            confirm = messagebox.askyesno("Delete Contact", f"Do you want to delete {contact['Name']}?")
            if confirm:
                del self.contacts[index]
                self.clear_listbox()
                self.view_contacts()
                messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
