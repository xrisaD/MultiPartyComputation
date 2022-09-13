import mesa
import timeit
from ttp.model import TTPModel
from statistics import mean

# TTP needs to steps to run
# empty_model = TPPModel(10)
# empty_model.step()
# empty_model.step()

# This runs the model 100 times, each model executing 2 steps.
def runTTP(times_to_run_the_experiment=100, times=None, times_range=None):
    if times is None and times_range is None:
        raise Exception("times or times_range should not be none")

    if times is None:
        times = range(times_range)

    res = []
    for j in range(times_to_run_the_experiment):
        # Run the model
        model = TTPModel(times)
        start = timeit.default_timer()
        for i in range(2):
            model.step()
        stop = timeit.default_timer()
        res.append(stop-start)
    return mean(res)