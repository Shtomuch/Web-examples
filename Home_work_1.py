import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path, root_path, target_dir):

    extension = file_path.split('.')[-1]
    if extension == file_path:  # Якщо файл без розширення
        extension = 'no_extension'

    dest_dir = os.path.join(target_dir, extension)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.copy(file_path, dest_dir)

def process_directory(directory, root_path, target_dir):

    for entry in os.scandir(directory):
        if entry.is_dir():
            process_directory(entry.path, root_path, target_dir)
        elif entry.is_file():
            executor.submit(copy_file, entry.path, root_path, target_dir)


if __name__ == "__main__":


    source_dir = sys.argv[1] if len(sys.argv) > 1 else 'picture'
    dist_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    with ThreadPoolExecutor() as executor:
        process_directory(source_dir, source_dir, dist_dir)
