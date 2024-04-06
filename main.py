import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import utils
import customtkinter
import textwrap


APP_ICON = os.path.join(os.path.dirname(__file__), "icon.ico")


def popup_invalid_length():
    title = "Invalid Input"
    message = "Password length must be\nbetween 8 and 64."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=("Arial", 12),
                                   text_color="red",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_no_length():
    title = "Invalid Input"
    message = "Please enter a password length."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=("Arial", 12),
                                   text_color="red",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_password_length():
    title = "Invalid Input"
    message = "Password length must be\nbetween 8 and 64."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=("Arial", 12),
                                   text_color="red",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_invalid_num_passwords():
    title = "Invalid Input"
    message = "Number of passwords must be\nbetween 1 and 4294967295."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=("Arial", 12),
                                   text_color="red",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=10)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_no_num_passwords():
    title = "Invalid Input"
    message = "Number of passwords must be\nbetween 1 and 4294967295."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=("Arial", 12),
                                   text_color="red",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_settings_saved():
    title = "Settings Saved"
    message = "Settings have been\nsaved successfully."
    root = customtkinter.CTkToplevel()
    root.geometry("250x120")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    font = customtkinter.CTkFont(family="Arial",
                                 size=12,
                                 weight="bold")
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=font,
                                   text_color="green",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        font=font,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


def popup_passwords_generated(num_passwords, file_path):
    title = "Passwords Generated"
    message = f"{num_passwords} passwords\nhave been generated and saved to\n{file_path}"
    root = customtkinter.CTkToplevel()
    root.geometry("400x140")
    root.resizable(width=False, 
                   height=False)
    root.title(title)
    root.iconbitmap(APP_ICON)
    # Background frame
    background_frame = customtkinter.CTkFrame(root,
                                              width=1000,
                                              height=1000,
                                              bg_color="#111111",
                                              fg_color="#111111")
    background_frame.grid(row=0,
                          column=0,
                          rowspan=1,
                          sticky="nsew")
    background_frame.grid_rowconfigure(index=2,
                                       weight=1)
    background_frame.place(x=0,
                           y=0)
    font = customtkinter.CTkFont(family="Arial",
                                 size=12,
                                 weight="bold")
    label = customtkinter.CTkLabel(root,
                                   text=message,
                                   font=font,
                                   text_color="green",
                                   bg_color="#111111")
    label.pack(padx=20,
               pady=20)
    ok_button = customtkinter.CTkButton(root,
                                        text="OK",
                                        command=root.destroy,
                                        font=font,
                                        hover_color="#3D0000",
                                        bg_color="#111111",
                                        fg_color="#950101")
    ok_button.pack(padx=0,
                   pady=0)
    root.grab_set()


class PasswordGenerator(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.num_passwords_entry = None
        self.length_entry = None
        self.title("SINEWAVE's Password Generator")
        self.geometry("476x191")
        self.resizable(width=False, 
                       height=False)
        self.iconbitmap(APP_ICON)
        self.font = customtkinter.CTkFont(family="Arial",
                                          size=12,
                                          weight="bold")
        self.tooltip_label = None
        customtkinter.set_appearance_mode("dark")

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
        background_frame = customtkinter.CTkFrame(self,
                                                  width=1000,
                                                  height=1000,
                                                  bg_color="#111111",
                                                  fg_color="#111111")
        background_frame.grid(row=0,
                              column=0,
                              rowspan=1,
                              sticky="nsew")
        background_frame.grid_rowconfigure(index=2,
                                           weight=1)
        background_frame.place(x=0,
                               y=0)

        # Password Length frame
        length_frame = customtkinter.CTkFrame(self,
                                              width=246,
                                              height=50,
                                              corner_radius=5,
                                              bg_color="#111111",
                                              fg_color="#191919")
        length_frame.place(x=10,
                           y=10)
        # Password Length label
        length_label = customtkinter.CTkLabel(length_frame,
                                              text="Password Length (8-64):",
                                              font=self.font)
        length_label.place(x=12,
                           y=10)
        # Password Length entry field
        self.length_entry = customtkinter.CTkEntry(length_frame,
                                                   textvariable=self.length_var,
                                                   width=76,
                                                   justify='center')
        self.length_entry.place(x=160,
                                y=11)
        self.length_var.trace_add("write", self.validate_length)

        # Number of Passwords frame
        num_passwords_frame = customtkinter.CTkFrame(self,
                                                     width=246,
                                                     height=50,
                                                     corner_radius=5,
                                                     bg_color="#111111",
                                                     fg_color="#191919")
        num_passwords_frame.place(x=10,
                                  y=70)
        # Number of Passwords label
        num_passwords_label = customtkinter.CTkLabel(num_passwords_frame,
                                                     text="Number of Passwords:",
                                                     font=self.font)
        num_passwords_label.place(x=12,
                                  y=10)
        # Number of Passwords entry field
        self.num_passwords_entry = customtkinter.CTkEntry(num_passwords_frame,
                                                          textvariable=self.num_passwords_var,
                                                          width=76,
                                                          justify='center')
        self.num_passwords_entry.place(x=160,
                                       y=11)
        self.num_passwords_var.trace_add("write",
                                         self.validate_num_passwords)

        # Options frame
        options_frame = customtkinter.CTkFrame(self,
                                               width=200,
                                               height=110, corner_radius=5,
                                               bg_color="#111111",
                                               fg_color="#191919")
        options_frame.place(x=266,
                            y=10)
        # Include Numbers option
        numbers_checkbox = customtkinter.CTkCheckBox(options_frame,
                                                     text="Include Numbers",
                                                     variable=self.include_numbers_var,
                                                     hover_color="#3D0000",
                                                     fg_color="#950101",
                                                     font=self.font)
        numbers_checkbox.place(x=10,
                               y=10)
        # Mixed Case option
        mixed_case_checkbox = customtkinter.CTkCheckBox(options_frame,
                                                        text="Mixed Case",
                                                        variable=self.include_mixed_case_var,
                                                        hover_color="#3D0000",
                                                        fg_color="#950101",
                                                        font=self.font)
        mixed_case_checkbox.place(x=10,
                                  y=42)
        # Include Symbols option
        symbols_checkbox = customtkinter.CTkCheckBox(options_frame,
                                                     text="Include Symbols",
                                                     variable=self.include_symbols_var,
                                                     hover_color="#3D0000",
                                                     fg_color="#950101",
                                                     font=self.font)
        symbols_checkbox.place(x=10,
                               y=75)

        # Buttons frame
        buttons_frame = customtkinter.CTkFrame(self,
                                               width=456,
                                               height=50,
                                               corner_radius=5,
                                               bg_color="#111111",
                                               fg_color="#191919")
        buttons_frame.place(x=10,
                            y=130)
        # Generate button
        generate_button = customtkinter.CTkButton(buttons_frame,
                                                  text="Generate",
                                                  command=self.generate_passwords,
                                                  hover_color="#3D0000",
                                                  fg_color="#950101",
                                                  font=self.font)
        generate_button.place(x=10,
                              y=10)
        # Save Settings button
        save_settings_button = customtkinter.CTkButton(buttons_frame,
                                                       text="Save Settings",
                                                       command=self.save_settings,
                                                       hover_color="#3D0000",
                                                       fg_color="#950101",
                                                       font=self.font)
        save_settings_button.place(x=158,
                                   y=10)
        # Choose Save Path button
        choose_save_path_button = customtkinter.CTkButton(buttons_frame,
                                                          text="Choose Save Path",
                                                          command=self.choose_save_path,
                                                          hover_color="#3D0000",
                                                          fg_color="#950101",
                                                          font=self.font)
        choose_save_path_button.place(x=306,
                                      y=10)

    def validate_length(self, *args):
        _ = args
        value = self.length_var.get()
        if value:
            if value.isdigit() and 8 <= int(value) <= 128:
                self.length_entry.configure(fg_color="green")
            else:
                self.length_entry.configure(fg_color="red")
        else:
            self.length_entry.configure(fg_color="red")

    def validate_num_passwords(self, *args):
        _ = args
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
        num_passwords = self.num_passwords_var.get()

        # Check for valid inputs
        if not length:
            popup_no_length()
            return
        if not num_passwords:
            popup_no_num_passwords()
            return

        try:
            length = int(length)
            num_passwords = int(num_passwords)
        except ValueError:
            popup_password_length()
            return

        if length < 8 or length > 64:
            popup_invalid_length()
            return
        if num_passwords < 1 or num_passwords > 4294967295:
            popup_invalid_num_passwords()
            return

        passwords = utils.generate_passwords(length,
                                             self.include_numbers_var.get(),
                                             self.include_mixed_case_var.get(),
                                             self.include_symbols_var.get(),
                                             num_passwords)

        file_path = os.path.join(self.save_path, "passwords.txt")
        mode = "w" if not os.path.exists(file_path) else "a"

        with open(file_path, mode) as file:
            if mode == "w":
                file.write("Generated Passwords:\n")
            for password in passwords:
                file.write(password + "\n")

        popup_passwords_generated(len(passwords), file_path)

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
        popup_settings_saved()

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
