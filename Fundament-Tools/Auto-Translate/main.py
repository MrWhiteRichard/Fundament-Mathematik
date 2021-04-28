# ---------------------------------------------------------------- #

import os
import codecs

from dictionary import dictionary

# ---------------------------------------------------------------- #

while os.path.basename(os.getcwd()) != 'Fundament-Mathematik':
    os.chdir('..')

os.chdir('Fundament-LaTeX')

# ---------------------------------------------------------------- #

def translate(file_name):

    assert file_name in ['macros', 'packages', 'environments']

    with codecs.open(file_name + '_de' + '.tex', 'r', 'utf-8') as file:
        file_content_de = file.readlines()

    file_content_en = file_content_de

    for index, line in enumerate(file_content_en):
        for expression_de, expression_en in dictionary.items():
            if expression_de in line:
                if expression_en == None:
                    file_content_en.pop(index)
                else:
                    file_content_en[index] = line.replace(
                        expression_de,
                        expression_en
                    )

    with codecs.open(file_name + '_en' + '.tex', 'w', 'utf-8') as file:
        file.writelines(file_content_en)

# ---------------------------------------------------------------- #

file_name = input('What file would you like to translate from german to english (macros / packages / environments)? ... ')
translate(file_name)

# ---------------------------------------------------------------- #
