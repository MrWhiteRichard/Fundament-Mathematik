# ---------------------------------------------------------------- #

import os
import codecs

# ---------------------------------------------------------------- #

def substitute(substitutions):

    for x, y in substitutions.items():

        for n, file_name in enumerate([
            file_name for file_name in os.listdir() if file_name.find(x) != -1
        ]):

            os.rename(
                file_name,
                file_name.replace(x, y)
            )

# ---------------------------------------------------------------- #

def rename(LVA):

    os.chdir(LVA)

    with codecs.open(LVA + '.txt', 'r', 'utf-8') as file:
        content = file.read().split('\r\n')

    for n, title in enumerate(content):

        os.rename(
            f'{n}.png',
            f'{LVA} - {title}.png'
        )

# ---------------------------------------------------------------- #
