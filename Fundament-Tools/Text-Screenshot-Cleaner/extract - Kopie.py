# ---------------------------------------------------------------- #

import os

from PIL import Image, ImageGrab

from colors import colors
from PIL_file_extensions import PIL_file_extensions

# ---------------------------------------------------------------- #

def extract(image, min_length = 64, min_height = 64):
    
    """
    extracts text boxes from given image (e.g. of pdf page or such)
    """

    image = image.convert('RGB')

    # stores extracted images of text boxes
    images_extracted = []

    x_min, y_min = 0, 0
    x_max, y_max = image.size

    x_init = x_max // 2
    y = y_min

    while y < y_max:

        # set x to half of image width
        x = x_init

        # check if box might be found
        if image.getpixel((x, y)) != colors['white']:

            # go to upper left corner
            while image.getpixel((x-1, y)) != colors['white']:
                x -= 1

            # save current position
            corner_1 = [x, y]

            # upper left corner might actually be a white dot
            if image.getpixel((corner_1[0]-1, corner_1[1]+1)) != colors['white']:

                # correct corner position, grab the white dot
                corner_1[0] -= 1

            # distance travelled must be high enough
            if abs(x_init - x) >= min_length:

                # go to lower left corner
                while image.getpixel((x, y+1)) != colors['white']:
                    y += 1

                # save current position
                corner_2 = [x, y]

                # lower left corner might actually be a white dot
                if image.getpixel((corner_2[0]+1, corner_2[1]+1)) != colors['white']:

                    # correct corner position, grab the white dot
                    corner_2[1] += 1

                # distance travelled must be high enough
                if abs(y - corner_1[1]) >= min_height:

                    # go to lower right corner
                    while image.getpixel((x+1, y)) != colors['white']:
                        x += 1

                    # save current position
                    corner_3 = [x, y]

                    # lower right corner might actually be a white dot
                    if image.getpixel((corner_3[0]+1, corner_3[1]-1)) != colors['white']:

                        # correct corner position, grab the white dot
                        corner_3[0] += 1

                    image_extracted = image.crop((*corner_1, corner_3[0]+1, corner_3[1]+1))
                    images_extracted.append(image_extracted)

                else:
                    y += 1

            else:
                y += 1

        else:
            y += 1

    return images_extracted

# ---------------------------------------------------------------- #

def extract_from_clipboard(min_length = 64, min_height = 64):
    
    """
    applies extract to image stored in clipboard
    """

    # grab image from clipboard
    image = ImageGrab.grabclipboard()

    # extract text boxes from image
    images_extracted = extract(image, min_length = 64, min_height = 64)

    # show extracted images in default image displayer
    for image_extracted in images_extracted:
        image_extracted.show()

# ---------------------------------------------------------------- #

def extract_from_directory(files = None, min_length = 64, min_height = 64):

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
            images_extracted = extract(image, min_length = 64, min_height = 64)

            # go to output folder
            os.chdir('..' + '/' + 'output')

            # save extracted images in dirctory
            for n, image_extracted in enumerate(images_extracted):
                image_extracted.save(file_name + ' - ' + 'extracted {}'.format(n) + '.png')

            # go to input folder
            os.chdir('..' + '/' + 'input')

# ---------------------------------------------------------------- #

