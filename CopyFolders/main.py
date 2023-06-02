import os
import shutil
from dotenv import load_dotenv

load_dotenv()

LIST_FOLDER_IGNORE = os.getenv('LIST_FOLDER_IGNORE')
SOURCE_FOLDER = os.getenv('SOURCE_FOLDER')
DESTINATION_FOLDER = os.getenv('DESTINATION_FOLDER')
IGNORE_FILES = os.getenv('IGNORE_FILES')

def ignore_directories(dir, files):
    ignored = []
    for folder in LIST_FOLDER_IGNORE:
        if folder in dir or folder in files:
            ignored.append(folder)
    return set(ignored)


for root, dirs, files in os.walk(SOURCE_FOLDER):
    dirs[:] = [d for d in dirs if d not in LIST_FOLDER_IGNORE]
    files[:] = [f for f in files if f not in LIST_FOLDER_IGNORE and f not in IGNORE_FILES]

    relative_path = os.path.relpath(root, SOURCE_FOLDER)
    dest_path = os.path.join(DESTINATION_FOLDER, relative_path)
    os.makedirs(dest_path, exist_ok=True)

    for file in files:
        src_file = os.path.join(root, file)
        dest_file = os.path.join(dest_path, file)
        
        print(f"Copiando '{src_file}' a '{dest_file}'...")
        
        shutil.copy2(src_file, dest_file)
        
        if os.path.exists(dest_file):
            print(f"'{src_file}' copiado a '{dest_file}' exitosamente.\n")
        else:
            print(f"¡Error al copiar '{src_file}' a '{dest_file}'!\n")