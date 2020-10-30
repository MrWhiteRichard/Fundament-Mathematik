import os

substitutions = {
    'Hetzl': 'DGA',
    'Kaltenbaeck': 'Ana1&2',
    'Grill': 'MassWHT1&2'
}

for x, y in substitutions.items():

    for file_name in os.listdir():

        if file_name.find(x) != -1:

            os.rename(
                file_name,
                file_name.replace(x, y)
            )