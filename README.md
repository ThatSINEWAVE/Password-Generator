<div align="center">

# [Password Generator](https://thatsinewave.github.io/Password-Generator)

This repository contains a simple password generator application implemented in Python using the CustomTkinter library for the graphical user interface as a script or directly in your browser.
The application allows users to generate up to random passwords with various customizable options.

</div>

<div align="center">

**Script Interface**

![Password-Generator GUI](https://github.com/ThatSINEWAVE/Password-Generator/assets/133239148/4136f56d-2c08-4acb-8d8b-f377d69a982f)

**Web Inteface**

![Password Generator WEB](https://github.com/ThatSINEWAVE/Password-Generator/assets/133239148/c1fd59d5-7f46-4c76-afd0-9a9cea9d8748)

</div>

## Features
- **Password Length**: Users can specify the length of the generated passwords (between 8 and 64 characters).
- **Number of Passwords**: Users can specify the number of passwords to generate (up to 4,294,967,295 passwords)
- **Options**:
  - **Include Numbers**: Option to include numerical digits in the generated passwords.
  - **Mixed Case**: Option to include both uppercase and lowercase letters in the generated passwords.
  - **Include Symbols**: Option to include special symbols in the generated passwords.

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Files

- `main.py`: Contains the main application code implemented using Tkinter for the GUI.
- `utils.py`: Contains utility functions for generating passwords.
- `settings.json`: Contains your saved settings.
- `passowords.json`: Contains the generated passwords.

<div align="center">

# [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

## Usage

To use the password generator:

1. Run the `main.py` file.

2. Adjust the desired options such as password length, inclusion of numbers, mixed case, and symbols.

3. Click on the "Generate" button to generate passwords.

4. Passwords will be saved to a file named `passwords.txt` in the same directory as the script.

5. Additionally, users can save their settings by clicking on the "Save Settings" button.

6. The "Choose Save Path" button allows users to select a custom directory to save the generated passwords.

## Requirements

- Python 3.x
- CustomTkinter library

## Note

Generated passwords are saved to a file named `passwords.txt` in the same directory as the script.
Settings such as password length, inclusion of numbers, mixed case, symbols, and the number of passwords are saved to a `settings.json` file for future use.
Ensure to handle the saved passwords file securely as it contains sensitive information.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
