from ttp.server import runTTP
from mpc.server import runMPC
from plot.plot import plot1, plot2
import random

#num_of_users = range(5, 10, 1)
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

plot1(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC_3, ["TTP", "MPC, minimum = 3"])
plot1(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC_all, ["TTP", "MPC, minimum = number of runners"])
plot1(num_of_users, time_to_compute_mean_MPC_3, time_to_compute_mean_MPC_all, ["MPC, minimum = 3", "MPC, minimum = number of runners"])
#plot2(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC_3, time_to_compute_mean_MPC_all)
