import os

substitutions = {}

for x, y in substitutions.items():

    for n, file_name in enumerate([
        file_name for file_name in os.listdir() if file_name.find(x) != -1
    ]):

        os.rename(
            file_name,
            file_name.replace(x, y)
        )
