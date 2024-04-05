import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import utils
import customtkinter


class PasswordGenerator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("SINEWAVE's Password Generator")
        self.geometry("476x191")
        self.resizable(False, False)
        self.bold_font = customtkinter.CTkFont(family="Arial", size=12, weight="bold")
        self.tooltip_label = None
        customtkinter.set_appearance_mode("dark")  # Set dark appearance mode

        self.length_var = customtkinter.StringVar(value="8")
        self.include_numbers_var = customtkinter.BooleanVar(value=True)
        self.include_mixed_case_var = customtkinter.BooleanVar(value=True)
        self.include_symbols_var = customtkinter.BooleanVar(value=False)
        self.num_passwords_var = customtkinter.StringVar(value="1")
        self.save_path = os.path.dirname(os.path.abspath(__file__))

        self.create_widgets()
        self.load_settings()

    def create_widgets(self):
        # Background frame
        background_frame = customtkinter.CTkFrame(self, width=1000, height=1000, bg_color="#111111", fg_color="#111111")
        background_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")
        background_frame.grid_rowconfigure(2, weight=1)
        background_frame.place(x=0, y=0)

        # Password Length frame
        length_frame = customtkinter.CTkFrame(self, width=246, height=50, corner_radius=5, bg_color="#111111")  # Dont forget to add fg_color="#191919"
        length_frame.place(x=10, y=10)
        # Password Length label
        length_label = customtkinter.CTkLabel(length_frame, text="Password Length (8-64):")
        length_label.place(x=12, y=10)
        # Password Length entry field
        self.length_entry = customtkinter.CTkEntry(length_frame, textvariable=self.length_var, width=76)
        self.length_entry.place(x=160, y=11)
        self.length_var.trace_add("write", self.validate_length)

        # Number of Passwords frame
        num_passwords_frame = customtkinter.CTkFrame(self, width=246, height=50, corner_radius=5, bg_color="#111111")  # Dont forget to add fg_color="#191919"
        num_passwords_frame.place(x=10, y=70)
        # Number of Passwords label
        num_passwords_label = customtkinter.CTkLabel(num_passwords_frame, text="Number of Passwords:")
        num_passwords_label.place(x=12, y=10)
        # Number of Passwords entry field
        self.num_passwords_entry = customtkinter.CTkEntry(num_passwords_frame, textvariable=self.num_passwords_var, width=76)
        self.num_passwords_entry.place(x=160, y=11)
        self.num_passwords_var.trace_add("write", self.validate_num_passwords)

        # Options frame
        options_frame = customtkinter.CTkFrame(self, width=200, height=110, corner_radius=5, bg_color="#111111")  # Dont forget to add fg_color="#191919"
        options_frame.place(x=266, y=10)
        # Include Numbers option
        numbers_checkbox = customtkinter.CTkCheckBox(options_frame, text="Include Numbers", variable=self.include_numbers_var)
        numbers_checkbox.place(x=10, y=10)
        # Mixed Case option
        mixed_case_checkbox = customtkinter.CTkCheckBox(options_frame, text="Mixed Case", variable=self.include_mixed_case_var)
        mixed_case_checkbox.place(x=10, y=42)
        # Include Symbols option
        symbols_checkbox = customtkinter.CTkCheckBox(options_frame, text="Include Symbols", variable=self.include_symbols_var)
        symbols_checkbox.place(x=10, y=75)

        # Buttons frame
        buttons_frame = customtkinter.CTkFrame(self, width=456, height=50, corner_radius=5, bg_color="#111111")  # Dont forget to add fg_color="#191919"
        buttons_frame.place(x=10, y=130)
        # Generate button
        generate_button = customtkinter.CTkButton(buttons_frame, text="Generate", command=self.generate_passwords)
        generate_button.place(x=10, y=10)
        # Save Settings button
        save_settings_button = customtkinter.CTkButton(buttons_frame, text="Save Settings", command=self.save_settings)
        save_settings_button.place(x=158, y=10)
        # Choose Save Path button
        choose_save_path_button = customtkinter.CTkButton(buttons_frame, text="Choose Save Path", command=self.choose_save_path)
        choose_save_path_button.place(x=306, y=10)

    def validate_length(self, *args):
        value = self.length_var.get()
        if value:
            if value.isdigit() and 8 <= int(value) <= 128:
                self.length_entry.configure(fg_color="green")
            else:
                self.length_entry.configure(fg_color="red")
        else:
            self.length_entry.configure(fg_color="red")

    def validate_num_passwords(self, *args):
        value = self.num_passwords_var.get()
        if value:
            if value.isdigit() and 1 <= int(value) <= 4294967295:
                self.num_passwords_entry.configure(fg_color="green")
            else:
                self.num_passwords_entry.configure(fg_color="red")
        else:
            self.num_passwords_entry.configure(fg_color="red")

    def generate_passwords(self):
        length = self.length_var.get()
        include_numbers = self.include_numbers_var.get()
        include_mixed_case = self.include_mixed_case_var.get()
        include_symbols = self.include_symbols_var.get()
        num_passwords = self.num_passwords_var.get()

        # Check for valid inputs
        if not length:
            messagebox.showerror("Invalid Input", "Please enter a password length.")
            return
        if not num_passwords:
            messagebox.showerror("Invalid Input", "Please enter the number of passwords.")
            return

        try:
            length = int(length)
            num_passwords = int(num_passwords)
        except ValueError:
            messagebox.showerror("Invalid Input", "Password length and number of passwords must be integers.")
            return

        if length < 8 or length > 64:
            messagebox.showerror("Invalid Input", "Password length must be between 8 and 64.")
            return
        if num_passwords < 1 or num_passwords > 4294967295:
            messagebox.showerror("Invalid Input", "Number of passwords must be between 1 and 4294967295.")
            return

        passwords = utils.generate_passwords(length, include_numbers, include_mixed_case, include_symbols, num_passwords)

        file_path = os.path.join(self.save_path, "passwords.txt")
        mode = "w" if not os.path.exists(file_path) else "a"

        with open(file_path, mode) as file:
            if mode == "w":
                file.write("Generated Passwords:\n")
            for password in passwords:
                file.write(password + "\n")

        messagebox.showinfo("Passwords Generated", f"{num_passwords} passwords have been generated and saved to {file_path}")

    def save_settings(self):
        settings = {
            "length": self.length_var.get(),
            "include_numbers": self.include_numbers_var.get(),
            "include_mixed_case": self.include_mixed_case_var.get(),
            "include_symbols": self.include_symbols_var.get(),
            "num_passwords": self.num_passwords_var.get(),
            "save_path": self.save_path
        }
        settings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        with open(settings_path, "w") as file:
            json.dump(settings, file)
        messagebox.showinfo("Settings Saved", "Settings have been saved successfully.")

    def choose_save_path(self):
        new_path = filedialog.askdirectory()
        if new_path:
            self.save_path = new_path

    def load_settings(self):
        settings_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        if os.path.exists(settings_path):
            with open(settings_path, "r") as file:
                settings = json.load(file)
            self.length_var.set(str(settings["length"]))
            self.include_numbers_var.set(settings["include_numbers"])
            self.include_mixed_case_var.set(settings["include_mixed_case"])
            self.include_symbols_var.set(settings["include_symbols"])
            self.num_passwords_var.set(str(settings["num_passwords"]))
            self.save_path = settings["save_path"]


if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
