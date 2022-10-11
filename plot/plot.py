import matplotlib.pyplot as plt
import numpy as np


def plot1(x, y_ttp, y_mpc, labels):
    plt.scatter(np.array(x), np.array(y_ttp), label=labels[0])
    plt.scatter(np.array(x), np.array(y_mpc), label=labels[1],
            marker ="s")
    plt.xlabel('number of runners')
    plt.ylabel('time to compute the meantime (sec)')
    plt.legend()
    plt.show()


def plot2(x, y_ttp, y_mpc, y_mpc2):
    plt.plot(np.array(x), np.array(y_ttp), label="TTP")
    plt.plot(np.array(x), np.array(y_mpc), label="MPC, minimum = 3")
    plt.plot(np.array(x), np.array(y_mpc2), label="MPC, minimum = number of runners")
    plt.xlabel('number of runners')
    plt.ylabel('time to compute the meantime (sec)')
    plt.legend()
    plt.show()
