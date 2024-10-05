import os

def explorer(target):
    all_files = list()
    def file_system(directory):
        nonlocal all_files
        for entry in os.listdir(directory):
            path = os.path.join(directory, entry)
            if os.path.isdir(path):
                file_system(path)
            else:
                all_files.append(path)
    file_system(target)
    return all_files

explorer('.')
