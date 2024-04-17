import os

def open_file_explorer(path):
    try:
        os.startfile(path)  # Open File Explorer at the specified path
        print(f"File Explorer opened at '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = r"C:\00 Sandbox\Data Files"  # Replace with your desired directory path
open_file_explorer(directory_path)
