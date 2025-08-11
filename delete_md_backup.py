import os
import glob

def delete_backup_files(directory):
    pattern = os.path.join(directory, '*.md.backup')
    files = glob.glob(pattern)
    for file in files:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

if __name__ == "__main__":
    target_dir = r"c:\src\yoo94.github.io\_posts"
    delete_backup_files(target_dir)
