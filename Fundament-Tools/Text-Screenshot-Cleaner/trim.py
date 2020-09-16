# ---------------------------------------------------------------- #

import os

from PIL import Image, ImageGrab


from colors import colors
from PIL_file_extensions import PIL_file_extensions

# ---------------------------------------------------------------- #

def trim(image, trim_out_color = colors['white']):

    image = image.convert('RGB')

    x_min, y_min = 0, 0
    x_max, y_max = image.size
    x_max -= 1
    y_max -= 1

    # -------------------------------- #

    # find left bound for x
    def f_1():

        x = x_min
        y = y_min

        while image.getpixel((x, y)) == trim_out_color:
            if y < y_max:
                y += 1
            else:
                y = y_min
                if x < x_max:
                    x += 1

        return x

    # -------------------------------- #

    # find upper bound for y
    def f_2():

        x = x_min
        y = y_min

        while image.getpixel((x, y)) == trim_out_color:
            if x < x_max:
                x += 1
            else:
                x = x_min
                if y < y_max:
                    y += 1

        return y

    # -------------------------------- #

    # find right bound for x
    def f_3():

        x = x_max
        y = y_max

        while image.getpixel((x, y)) == trim_out_color:
            if y > 0:
                y -= 1
            else:
                y = y_max
                if x > 0:
                    x -= 1

        return x + 1

    # -------------------------------- #

    # find lower bound for y
    def f_4():

        x = x_max
        y = y_max

        while image.getpixel((x, y)) == trim_out_color:
            if x > 0:
                x -= 1
            else:
                x = x_max
                if y > 0:
                    y -= 1

        return y + 1

    # -------------------------------- #

    image_trimmed = image.crop(tuple([f() for f in [f_1, f_2, f_3, f_4]]))

    return image_trimmed

# ---------------------------------------------------------------- #

def trim_from_clipboard_to_display(trim_out_color = colors['white']):

    # grab image from clipboard
    image = ImageGrab.grabclipboard()

    # trim out the border color
    image_trimmed = trim(image, trim_out_color)

    # show cropped image in default image displayer
    image_trimmed.show()

# ---------------------------------------------------------------- #

from stackoverflow import send_to_clipboard

def trim_from_clipboard_to_clipboard(trim_out_color = colors['white']):

    # grab image from clipboard
    image = ImageGrab.grabclipboard()

    # trim out the border color
    image_trimmed = trim(image, trim_out_color)

    # send cropped image to clipboard
    send_to_clipboard(image_trimmed)

# ---------------------------------------------------------------- #

def trim_from_directory_to_directory(files = None, trim_out_color = colors['white']):

    # go to input folder
    os.chdir('input')
    
    if files == None:
        files = os.listdir()

    for file in files:
        
        # isolate name and extension
        file_name, file_extension = os.path.splitext(file)

        # check if file has desired extension
        if file_extension in PIL_file_extensions:

            print('trimming', file, '...')

            # import image from directory
            image = Image.open(file)

            # trim out the border color
            image_trimmed = trim(image, trim_out_color)

            # go to output folder
            os.chdir('..' + '/' + 'output')

            # save cropped image in dirctory
            image_trimmed.save(file_name + '.png')

            # go to input folder
            os.chdir('..' + '/' + 'input')

# ---------------------------------------------------------------- #