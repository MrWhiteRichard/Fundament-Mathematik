colors = {'black': (0, 0, 0), 'white': (255, 255, 255),
          'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

colors_hit = {colors['black']}

# Prof. Grill's special colors
colors_hit.update({colors['red'],   (255, 84, 84),   (255, 186, 186), (255, 100, 100)},
                   colors['green'], (181, 255, 181), (135, 255, 135))