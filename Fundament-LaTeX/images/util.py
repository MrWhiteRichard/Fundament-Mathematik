import os
import codecs

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

"""

image_file_names = [file_name for file_name in os.listdir() if file_name.find('ODEs') != -1]

for image_file_name in image_file_names:

    os.rename(
        image_file_name,
        image_file_name + '.png'
    )

"""

# ---------------------------------------------------------------- #

with codecs.open('ODEs.txt', 'r', 'utf-8') as file:
    content = file.read()
    content = content.split('\r\n')

for n in range(90):

    os.rename(
        f'ODEs - {n+1}.png',
        f'ODEs - {content[n]}.png'
    )

# ---------------------------------------------------------------- #
