import os
import shutil

# Get the list of all files in directory tree at given path
def get_files_tree(dir_name):

    files = list()
    for (dir_path, dir_names, file_names) in os.walk(dir_name):
        files += [os.path.join(dir_path, file) for file in file_names]

    return files

# Get the list of all files in directory tree at given path_1 but not in directory tree at given path_2
# ... and vice versa
def get_files_differences_list(path_1, path_2):

    file_paths_1 = [file_path[len(path_1)+1::] for file_path in get_files_tree(path_1)]
    file_paths_2 = [file_path[len(path_2)+1::] for file_path in get_files_tree(path_2)]

    file_paths_1_minus_file_paths_2 = [file for file in file_paths_1 if file not in file_paths_2]
    file_paths_2_minus_file_paths_1 = [file for file in file_paths_2 if file not in file_paths_1]

    return file_paths_1_minus_file_paths_2, file_paths_2_minus_file_paths_1

# Get the list of all files in directory tree at given path_1 but not in directory tree at given path_2
def get_files_difference_list(path_1, path_2):
    return get_files_differences_list(path_1, path_2)[0]

# Copy files in directory tree at given path_1 but not in directory tree at given path_2 to path_difference
def copy_files_difference(path_1, path_2, path_difference):

    for file in get_files_difference_list(path_1, path_2):

        source = os.path.join(path_1, file)
        destination = os.path.join(path_difference, file)

        os.makedirs(os.path.dirname(destination), exist_ok = True)
        shutil.copy(source, destination)