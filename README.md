# Evolutionary Neural Netwrok

We have used an evolutionary algorithm to train an MLP ANN to play the game in this code.

To understand how the code works, you must take a look at these files:
- `Evolution` class and its methods in evolution.py
- `NeuralNetwork` class and its methods in nn.py to
- `think` method in player.py (box list is a queue which objects append to the end. It can be empty when the game just started.)

You can change neural network architecure and other configurations in `config.py`:
```
    # Parameters
    'seed': 0,             # map of the game
    'num_players': 150,    # number of players generated in each step
    'checkpoint_freq': 5,   # the frequency of saving generations
    'crossover_rate': 0.5,  # rate of crossover
    "mutaion_rate": 0.8,    # rate of mutation
    'SUS_in_next_population': False,  # whether to use SUS in next generation selection
    'mutation_mean': 0,  # gaussian distibution mean
    'mutation_standard_deviation': 0.3,  # gaussian distribution SD
    'q_value_for_tournoment': 5,  # q-tournoment parameter in `generate_new_population`

    # ANN setting
    # Note: input & output of network must be handled in `think` method in Player object
    "helicopter_mode_network": [5, 15, 7, 2],
    "gravity_mode_network": [5, 20, 2],
    "thrust_mode_network": [5, 20, 7, 3],
    "activation_function": "sigmoid"  # relu or sigmoid
```



## Game Modes
Helicopter             |  Gravity          |  Thrust
:-------------------------:|:-------------------------:|:-------------------------:
![Helicopter](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/helicopter.png?raw=true)  |  ![Gravity](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/gravity.png?raw=true) | ![Thrust](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/thrust.png?raw=true)

## Contributors
- [Ali Faraji](https://github.com/HosseinZaredar)
- [Hossein Zaredar](https://github.com/HosseinZaredar)
- [Matin Tavakoli](https://github.com/MatinTavakoli/) <br>
- Many thanks to [Parnian Rad](https://github.com/Parnian-Rad)

