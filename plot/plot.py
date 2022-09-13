import matplotlib.pyplot as plt
import numpy as np


def plot(xpoints, ypoints):
    plt.plot(np.array(xpoints), np.array(ypoints))
    plt.show()
