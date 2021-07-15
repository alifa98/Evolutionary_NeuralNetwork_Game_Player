CONFIG = {

    # DO NOT CHANGE
    'WIDTH': 1280,         # width of the window
    'HEIGHT': 720,         # height of the window
    'fps': 50,             # frame/second
    'camera_speed': 8,     # speed of camera
    'box_gap': 9,          # relative gap between box lists

    # Parameters
    'seed': 0,             # map of the game
    'num_players': 150,    # number of players generated in each step
    'checkpoint_freq': 5,   # the frequency of saving generations
    'crossover_rate': 0.5,  # rate of crossover
    "mutaion_rate": 0.8,    # rate of mutation
    'SUS_in_next_population': True,  # whether to use SUS in next generation selection
    'mutation_mean': 0,
    'mutation_standard_deviation': 0.1,
}
