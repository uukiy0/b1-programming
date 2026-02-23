# Lab Task 3: File Manager with os Module
# This script demonstrates how to work with files and folders using pythons os module.

import os


def run_file_demo():
    """Performs basic file and directory operations safely."""

    # Show the current working directory
    current_path = os.getcwd()
    print("Current Working Directory:")
    print(current_path)
    print()

    # Create a new folder named "lab_files"
    folder = "lab_files"

    # Check if folder already exists before creating it
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Folder created: {folder}")
    else:
        print(f"Folder '{folder}' already exists.")
    print()

    # Create three empty text files inside the folder
    text_files = ["notes1.txt", "notes2.txt", "notes3.txt"]

    for name in text_files:
        file_location = os.path.join(folder, name)

        # Open file in write mode it then creates file if it doesnt exist
        with open(file_location, "w") as file:
            file.write("")  # Writing empty content

        print(f"Created file: {name}")

    print()

    # List all files inside the folder
    print(f"Files inside '{folder}':")
    file_list = os.listdir(folder)

    for file in file_list:
        print("-", file)

    print()

    # Rename one of the files
    original_name = os.path.join(folder, "notes2.txt")
    updated_name = os.path.join(folder, "updated_notes.txt")

    # Always check if file exists before renaming
    if os.path.exists(original_name):
        os.rename(original_name, updated_name)
        print("File renamed from 'notes2.txt' to 'updated_notes.txt'")
    else:
        print("File to rename was not found.")

    print()

    # Show files again after renaming
    print("Files after renaming:")
    for file in os.listdir(folder):
        print("-", file)

    print()

    # Clean up and delete all files and then remove the folder
    print("Starting cleanup process...")

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        os.remove(file_path)  # Delete each file
        print(f"Deleted file: {file}")

    # Remove the folder after files are deleted
    os.rmdir(folder)
    print(f"Removed folder: {folder}")

    print("\nCleanup completed successfully!")


# Run the program
run_file_demo()
