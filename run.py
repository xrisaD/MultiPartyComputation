from ttp.server import runTTP
from mpc.server import runMPC
from plot.plot import plot


num_of_users = [5, 10, 100]


time_to_compute_mean_TTP = []
time_to_compute_mean_MPC = []

for u in num_of_users:
    # call TTP
    t = runTTP(times=range(u, 0, -1), times_to_run_the_experiment=50)
    time_to_compute_mean_TTP.append(t)

    # call MPC
    t = runMPC(times=range(u, 0, -1), times_to_run_the_experiment=50)
    time_to_compute_mean_MPC.append(t)

plot(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC)