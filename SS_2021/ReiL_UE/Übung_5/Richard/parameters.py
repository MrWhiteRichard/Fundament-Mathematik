parameters_array = [
    {
        'gamma': 0.9,
        'feature info': {'mode': 'polynomials', 'degree': 1},
        'learning method': 'REINFORCE',

        'alpha': 0.1,

        # 'alpha_theta':,
        # 'alpha_w':,

        'episode number max': 100,
    },
    {
        'gamma': 0.9,
        'feature info': {'mode': 'polynomials', 'degree': 1},
        'learning method': 'REINFORCE with Baseline',

        # 'alpha':,

        'alpha_theta': 0.1,
        'alpha_w': 0.01,

        'episode number max': 100,
    },
    {
        'gamma': 0.9,
        'feature info': {'mode': 'polynomials', 'degree': 1},
        'learning method': 'REINFORCE with Baseline',

        # 'alpha':,

        'alpha_theta': 0.1,
        'alpha_w': 0.1,

        'episode number max': 100,
    },
    {
        'gamma': 0.9,
        'feature info': {'mode': 'polynomials', 'degree': 1},
        'learning method': 'REINFORCE with Baseline',

        # 'alpha':,

        'alpha_theta': 0.1,
        'alpha_w': 0.25,

        'episode number max': 100,
    },
    {
        'gamma': 0.9,
        'feature info': {'mode': 'polynomials', 'degree': 1},
        'learning method': 'One-step Actor-Critic',

        # 'alpha':,

        'alpha_theta': 0.1,
        'alpha_w': 0.1,

        'episode number max': 100,
    },
]