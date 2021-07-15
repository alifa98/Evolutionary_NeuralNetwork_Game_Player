import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("hist/"+(input("Enter history file name:")), header=None)

plt.plot(data[0], 'g', label='Maximum Fitness')
plt.plot(data[1], 'r', label='Average Fitness')
plt.plot(data[2], 'y', label='Minimum Fitness')
plt.legend(loc="best")
plt.show()
