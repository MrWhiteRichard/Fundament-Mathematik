# ---------- #
# DEPRECATED #
# ---------- #

import tkinter as tk

# write application name
application_name = "Pillow Talk"

# create root of application
root = tk.Tk()

# change application title
root.title(application_name)

# change application icon
root.iconbitmap(os.getcwd() + "//" + "apfel_icon.ico")

# ---------------- #

# write application title text
application_title_text = ""
application_title_text += "\n"
application_title_text += "+-------------+"
application_title_text += "\n"
application_title_text += "| " + application_name + " |"
application_title_text += "\n"
application_title_text += "+-------------+"
application_title_text += "\n"

# create application title label
application_title_label = tk.Label(root, text = application_title_text)

# show application title label on screen
application_title_label.grid(row = 0, column = 0, columnspan = 3)


# ---------------- #

# write application description
application_description_text = ""
application_description_text += "This application trims out edges of images."
application_description_text += "\n"
application_description_text += "You will have to provide one or two parameters!"
application_description_text += "\n"

# pack application description into a label
application_description_label = tk.Label(root, text = application_description_text)

# show application description label on screen
application_description_label.grid(row = 1, column = 0, columnspan = 3)

# ---------------- #

# create trim out color label
trim_out_color_label = tk.Label(root, text = "trim out color ...")

# show trim out color label on screeen
trim_out_color_label.grid(row = 2, column = 0, columnspan = 3)

# create trim out color entries for R, G, B
trim_out_color_entry = [tk.Entry(root), tk.Entry(root), tk.Entry(root)]

# iterate over all trim out color entries
for i in range(3):

    # show trim out color entry i on screen
    trim_out_color_entry[i].grid(row = 3, column = i)

    # set default value for trim out color entry i
    trim_out_color_entry[i].insert(0, "255")

# write trim out color description
trim_out_color_description_text = ""
trim_out_color_description_text += "You must provide the RGB-code of the color of the edges,"
trim_out_color_description_text += "\n"
trim_out_color_description_text += "that you want to get trimmed out!"
trim_out_color_description_text += "\n"

# pack trim out color description into a label
trim_out_color_description_label = tk.Label(root, text = trim_out_color_description_text)

# show trim out color description label on screen
trim_out_color_description_label.grid(row = 4, column = 0, columnspan = 3)

# ---------------- #

# runs trim_from_clipboard with current RGB-values from entry boxes
def trim_from_clipboard_tkinter():

    # get trim out color from entry boxes
    trim_out_color = [int(trim_out_color_entry[i].get()) for i in range(3)]
    trim_out_color = tuple(trim_out_color)

    # run original function
    return trim_from_clipboard(trim_out_color)

# create trim from clipboard button
trim_from_clipboard_button = tk.Button(root, text = "trim from clipboard", command = trim_from_clipboard_tkinter)

# show trim from clipboard button on screen
trim_from_clipboard_button.grid(row = 5, column = 0, columnspan = 3)

# write trim from clipboard description
trim_from_clipboard_description_text = ""
trim_from_clipboard_description_text += "Make shure, you have the image,"
trim_from_clipboard_description_text += "\n"
trim_from_clipboard_description_text += "from which you want to trim away the edges,"
trim_from_clipboard_description_text += "\n"
trim_from_clipboard_description_text += "saved to your clipboard!"
trim_from_clipboard_description_text += "\n"

# pack trim from clipboard description into a label
trim_from_clipboard_description_label = tk.Label(root, text = trim_from_clipboard_description_text)

# show trim from clipboard description label on screen
trim_from_clipboard_description_label.grid(row = 6, column = 0, columnspan = 3)

# ---------------- #

# create image folder label
image_folder_label = tk.Label(root, text = "image folder ...")

# show image folder label on screeen
image_folder_label.grid(row = 7, column = 0, columnspan = 3)

# create image folder entry
image_folder_entry = tk.Entry(root)

# show image folder entry on screen
image_folder_entry.grid(row = 8, column = 0, columnspan = 3)

# set default value for image folder entry
image_folder_entry.insert(0, "images")

# write image folder description
image_folder_description_text = ""
image_folder_description_text += "You must provide the name of the folder in your application directory,"
image_folder_description_text += "\n"
image_folder_description_text += "where your images are stored (as .PNG or .png)!"
image_folder_description_text += "\n"

# pack trim out color description into a label
image_folder_description_label = tk.Label(root, text = image_folder_description_text)

# show trim out color description label on screen
image_folder_description_label.grid(row = 9, column = 0, columnspan = 3)

# ---------------- #

# runs trim_from_directory with current image folder from entry box
def trim_from_directory_tkinter():

    # get trim out color from entry boxes
    trim_out_color = [int(trim_out_color_entry[i].get()) for i in range(3)]
    trim_out_color = tuple(trim_out_color)

    # get image folder from entry box
    image_folder = "\\" + image_folder_entry.get()

    # run original function
    return trim_from_directory(trim_out_color, image_folder)

# create trim from directory button
trim_from_directory_button = tk.Button(root, text = "trim from directory", command = trim_from_directory_tkinter)

# show trim from directory button on screen
trim_from_directory_button.grid(row = 10, column = 0, columnspan = 3)

# write trim from directory description
trim_from_directory_description_text = ""
trim_from_directory_description_text += "Make shure, you have the images,"
trim_from_directory_description_text += "\n"
trim_from_directory_description_text += "from which you want to trim away the edges"
trim_from_directory_description_text += "\n"
trim_from_directory_description_text += "saved to your image folder (as .PNG or .png)!"
trim_from_directory_description_text += "\n"

# pack trim from clipboard description into a label
trim_from_directory_description_label = tk.Label(root, text = trim_from_directory_description_text)

# show trim from clipboard description label on screen
trim_from_directory_description_label.grid(row = 11, column = 0, columnspan = 3)

# ---------------- #

root.mainloop()

# ---------------- #