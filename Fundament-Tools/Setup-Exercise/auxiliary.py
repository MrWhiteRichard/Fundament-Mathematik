# ---------------------------------------------------------------- #

import os
import shutil
import itertools
import codecs

# ---------------------------------------------------------------- #

script_folder_path = os.getcwd()
source_folder_path = script_folder_path + r'/../../Fundament-LaTeX/Templates'

# ---------------------------------------------------------------- #

def exercise_and_solution_file_names(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    return [
        f'{exercise_session_number}.{exercise_number}' + '.tex'
        for exercise_number in range(
            exercise_number_min,
            exercise_number_max + 1
        )
    ]

# ---------------------------------------------------------------- #

def setup_exercises_and_solutions(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    for exercise_and_solution_file_name in exercise_and_solution_file_names(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    ):

        # copy 'exercise and solution.tex' as destination_file_name ...

        source_file_name = 'exercise and solution.tex'
        destination_file_name = exercise_and_solution_file_name

        destination_folder_path = exercise_folder_path

        source_file_path      = source_folder_path      + '\\' + source_file_name
        destination_file_path = destination_folder_path + '\\' + destination_file_name
        shutil.copyfile(source_file_path, destination_file_path)

# ---------------------------------------------------------------- #

def setup_exercise_main(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    # -------------------------------- #

    # copy 'main.tex' as 'main.tex'

    source_file_name = 'main.tex'
    destination_file_name = 'main.tex'

    destination_folder_path = exercise_folder_path

    source_file_path      = source_folder_path      + '\\' + source_file_name
    destination_file_path = destination_folder_path + '\\' + destination_file_name
    shutil.copyfile(source_file_path, destination_file_path)

    # -------------------------------- #

    # read old content of 'main.tex' as array of lines
    with codecs.open(source_file_path, 'r', 'utf-8') as main:
        main_content_old = main.readlines()
        # print('main_content_old', main_content_old)

    # -------------------------------- #

    # stuff that gets added to 'main.tex'
    main_content_add = ['\n'] + [
        r'\input{' + exercise_and_solution_file_name + r'}' + '\n'
        for exercise_and_solution_file_name in exercise_and_solution_file_names(
            exercise_folder_path,
            lva_name,
            exercise_session_number,
            exercise_number_min,
            exercise_number_max,
            exercise_date
        )
    ]

    # get index of line that says '\maketitle',
    # will insert new content beneath that line
    index = main_content_old.index(r'\maketitle' + '\r' + '\n')

    # new content of 'main.tex'
    main_content_new = main_content_old[:index+1:] + main_content_add + main_content_old[index+1::]

    # ---------------- #

    if exercise_number_min != 0:

        # add counter ...

        main_content_old = main_content_new
        main_content_add = ['\n'] + [r'\def' + ' ' + r'\lastexercisenumber' + r'{' + str(exercise_number_min - 1) + r'}'] + ['\n']

        # get index of line that says '\documentclass{article}',
        # will insert new content beneath that line
        index = main_content_old.index(r'\documentclass{article}' + '\r' + '\n')

        # new content of 'main.tex'
        main_content_new = main_content_old[:index+1:] + main_content_add + main_content_old[index+1::]

    # ---------------- #

    # replace title ...

    main_content = main_content_new
    main_content_replace = [
        (
            '  ' + 'Titel' + ' ' + r'\\' + '\r' + '\n',
            '  ' + lva_name + ' ' + r'\\' + '\r' + '\n'
        ),
        (
            '  ' + r'\textit{' + 'Untertitel' + r'}' + '\r' + '\n',
            '  ' + r'\textit{' + f'{exercise_session_number}.' + ' ' + u'Übung' + ' ' + f'am {exercise_date}' + r'}' + '\r' + '\n'
        )
    ]

    for x, y in main_content_replace:

        # get index of line that says x
        index = main_content.index(x)

        # change it to y
        main_content[index] = y

    # -------------------------------- #

    # write new content of 'main.tex' as array of lines
    # replace old content with new content
    with codecs.open(destination_file_path, 'w', 'utf-8') as main:
        main.writelines(main_content)

# ---------------------------------------------------------------- #

def setup_exercise(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    setup_exercises_and_solutions(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    )

    setup_exercise_main(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    )

# ---------------------------------------------------------------- #
