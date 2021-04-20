# ---------------------------------------------------------------- #

import os
import shutil
import itertools
import codecs

# ---------------------------------------------------------------- #

while os.path.basename(os.getcwd()) != 'Fundament-Mathematik':
    os.chdir('..')

os.chdir('Fundament-Tools/Setup-Exercise')

script_folder_path = os.getcwd()
source_folder_path = script_folder_path + r'/../../Fundament-LaTeX/Templates'

# ---------------------------------------------------------------- #

def exercise_and_solution_file_names(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    author_names,
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
    author_names,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    for exercise_and_solution_file_name in exercise_and_solution_file_names(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        author_names,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    ):

        # copy 'exercise and solution.tex' as destination_file_name ...

        source_file_name = 'exercise and solution.tex'
        destination_file_name = exercise_and_solution_file_name

        destination_folder_path = exercise_folder_path

        source_file_path      = source_folder_path      + '/' + source_file_name
        destination_file_path = destination_folder_path + '/' + destination_file_name
        shutil.copyfile(source_file_path, destination_file_path)

# ---------------------------------------------------------------- #

def setup_exercise_main(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    author_names,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    # -------------------------------- #

    # copy 'main.tex' as 'main.tex'

    source_file_name = 'main.tex'
    destination_file_name = 'main.tex'

    destination_folder_path = exercise_folder_path

    source_file_path      = source_folder_path      + '/' + source_file_name
    destination_file_path = destination_folder_path + '/' + destination_file_name
    shutil.copyfile(source_file_path, destination_file_path)

    # -------------------------------- #
    # read old content of 'main.tex' as array of lines

    with codecs.open(source_file_path, 'r', 'utf-8') as main:
        main_content = main.readlines()

    # -------------------------------- #
    # add stuff to 'main.tex'

    # ---------------- #
    # add \input{}-s

    main_content_add = []
    main_content_add += ['\n']
    main_content_add += [
        r'\input{' + exercise_and_solution_file_name + r'}' + '\n'
        for exercise_and_solution_file_name in exercise_and_solution_file_names(
            exercise_folder_path,
            lva_name,
            exercise_session_number,
            author_names,
            exercise_number_min,
            exercise_number_max,
            exercise_date
        )
    ]

    # get index of line that says '\maketitle',
    # will insert new content beneath that line
    index = main_content.index(r'\maketitle' + '\r' + '\n')

    # new content of 'main.tex'
    main_content = main_content[:index+1:] + main_content_add + main_content[index+1::]

    # ---------------- #
    # add \lastexercisenumber

    if exercise_number_min != 0:

        # add counter ...

        main_content = main_content
        main_content_add = ['\n'] + [r'\def' + ' ' + r'\lastexercisenumber' + r'{' + str(exercise_number_min - 1) + r'}'] + ['\n']

        # get index of line that says '\documentclass{article}',
        # will insert new content beneath that line
        index = main_content.index(r'\documentclass{article}' + '\r' + '\n')

        # new content of 'main.tex'
        main_content = main_content[:index+1:] + main_content_add + main_content[index+1::]

    # -------------------------------- #
    # replace stuff in 'main.tex'

    main_content_replace = []

    # ---------------- #
    # author_replacement

    author_replacement = ''

    if len(author_names) == 1:
        author_replacement += r'\author{' + author_names[0] + r'}' + '\r' + '\n'

    else:

        author_replacement += r'\author' + '\r' + '\n'
        author_replacement += r'{' + '\r' + '\n'

        for author_name in author_names[:-1]:
            author_replacement += '    ' + author_name + '\r' + '\n'
            author_replacement += '    ' + r'\and' + '\r' + '\n'

        author_replacement += '    ' + author_names[-1] + '\r' + '\n'
        author_replacement += r'}' + '\r' + '\n'

    main_content_replace += [
        (
            r'\author{' + 'Autor' + r'}' + '\r' + '\n',
            author_replacement
        )
    ]

    # ---------------- #
    # \input{}-replacements

    path_split = exercise_folder_path.split('\\')

    i = 0
    n = len(path_split) - 1
    while path_split[n-i] != 'Fundament-Mathematik':

        assert n >= i
        i += 1

    for line in main_content:
        if 'Fundament-LaTeX' in line:
            main_content_replace += [
                (
                    line,
                    line.replace(
                        'Fundament-LaTeX',
                        r'../' * i + 'Fundament-LaTeX'
                    )
                )
            ]

    # ---------------- #
    # miscellaneous replacements

    main_content_replace += [
        (
            '    ' + 'Titel' + ' ' + r'\\' + '\r' + '\n',
            '    ' + lva_name + ' ' + r'\\' + '\r' + '\n'
        ),
        (
            '    ' + r'\textit{' + 'Untertitel' + r'}' + '\r' + '\n',
            '    ' + r'\textit{' + f'{exercise_session_number}.' + ' ' + u'Übung' + r'}' + '\r' + '\n'
        ),
        (
            r'\date{}' + '\r' + '\n',
            r'\date{' + f'{exercise_date}' + r'}' + '\r' + '\n'
        )
    ]

    # ---------------- #
    # do actual replacing

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
    author_names,
    exercise_number_min,
    exercise_number_max,
    exercise_date
):

    # -------------------------------- #
    # pre process author_names
    # e.g. 'Richard Weiss,  Florian Schager' -> ['Richard Weiss', 'Florian Schager']

    author_names = author_names.split(',')

    for i, author_name in enumerate(author_names):

        lower_bound = 0
        while author_name[lower_bound] == ' ':
            lower_bound += 1

        upper_bound = len(author_name) - 1
        while author_name[upper_bound] == ' ':
            upper_bound -= 1

        author_names[i] = author_name[lower_bound:upper_bound+1]

    # -------------------------------- #

    setup_exercises_and_solutions(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        author_names,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    )

    setup_exercise_main(
        exercise_folder_path,
        lva_name,
        exercise_session_number,
        author_names,
        exercise_number_min,
        exercise_number_max,
        exercise_date
    )

# ---------------------------------------------------------------- #
