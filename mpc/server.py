import mesa
from mpc.model import MPCModel
from mpc.agents import Runner

params = {"N": range(10, 500, 10)}

results = mesa.BatchRunner(
    MPCModel,
    parameters=params,
    iterations=5,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

