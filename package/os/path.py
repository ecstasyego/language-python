import os

separator = os.path.sep
relative_path = os.path.join('root', 'directory', 'subdirectory', 'python.py')
absolute_path = os.path.join(os.getcwd(), 'root', 'directory', 'subdirectory', 'python.py')
absolute_path = os.path.join(os.path.abspath('.'), 'root', 'directory', 'subdirectory', 'python.py')
absolute_path = os.path.abspath(os.path.join('root', 'directory', 'subdirectory', 'python.py'))

os.path.exists(relative_path)
os.path.isdir(relative_path)
os.path.isfile(relative_path)

relative_path.split(os.path.sep)
os.path.split(relative_path)
os.path.splitext(relative_path)
