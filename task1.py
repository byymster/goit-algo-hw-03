import os
import shutil
import sys

def copy_files(src_dir, dest_dir="dist"):
    # Створюємо директорію призначення, якщо її не існує
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Рекурсивне копіювання
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивний виклик для вкладених директорій
            copy_files(item_path, dest_dir)
        else:
            # Отримуємо розширення файлу
            ext = os.path.splitext(item)[1][1:] or "no_extension"
            target_dir = os.path.join(dest_dir, ext)

            try:
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                # Копіюємо файл до відповідної піддиректорії
                shutil.copy2(item_path, target_dir)
            except Exception as e:
                print(f"Помилка при копіюванні файлу {item_path} до {target_dir}: {e}")

if __name__ == "__main__":
    # Отримання аргументів командного рядка
    src_directory = sys.argv[1] if len(sys.argv) > 1 else "."
    dest_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"
    try:
        copy_files(src_directory, dest_directory)
        print(f"Файли скопійовані в {dest_directory}")
    except Exception as e:
        print(f"Помилка: {e}")
