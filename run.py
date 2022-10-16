from ttp.server import runTTP
from mpc.server import runMPC
from plot.fitdata import fitMPC, fitTTP
from plot.plot import plot1, plot2, plotFit
import random


num_of_users = range(5, 55, 5)
mins = []


times = []
for u in num_of_users:
    time = []
    for i in range(u):
        time.append(random.randint(30, 70))
    times.append(time)

time_to_compute_mean_TTP = []
time_to_compute_mean_MPC_3 = []
time_to_compute_mean_MPC_all = []

step = 0
for t in times:
    print(step)
    # call TTP
    res = runTTP(times=t, times_to_run_the_experiment=30)
    time_to_compute_mean_TTP.append(res)

    # call MPC with minimun = 3
    res = runMPC(times=t, times_to_run_the_experiment=30, minimum=3)
    time_to_compute_mean_MPC_3.append(res)

    # call MPC with minimun = number of users
    res = runMPC(times=t, times_to_run_the_experiment=30, minimum=len(t))
    time_to_compute_mean_MPC_all.append(res)

    step = step + 1

x_all, y_all, params_all = fitMPC(num_of_users, time_to_compute_mean_MPC_all)
print("MPC ALL: " + str(params_all))
x_3, y_3, params_3 = fitMPC(num_of_users, time_to_compute_mean_MPC_3)
print("MPC 3: " + str(params_3))
x_TTP, y_TTP, params_TTP = fitTTP(num_of_users, time_to_compute_mean_TTP)
print("TTP: " + str(params_TTP))


plotFit(num_of_users, time_to_compute_mean_TTP, x_TTP, y_TTP, ["TTP", "fitted curve for TTP"])
plotFit(num_of_users, time_to_compute_mean_MPC_3, x_3, y_3, ["MPC, minimum = 3", "fitted curve for MPC, minimum = 3"])
plotFit(num_of_users, time_to_compute_mean_MPC_all, x_all, y_all, ["MPC, minimum = number of users", "fitted curve for MPC, minimum = number of users"])

plot1(num_of_users, time_to_compute_mean_TTP, x_TTP, y_TTP,  num_of_users, time_to_compute_mean_MPC_3, x_3, y_3, ["TTP", "fitted curve for TTP", "MPC, minimum = 3", "fitted curve for MPC, minimum = 3"])
plot1(num_of_users, time_to_compute_mean_TTP, x_TTP, y_TTP, num_of_users, time_to_compute_mean_MPC_all, x_all, y_all, ["TTP", "fitted curve for TTP", "MPC, minimum = number of users", "fitted curve for MPC, minimum = number of users"])
plot1(num_of_users, time_to_compute_mean_MPC_3, x_3, y_3, num_of_users, time_to_compute_mean_MPC_all, x_all, y_all, ["MPC, minimum = 3", "fitted curve for MPC, minimum = 3", "MPC, minimum = number of users", "fitted curve for MPC, minimum = number of users"])
#plot2(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC_3, time_to_compute_mean_MPC_all)
