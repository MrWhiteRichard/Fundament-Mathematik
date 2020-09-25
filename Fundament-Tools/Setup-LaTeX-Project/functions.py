# ---------------------------------------------------------------- #

import os
import shutil
import itertools

# ---------------------------------------------------------------- #

path_script_folder = os.getcwd()
path_script_folder_dissected = path_script_folder.split('\\')

# if script is terminated from super folder of script_super_folder ...
script_super_folder = 'Fundament-Tools'
if script_super_folder not in path_script_folder_dissected:
    path_script_folder_dissected.append(script_super_folder)
    path_script_folder = '\\'.join(path_script_folder_dissected)

# if script is terminated from super folder of script_folder ...
script_folder = 'Setup-LaTeX-Project'
if script_folder not in path_script_folder_dissected:
    path_script_folder_dissected.append(script_folder)
    path_script_folder = '\\'.join(path_script_folder_dissected)

path_source_folder = '\\'.join(path_script_folder_dissected[:-2:] + ['Fundament-LaTeX', 'Templates'])

# ---------------------------------------------------------------- #

def setup_exercises_and_solutions(path_project_folder, Numbers):

    destination_file_names = ['.'.join([str(number) for number in numbers]) + '.tex' for numbers in itertools.product(*Numbers)]

    for destination_file_name in destination_file_names:

        # copy 'exercise and solution.tex' as destination_file_name
        path_source_file      = path_source_folder  + '\\' + 'exercise and solution.tex'
        path_destination_file = path_project_folder + '\\' + destination_file_name
        shutil.copyfile(path_source_file, path_destination_file)

    return destination_file_names

# ---------------------------------------------------------------- #

def setup_main(path_project_folder, subfile_names):
    
    path_source_file = path_project_folder + '\\' + 'main.tex'

    # read content of 'main.tex' as array of lines
    with open(path_source_file, 'r') as main:
        main_content_old = main.readlines()

    # get index of line that says '\maketitle'
    index = main_content_old.index(r'\maketitle'+ '\n')

    # stuff that gets added to 'main.tex'
    main_content_add = [r'\input{' + subfile_name + '}\n' for subfile_name in subfile_names]

    # new content of 'main.tex'
    main_content_new = main_content_old[:index+1:] + ['\n'] + main_content_add+ main_content_old[index+1::]

    # write new content to 'main.tex'
    with open(path_source_file, 'w') as main:
        main.writelines(main_content_new)

# ---------------------------------------------------------------- #

def setup_exercise(path_project_folder, exercise_number, exercise_amount):

    # copy 'main.tex' as 'main.tex'
    path_source_file      = path_source_folder  + '\\' + 'main.tex'
    path_destination_file = path_project_folder + '\\' + 'main.tex'
    shutil.copyfile(path_source_file, path_destination_file)

    Numbers = [[exercise_number], range(1, exercise_amount+1)]
    exercises_and_solution_file_names = setup_exercises_and_solutions(path_project_folder, Numbers)

    setup_main(path_project_folder, exercises_and_solution_file_names)

# ---------------------------------------------------------------- #
