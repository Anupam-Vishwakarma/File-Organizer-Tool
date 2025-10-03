import os
import shutil

# Folder jaha files hai
source_folder = "downloads"  # apna folder name dalna

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_files():
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Agar folder hai to skip
        if os.path.isdir(file_path):
            continue

        # Extension find karo
        _, ext = os.path.splitext(file_name)

        moved = False
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(source_folder, folder)

                # Agar folder nahi hai to create karo
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move file
                shutil.move(file_path, os.path.join(folder_path, file_name))
                print(f" Moved: {file_name} -> {folder}/")
                moved = True
                break

        # Agar koi match nahi mila to Others folder me daal do
        if not moved:
            others_path = os.path.join(source_folder, "Others")
            if not os.path.exists(others_path):
                os.makedirs(others_path)
            shutil.move(file_path, os.path.join(others_path, file_name))
            print(f"📦 Moved: {file_name} -> Others/")

if __name__ == "__main__":
    organize_files()
