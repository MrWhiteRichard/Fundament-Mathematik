from auxiliary import setup_exercise

exercise_folder_path    = str(input('exercise_folder_path           ... '))
lva_name                = str(input('lva_name                       ... '))
exercise_session_number = int(input('exercise_session_number        ... '))
author_names            = str(input('author_names ("author 1, ...") ... '))
exercise_number_min     = int(input('exercise_number_min            ... '))
exercise_number_max     = int(input('exercise_number_max            ... '))
exercise_date           = str(input('exercise_date                  ... '))
language                = str(input('language ("de" / "en")         ... '))

setup_exercise(
    exercise_folder_path,
    lva_name,
    exercise_session_number,
    author_names,
    exercise_number_min,
    exercise_number_max,
    exercise_date,
    language
)
