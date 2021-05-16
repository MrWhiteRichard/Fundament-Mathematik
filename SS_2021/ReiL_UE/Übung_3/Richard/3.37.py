import matplotlib.pyplot as plt

from functions import test_1, test_2
from classes import WindyGridworldKingsMoves, WindyGridworldKingsMovesStationary

# test_1(WindyGridworldKingsMoves)
# test_1(WindyGridworldKingsMovesStationary)

time_steps_observed_max = 8_000

plt.figure()

plt.plot(*test_2(WindyGridworldKingsMoves,           time_steps_observed_max = time_steps_observed_max), label = 'WindyGridworldKingsMoves')
plt.plot(*test_2(WindyGridworldKingsMovesStationary, time_steps_observed_max = time_steps_observed_max), label = 'WindyGridworldKingsMovesStationary')

plt.legend()
plt.show()
