from ttp.server import runTTP
from plot.plot import plot


num_of_users = [30, 40, 50]
time_to_compute_mean = []

for u in num_of_users:
    t = runTTP(times=range(u, 0, -1))
    time_to_compute_mean.append(t)

plot(num_of_users, time_to_compute_mean)