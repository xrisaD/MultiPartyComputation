from ttp.server import runTTP
from plot.plot import plot


num_of_users = [30, 40, 100]
time_to_compute_mean_TTP = []
time_to_compute_mean_MPC = []

for u in num_of_users:
    # call TTP
    t = runTTP(times=range(u, 0, -1))
    time_to_compute_mean_TTP.append(t)

    # call MPC
    time_to_compute_mean_MPC.append(0)

plot(num_of_users, time_to_compute_mean_TTP, time_to_compute_mean_MPC)