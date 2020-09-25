from functions import setup_exercise

path_project_folder = str(input('path_project_folder ... '))
exercise_number     = int(input('exercise_number     ... '))
exercise_amount     = int(input('exercise_amount     ... '))

setup_exercise(path_project_folder, exercise_number, exercise_amount)
