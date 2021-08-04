# Evolutionary Neural Netwrok

We have used an evolutionary algorithm to train an MLP ANN to play the game in this code.

To understand how the code works, you must take a look at these files:
- `Evolution` class and its methods in evolution.py
- `NeuralNetwork` class and its methods in nn.py to
- `think` method in player.py (box list is a queue which objects append to the end. It can be empty when the game just started.)

You can change neural network architecture and other configurations in `config.py`:
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

## How to play


You can play the game with following command:

`python game.py --mode thrust --play True`

If you wnat to play another mode, just replace `thrust` with the desired game-mode name. (helicopter, gravity, thrust)

Also, you can start the game from a checkpoint which you were there before:

`‫‪python‬‬ ‫‪game.py‬‬ ‫‪--mode‬‬ ‫‪$mode$‬‬ ‫‪--checkpoint‬‬ ‫‪checkpoint/$mode$/$gen_num$‬‬`

## how to train

Just run the mentioned command without `--play True`.

After you train a model, you can see the training process by plotting each generation score:

```
>> python plot.py 
>> Enter history file name:evol_history-2021-07-15.18.07.25.csv
```
** This file had been saved in `hist` folder **


## Game Modes
Helicopter             |  Gravity          |  Thrust
:-------------------------:|:-------------------------:|:-------------------------:
![Helicopter](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/helicopter.png?raw=true)  |  ![Gravity](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/gravity.png?raw=true) | ![Thrust](https://github.com/HosseinZaredar/EvolutionaryGames/blob/main/screenshots/thrust.png?raw=true)

## Contributors
- [Ali Faraji](https://github.com/HosseinZaredar)
- [Hossein Zaredar](https://github.com/HosseinZaredar)
- [Matin Tavakoli](https://github.com/MatinTavakoli/) <br>
- Many thanks to [Parnian Rad](https://github.com/Parnian-Rad)

