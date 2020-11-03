import os

# ---------------------------------------------------------------- #

"""

substitutions = {}

for x, y in substitutions.items():

    for n, file_name in enumerate([
        file_name for file_name in os.listdir() if file_name.find(x) != -1
    ]):

        os.rename(
            file_name,
            file_name.replace(x, y)
        )

"""

# ---------------------------------------------------------------- #

image_file_names = [file_name for file_name in os.listdir() if file_name.find('ODEs') != -1]

for image_file_name in image_file_names:

    os.rename(
        image_file_name,
        image_file_name + '.png'
    )

# ---------------------------------------------------------------- #
