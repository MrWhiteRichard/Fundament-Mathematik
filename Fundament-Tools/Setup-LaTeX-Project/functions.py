# ---------------------------------------------------------------- #

import os
import shutil
import itertools
import codecs

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

def exercise_and_solution_file_names(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date):

    Numbers = itertools.product(*[[exercise_number], range(1, exercise_amount+1)])
    destination_file_name  = lambda numbers: '.'.join([str(number) for number in numbers]) + '.tex'
    return [destination_file_name(numbers) for numbers in Numbers]

# ---------------------------------------------------------------- #

def setup_exercises_and_solutions(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date):

    for destination_file_name in exercise_and_solution_file_names(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date):

        # copy 'exercise and solution.tex' as destination_file_name
        path_source_file      = path_source_folder  + '\\' + 'exercise and solution.tex'
        path_destination_file = path_exercise_folder + '\\' + destination_file_name
        shutil.copyfile(path_source_file, path_destination_file)

# ---------------------------------------------------------------- #

def setup_exercise_main(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date):
    
    # copy 'main.tex' as 'main.tex'
    path_source_file      = path_source_folder   + '\\' + 'main.tex'
    path_destination_file = path_exercise_folder + '\\' + 'main.tex'
    shutil.copyfile(path_source_file, path_destination_file)

    # read content of 'main.tex' as array of lines
    with codecs.open(path_source_file, 'r', 'utf-8') as main:
        main_content_old = main.readlines()

    # stuff that gets added to 'main.tex'
    main_content_add = [r'\input{' + exercise_and_solution_file_name + '}\n' for exercise_and_solution_file_name in exercise_and_solution_file_names(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date)]

    # get index of line that says '\maketitle'
    index = main_content_old.index('\\maketitle\r\n')

    # new content of 'main.tex'
    main_content_new = main_content_old[:index+1:] + ['\n'] + main_content_add + main_content_old[index+1::]

    x_1 = '  Titel \\\\\r\n'
    y_1 = '  ' + lva_name + ' - ' + r'\\' + '\n'

    x_2 = '  \\textit{Untertitel}\r\n'
    y_2 = '  ' + r'\textit{' + f'{exercise_number}. ' + u'Übung' + f' am {exercise_date}' + r'}' + '\n'

    for x, y in [(x_1, y_1), (x_2, y_2)]:

        # get index of line that says x
        index = main_content_new.index(x)

        # change it to y
        main_content_new[index] = y

    # write new content to 'main.tex'
    with codecs.open(path_destination_file, 'w', 'utf-8') as main:
        main.writelines(main_content_new)

# ---------------------------------------------------------------- #

def setup_exercise(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date):

    setup_exercises_and_solutions(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date)
    setup_exercise_main          (path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date)

# ---------------------------------------------------------------- #
