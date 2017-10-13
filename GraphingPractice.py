import matplotlib.pyplot as plt
import numpy as np

upperBound = input('Enter a upper bound for randomizer: ')

bound = int(upperBound)

x = np.arange(0,bound,0.1);
y = np.sin(x)

plt.show(plt.plot(x,y))
