import matplotlib.pyplot as plt
import numpy as np


def plotFit(x, y, x_line, y_line, labels):
    plt.scatter(np.array(x), np.array(y), label=labels[0])
    plt.plot(x_line, y_line, '--', color='red', label=labels[1])

    plt.xlabel('number of runners')
    plt.ylabel('time to compute the meantime (sec)', labelpad=0)
    plt.legend()
    plt.show()


def plot1(x1, y1, x_line1, y_line1, x2, y2, x_line2, y_line2, labels):
    plt.scatter(np.array(x1), np.array(y1), label=labels[0])
    plt.plot(x_line1, y_line1, '--', color='red', label=labels[1])

    plt.scatter(np.array(x2), np.array(y2), label=labels[2], color="orange", marker='s')
    plt.plot(x_line2, y_line2, '-', color='red', label=labels[3])
    plt.xlabel('number of runners')
    plt.ylabel('time to compute the meantime (sec)', labelpad=0)
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
