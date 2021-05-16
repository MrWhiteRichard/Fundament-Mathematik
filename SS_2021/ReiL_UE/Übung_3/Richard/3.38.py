from functions import test
from classes import WindyGridworldKingsMovesStochastic

test(WindyGridworldKingsMovesStochastic, episodes_learn = 2_500, episodes_learned_max = 100_000, sample_size_peak = 1_000_000)
