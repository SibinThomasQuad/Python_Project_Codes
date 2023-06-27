import os
import ctypes

def clean_temp_files():
    temp_path = os.environ.get('TEMP')
    if temp_path:
        for root, dirs, files in os.walk(temp_path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {str(e)}")

def clean_prefetch_files():
    prefetch_path = 'C:\\Windows\\Prefetch'
    if os.path.exists(prefetch_path):
        for file in os.listdir(prefetch_path):
            try:
                file_path = os.path.join(prefetch_path, file)
                os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {str(e)}")

def empty_recycle_bin():
    SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
    SHEmptyRecycleBin(None, None, 1)

def free_ram():
    ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1)

def main():
    clean_temp_files()
    clean_prefetch_files()
    empty_recycle_bin()
    free_ram()
    print("Cleanup completed.")

if __name__ == '__main__':
    main()
