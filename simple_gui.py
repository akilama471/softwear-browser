import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from folder_scanner import scan_folder
from file_operations import send_to_pendrive, delete_setup
import config

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Software Manager")

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(padx=10, pady=10)

        self.scan_button = tk.Button(button_frame, text="Scan Folder", command=self.scan_folder)
        self.scan_button.grid(row=0, column=0, padx=5, pady=5)

        self.search_button = tk.Button(button_frame, text="Search", command=self.search_files)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

        self.send_button = tk.Button(button_frame, text="Send to Pendrive", command=self.send_to_pendrive)
        self.send_button.grid(row=0, column=2, padx=5, pady=5)

        self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_setup)
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        # Search Entry
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(padx=10, pady=10)

        # Treeview for displaying files
        self.tree = ttk.Treeview(self.root, columns=("Name", "Publisher", "Category", "Path"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Publisher", text="Publisher")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Path", text="Path")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Load initial data
        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

    from database_setup import SoftwareSetup
    for setup in SoftwareSetup.select():
        self.tree.insert("", tk.END, values=(setup.name, setup.publisher, setup.category, setup.path))


    def scan_folder(self):
        scan_folder(config.SETUPS_FOLDER_PATH)
        self.load_data()
        messagebox.showinfo("Info", "Folder scanned and data updated.")

    def search_files(self):
        search_term = self.search_entry.get()
        for row in self.tree.get_children():
            self.tree.delete(row)

        from database_setup import SoftwareSetup
        query = SoftwareSetup.select().where(SoftwareSetup.name.contains(search_term))
        for setup in query:
            self.tree.insert("", tk.END, values=(setup.name, setup.publisher, setup.category, setup.path))

    def send_to_pendrive(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a file to send.")
            return
        
        file_path = self.tree.item(selected_item[0], 'values')[3]
        if not file_path:
            messagebox.showwarning("Warning", "File path not found.")
            return
        
        usb_drive_path = filedialog.askdirectory(title="Select USB Drive")
        if usb_drive_path:
            send_to_pendrive(file_path, usb_drive_path)
            messagebox.showinfo("Info", f"File sent to {usb_drive_path}.")

    def delete_setup(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a file to delete.")
            return
        
        file_path = self.tree.item(selected_item[0], 'values')[3]
        if not file_path:
            messagebox.showwarning("Warning", "File path not found.")
            return
        
        delete_setup(file_path)
        self.load_data()
        messagebox.showinfo("Info", "File deleted and database updated.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    root.mainloop()
