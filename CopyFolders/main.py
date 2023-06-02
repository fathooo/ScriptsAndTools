import os
import shutil
import time
from dotenv import load_dotenv
from colorama import init, Fore, Style

init(autoreset=True)
load_dotenv()

LIST_FOLDER_IGNORE = os.getenv('LIST_FOLDER_IGNORE')
SOURCE_FOLDER = os.getenv('SOURCE_FOLDER')
DESTINATION_FOLDER = os.getenv('DESTINATION_FOLDER')
IGNORE_FILES = os.getenv('IGNORE_FILES')
IGNORE_EXTENSION = os.getenv('IGNORE_EXTENSION')

def ignore_directories(dir, files):
    ignored = []
    for folder in LIST_FOLDER_IGNORE:
        if folder in dir or folder in files:
            ignored.append(folder)
    return set(ignored)

print(Fore.YELLOW + "-" * 50)
print(Fore.CYAN + "iniciando.....")
print()
start_time = time.time()

for root, dirs, files in os.walk(SOURCE_FOLDER):

    dirs[:] = [d for d in dirs if d not in LIST_FOLDER_IGNORE]
    # files[:] = [f for f in files if f not in LIST_FOLDER_IGNORE and f not in IGNORE_FILES]

    files[:] = [f for f in files if f not in LIST_FOLDER_IGNORE and f not in IGNORE_FILES and not f.endswith(tuple(IGNORE_EXTENSION))]
    relative_path = os.path.relpath(root, SOURCE_FOLDER)
    dest_path = os.path.join(DESTINATION_FOLDER, relative_path)
    os.makedirs(dest_path, exist_ok=True)

    for file in files:
        src_file = os.path.join(root, file)
        dest_file = os.path.join(dest_path, file)

        if os.path.exists(dest_file):
            print(Fore.YELLOW + f"El archivo '{dest_file}' ya existe. Omitiendo...")
        else:
            print(Fore.GREEN + f"Copiando '{src_file}' a '{dest_file}'...")
            shutil.copy2(src_file, dest_file)
            
            if os.path.exists(dest_file):
                print(Fore.GREEN + f"'{src_file}' copiado a '{dest_file}' exitosamente.\n")
            else:
                print(Fore.RED + f"¡Error al copiar '{src_file}' a '{dest_file}'!\n")
                        
print()
print(Fore.YELLOW + "-" * 50)
print(Fore.CYAN + f"Tiempo de ejecución: {time.time() - start_time} segundos.\n")
