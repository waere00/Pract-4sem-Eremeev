import os
import shutil
from settings import WORKING_DIRECTORY


def create_folder(name):
    folder_path = os.path.join(WORKING_DIRECTORY, name)
    os.mkdir(folder_path)
    print(f"Создана папка {name}")


def delete_folder(name):
    folder_path = os.path.join(WORKING_DIRECTORY, name)
    shutil.rmtree(folder_path)
    print(f"Удалена папка {name}")


def move_to_folder(name):
    global WORKING_DIRECTORY

    if name == "..":
        # Перейти в родительскую директорию
        parent_directory = os.path.dirname(WORKING_DIRECTORY)
        if parent_directory.startswith(WORKING_DIRECTORY):
            WORKING_DIRECTORY = parent_directory
            print("Перешли в родительскую папку")
        else:
            print("Вы достигли корневой папки")
    else:
        # Перейти в подпапку
        folder_path = os.path.join(WORKING_DIRECTORY, name)
        if os.path.isdir(folder_path) and folder_path.startswith(WORKING_DIRECTORY):
            WORKING_DIRECTORY = folder_path
            print(f"Перешли в папку {name}")
        else:
            print(f"Папка {name} не существует или находится за пределами рабочей папки")



def create_file(name):
    file_path = os.path.join(WORKING_DIRECTORY, name)
    open(file_path, 'a').close()
    print(f"Создан файл {name}")


def write_to_file(name):
    file_path = os.path.join(WORKING_DIRECTORY, name)
    if os.path.isfile(file_path):
        text = input("Введите текст для записи в файл: ")
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Текст записан в файл {name}")
    else:
        print(f"Файл {name} не существует")


def view_file_contents(name):
    file_path = os.path.join(WORKING_DIRECTORY, name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
        print(f"Содержимое файла {name}:")
        print(contents)
    else:
        print(f"Файл {name} не существует")


def delete_file(name):
    file_path = os.path.join(WORKING_DIRECTORY, name)
    os.remove(file_path)
    print(f"Удален файл {name}")


def copy_file(source, destination):
    source_path = os.path.join(WORKING_DIRECTORY, source)
    destination_path = os.path.join(WORKING_DIRECTORY, destination)
    shutil.copy(source_path, destination_path)
    print(f"Файл {source} скопирован в {destination}")


def move_file(source, destination):
    source_path = os.path.join(WORKING_DIRECTORY, source)
    destination_path = os.path.join(WORKING_DIRECTORY, destination)
    shutil.move(source_path, destination_path)
    print(f"Файл {source} перемещен в {destination}")


def rename_file(old_name, new_name):
    old_path = os.path.join(WORKING_DIRECTORY, old_name)
    new_path = os.path.join(WORKING_DIRECTORY, new_name)
    os.rename(old_path, new_path)
    print(f"Файл {old_name} переименован в {new_name}")


def print_menu():
    print("=== Простой файловый менеджер ===")
    print("Текущая папка:", WORKING_DIRECTORY)
    print("1. Создать папку (mkfolder)")
    print("2. Удалить папку (rmfolder)")
    print("3. Перейти в папку (goto)")
    print("4. Создать файл (mkfile)")
    print("5. Записать в файл (writefile)")
    print("6. Просмотреть содержимое файла (viewcat)")
    print("7. Удалить файл (rmfile)")
    print("8. Копировать файл (cpfile)")
    print("9. Переместить файл (mvfile)")
    print("10. Переименовать файл (renamefile)")
    print("0. Выйти (quit)")


def process_choice(choice):
    if choice == "1" or choice.lower() == "mkfolder":
        folder_name = input("Введите имя папки: ")
        create_folder(folder_name)
    elif choice == "2" or choice.lower() == "rmfolder":
        folder_name = input("Введите имя папки: ")
        delete_folder(folder_name)
    elif choice == "3" or choice.lower() == "goto":
        folder_name = input("Введите имя папки или '..' для перехода в родительскую папку: ")
        move_to_folder(folder_name)
    elif choice == "4" or choice.lower() == "makefile":
        file_name = input("Введите имя файла: ")
        create_file(file_name)
    elif choice == "5" or choice.lower() == "writefile":
        file_name = input("Введите имя файла: ")
        write_to_file(file_name)
    elif choice == "6" or choice.lower() == "viewcat":
        file_name = input("Введите имя файла: ")
        view_file_contents(file_name)
    elif choice == "7" or choice.lower() == "rmfile":
        file_name = input("Введите имя файла: ")
        delete_file(file_name)
    elif choice == "8" or choice.lower() == "cpfile":
        source_file = input("Введите имя исходного файла: ")
        destination_file = input("Введите имя целевого файла: ")
        copy_file(source_file, destination_file)
    elif choice == "9" or choice.lower() == "mvfile":
        source_file = input("Введите имя исходного файла: ")
        destination_file = input("Введите имя целевого файла: ")
        move_file(source_file, destination_file)
    elif choice == "10" or choice.lower() == "renamefile":
        old_name = input("Введите текущее имя файла: ")
        new_name = input("Введите новое имя файла: ")
        rename_file(old_name, new_name)
    elif choice == "0" or choice.lower() == "quit":
        return False
    else:
        print("Некорректный выбор. Попробуйте снова.")
    return True


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Введите ваш выбор: ")

        if not process_choice(choice):
            break
