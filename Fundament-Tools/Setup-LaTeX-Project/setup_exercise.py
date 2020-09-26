from functions import setup_exercise

path_exercise_folder = str(input('path_exercise_folder ... '))
lva_name             = str(input('lva_name             ... '))
exercise_number      = int(input('exercise_number      ... '))
exercise_amount      = int(input('exercise_amount      ... '))
exercise_date        = str(input('exercise date        ... '))

setup_exercise(path_exercise_folder, lva_name, exercise_number, exercise_amount, exercise_date)
