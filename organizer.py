import os
import shutil

SOURCE_FOLDER = r"C:\Users\YourName\Downloads"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".tar.gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".sh"],
    "Data": [".csv", ".json"],
    "Others": []
}

def get_category(filename):
    for folder, extensions in FILE_TYPES.items():
        for ext in extensions:
            if filename.lower().endswith(ext):
                return folder
    return None


def organize_files(preview=True):
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            category = get_category(filename)

            if category:
                target_folder = os.path.join(SOURCE_FOLDER, category)

                if preview:
                    print(f"[PREVIEW] {filename} -> {category}/")
                else:
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"[MOVED] {filename} -> {category}/")


if __name__ == "__main__":
    mode = input("Run in preview mode? (y/n): ").lower()

    if mode == "y":
        organize_files(preview=True)
    else:
        organize_files(preview=False)