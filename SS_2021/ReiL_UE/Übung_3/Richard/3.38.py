import matplotlib.pyplot as plt

from functions import test_1, test_2
from classes import WindyGridworldKingsMovesStochastic

# test_1(WindyGridworldKingsMovesStochastic, episodes_learn = 2_500, episodes_learned_max = 100_000, sample_size_peak = 1_000_000)

time_steps_observed_max = 8_000

plt.figure()

plt.plot(*test_2(WindyGridworldKingsMovesStochastic, time_steps_observed_max = time_steps_observed_max), label = 'WindyGridworldKingsMovesStochastic')

plt.legend()
plt.show()
