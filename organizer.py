import os
import shutil

# Шлях до папки 'Downloads' в англійській локалізації Linux
path = os.path.expanduser('~/Downloads')

# Словник категорій: куди і які файли ми переміщуємо
folders = {
 "Images": [".jpg", ".jpeg", ".png", ".gif"],
 "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
 "Archives": [".zip", ".rar", ".tar.gz"],
 "Programs": [".exe", ".msi", ".deb"],
 "Videos": [".mp4", ".mov", ".mkv", ".avi", ".webm"],
 "Audio": [".mp3", ".wav", ".flac", ".acc", ".m4a"]
}

def organize_files():
    # Перевіряємо, чи існує папка, щоб програма не "впала" з помилкою
    if not os.path.exists(path):
        print("folder doesn`t exists!")
        return
    
    # Складаємо список усіх об'єктів у папці
    files = os.listdir(path)

    for file in files:
        # Відокремлюємо розширення від імені файлу
        filename, extension = os.path.splitext(file)
        extension = extension.lower() # Робимо маленькими для порівняння

        file_path = os.path.join(path, file)

        # Переконуємось, що ми працюємо з файлом, а не з папкою
        if os.path.isfile(file_path):
            for folder_name, extensions in folders.items():
                # Якщо розширення файлу є в нашому списку правил
                if extension in extensions:
                    target_folder = os.path.join(path, folder_name)

                    # Створюємо цільову папку, якщо вона ще не існує
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    # Виконуємо переміщення файлу
                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} -> {folder_name}")
                    break

if __name__ == "__main__":
    print(f"The script is run for: {path}")
    organize_files()
    print("Cleaning is gone!")