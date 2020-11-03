import os

image_file_names = [file_name for file_name in os.listdir() if '.png' != -1]

for image_file_name in image_file_names:

    os.rename(
        image_file_name,
        'MassWHT1&2' + ' - ' + image_file_name
    )