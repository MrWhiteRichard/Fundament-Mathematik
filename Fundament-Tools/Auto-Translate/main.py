# ---------------------------------------------------------------- #

import os
import codecs

from dictionary import dictionary

# ---------------------------------------------------------------- #

def translate(file_name_old, file_name_new):

    if os.path.splitext(file_name_old)[1] == '':
        file_name_old += '.tex'

    if os.path.splitext(file_name_new)[1] == '':
        file_name_new += '.tex'

    with codecs.open(file_name_old, 'r', 'utf-8') as file:
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

    with codecs.open(file_name_new, 'w', 'utf-8') as file:
        file.writelines(file_content_en)

# ---------------------------------------------------------------- #

print('Moving to folder "Fundament-LaTeX" ...')
go_somewhere_else = input('Would you like to go somewhere else ("yes" / "no")? ...' + ' ')

if go_somewhere_else == 'yes':

    path = input('Please input the desired destination path ...' + ' ')
    os.chdir(path)

else:

    while os.path.basename(os.getcwd()) != 'Fundament-Mathematik':
        os.chdir('..')

    os.chdir('Fundament-LaTeX')

print('What file would you like to translate from german to english?')

file_name_old = input('Old file name:' + ' ')
file_name_new = input('New file name:' + ' ')

translate(file_name_old, file_name_new)

# ---------------------------------------------------------------- #
