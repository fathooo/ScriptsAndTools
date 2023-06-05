import os
import shutil
import time
from dotenv import load_dotenv
from colorama import init, Fore, Style

init(autoreset=True)
load_dotenv()

SOURCE_FOLDER = os.getenv('SOURCE_FOLDER')
DESTINATION_FOLDER = os.getenv('DESTINATION_FOLDER')
INCLUDED_FILES = os.getenv('INCLUDED_FILES')

print(Fore.YELLOW + "-" * 50)
print(Fore.CYAN + f"Iniciando copia de archivos incluidos en {INCLUDED_FILES}")
print()
start_time = time.time()

for root, dirs, files in os.walk(SOURCE_FOLDER):

    included_files = [f for f in files if f in INCLUDED_FILES]

    if not included_files:
        continue

    relative_path = os.path.relpath(root, SOURCE_FOLDER)
    dest_path = os.path.join(DESTINATION_FOLDER, relative_path)
    os.makedirs(dest_path, exist_ok=True)

    for file in included_files:
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