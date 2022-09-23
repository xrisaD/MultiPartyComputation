from ttp.server import runTTP
from mpc.server import runMPC
from plot.plot import plot
import random

#num_of_users = range(5, 10, 1)
num_of_users = range(50, 500, 50)
times = []

for u in num_of_users:
    time = []
    for i in range(u):
        time.append(random.randint(30, 70))
    times.append(time)

time_to_compute_mean_TTP = []
time_to_compute_mean_MPC = []

step = 0
for t in times:
    print(step)
    # call TTP
    res = runTTP(times=t, times_to_run_the_experiment=50)
    time_to_compute_mean_TTP.append(res)

    # call MPC
    res = runMPC(times=t, times_to_run_the_experiment=50)
    time_to_compute_mean_MPC.append(res)

    step = step + 1
plot(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC)
