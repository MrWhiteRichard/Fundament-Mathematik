# ---------------------------------------------------------------- #

import os

from PIL import Image, ImageGrab

from colors import *
from PIL_file_extensions import *

# ---------------------------------------------------------------- #

increments = {'left': -1, 'right': 1, 'up': -1, 'down': 1}

def go_horizontal(image, point_start, direction):

    """
    returns left / right most point
    lying on horizontal line
    passing through given starting point
    on image
    """

    # assert direction
    assert direction in {'left', 'right'}

    # get color of starting pixel
    color = image.getpixel(point_start)

    # extract coordinates
    x, y = point_start

    # go left / right
    # point might be differently colored pixel but still relevant
    while color in [image.getpixel((x+increments[direction], y+sign)) for sign in [-1, 0, 1]]:
        x += increments[direction]

    point_end = (x, y)
    return point_end

def go_vertical(image, point_start, direction):

    """
    returns upper / lower most point
    lying on vertical line
    passing through given starting point
    on image
    """

    # assert direction
    assert direction in {'up', 'down'}

    # get color of starting pixel
    color = image.getpixel(point_start)

    # extract coordinates
    x, y = point_start

    # go left / right
    # point might be differently colored pixel but still relevant
    while color in [image.getpixel((x+sign, y+increments[direction])) for sign in [-1, 0, 1]]:
        y += increments[direction]

    point_end = (x, y)
    return point_end

def get_width(image, point):

    """
    returns maximum length of
    single colored horizontal line
    passing through given point
    on image
    """

    # get left corner
    corner_left = go_horizontal(image, point, 'left')

    # get right corner
    corner_right = go_horizontal(image, point, 'right')

    return abs(corner_right[0] - corner_left[0])

def get_height(image, point):

    """
    returns maximum length of
    single colored vertical line
    passing through given point
    on image
    """

    # get upper corner
    corner_upper = go_vertical(image, point, 'up')

    # get lower corner
    corner_lower = go_vertical(image, point, 'down')

    return abs(corner_lower[1] - corner_upper[1])

def extract(image, min_length = 64):
    
    """
    extracts text boxes from given image (e.g. of pdf page)
    """

    image = image.convert('RGB')

    # stores extracted images of text boxes
    images_extracted = []

    # start at upper center
    x = image.size[0] // 2
    y = 0

    while y < image.size[1]:

        # checking if text box was hit
        if image.getpixel((x, y)) == colors['black']:
            print(f'pixel was hit @ {(x, y)} with color {image.getpixel((x, y))}')

            # store information of pixel pixel hit
            point_hit = (x, y)

            width = get_width(image, (x, y))
            if width >= min_length:
                print('wide enough')

                x, y = go_horizontal(image, (x, y), 'left')

                height = get_height(image, (x, y))
                if height >= min_length:
                    print('high enough')

                    x, y = go_vertical(image, (x, y), 'up')

                    image_extracted = image.crop((x, y, x+width, y+height))
                    images_extracted.append(image_extracted)
                    print('appended image')

                x, y = point_hit
                y += 1 + height
            else:
                x, y = point_hit
                y += 1
        else:
            y += 1

    return images_extracted

# ---------------------------------------------------------------- #

def extract_from_clipboard_to_display(min_length = 64):
    
    """
    applies extract to image stored in clipboard
    """

    # grab image from clipboard
    image = ImageGrab.grabclipboard()

    # extract text boxes from image
    images_extracted = extract(image, min_length)

    # show extracted images in default image displayer
    for image_extracted in images_extracted:
        image_extracted.show()

# ---------------------------------------------------------------- #

def extract_from_directory_to_directory(files = None, min_length = 64):

    """
    applies extract to files in input folder and
    stores extracted images in output folder
    
    files:
    files extract is applied to
    If none are specified, all will be used.
    """

    # go to input folder
    os.chdir('input')
    
    if files == None:

        # will apply extract to all files
        files = os.listdir()

    for file in files:

        # isolate name and extension
        file_name, file_extension = os.path.splitext(file)

        # check if file has desired extension
        if file_extension in PIL_file_extensions:

            print('extracting', file, '...')

            # import image from directory
            image = Image.open(file)

            # trim out the border color
            images_extracted = extract(image, min_length)

            # go to output folder
            os.chdir('..' + '/' + 'output')

            # save extracted images in dirctory
            for n, image_extracted in enumerate(images_extracted):
                image_extracted.save(file_name + ' - ' + f'extracted {n}' + '.png')

            # go to input folder
            os.chdir('..' + '/' + 'input')

# ---------------------------------------------------------------- #
