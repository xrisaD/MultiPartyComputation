import matplotlib.pyplot as plt
import numpy as np


def plot(x, y_ttp, y_mpc):
    plt.plot(np.array(x), np.array(y_ttp), label="TTP")
    plt.plot(np.array(x), np.array(y_mpc), label="MPC")
    plt.xlabel('number of users')
    plt.ylabel('time to compute the meantime (sec)')
    plt.legend()
    plt.show()
