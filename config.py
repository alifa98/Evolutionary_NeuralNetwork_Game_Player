CONFIG = {

    # DO NOT CHANGE
    'WIDTH': 1280,         # width of the window
    'HEIGHT': 720,         # height of the window
    'fps': 50,             # frame/second
    'camera_speed': 8,     # speed of camera
    'box_gap': 9,          # relative gap between box lists
    'MAXIMUM_VELOCITY': 10,  # maximum of velocity for normalization

    # Parameters
    'seed': 0,             # map of the game
    'num_players': 150,    # number of players generated in each step
    'checkpoint_freq': 5,   # the frequency of saving generations
    'crossover_rate': 0.5,  # rate of crossover
    "mutaion_rate": 0.8,    # rate of mutation
    'SUS_in_next_population': False,  # whether to use SUS in next generation selection
    'mutation_mean': 0,  # gaussian distibution mean
    'mutation_standard_deviation': 0.25,  # gaussian distribution SD
    'q_value_for_tournoment': 5,  # q-tournoment parameter in `generate_new_population`

    # ANN setting
    # Note: input & output of network must be handled in `think` method in Player object
    "helicopter_mode_network": [5, 15, 7, 2],
    "gravity_mode_network": [5, 20, 2],
    "thrust_mode_network": [5, 20, 10, 3],
    "activation_function": "sigmoid"  # relu or sigmoid
}
