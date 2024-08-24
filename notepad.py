import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button, messagebox
import os
from typing import Optional

# Global variable to store the current file path
current_file_path: Optional[str] = None


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Your NotePad")

        # Text Widget

        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        # Frame - Create button frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # New file button
        self.new_file: Button = Button(
            self.button_frame, text="New File", command=self.create_new_file
        )
        self.new_file.pack(side="left")

        # Save button
        self.save_button: Button = Button(
            self.button_frame, text="Save", command=self.save_file
        )
        self.save_button.pack(side=tk.LEFT)

        # Save As button
        self.save_as_button: Button = Button(
            self.button_frame, text="Save As", command=self.save_file_as
        )
        self.save_as_button.pack(side=tk.LEFT)

        # Load Button
        self.load_button: Button = Button(
            self.button_frame, text="Load", command=self.load_file
        )
        self.load_button.pack(side=tk.RIGHT)

    def save_file(self) -> None:
        global current_file_path

        if current_file_path is None:
            current_file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text files", "*.txt")]
            )

            if not current_file_path:
                return

        try:
            with open(current_file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully.")
            print(f"File Saved to : {current_file_path}")

        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while saving the file: {e}"
            )

    def load_file(self) -> None:

        global current_file_path
        file_path: str = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )

        if file_path:
            current_file_path = file_path
            with open(current_file_path, "r") as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)

            print(f"File Loaded from: {file_path}")

    def save_file_as(self) -> None:
        global current_file_path

        new_file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if new_file_path:
            current_file_path = new_file_path
            self.save_file()

    def create_new_file(self) -> None:
        global current_file_path, text_area
        current_file_path = None  # Reset the current file path
        self.text_area.delete(1.0, tk.END)  # Clear the text area
        messagebox.showinfo("New File", "New file created. You can now start editing.")
        print(f"New file created. You can now start editing: {current_file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == "__main__":
    main()


"""
Homework:
1. Make it so that the save button saves the text to the current file if it already exists, instead
of asking the user to create a new file each time.

"""
