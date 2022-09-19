import mesa
from mpc.agents import Runner


class MPCModel(mesa.Model):
    """A model with """

    def __init__(self, times):
        self.num_agents = len(times)

        # activates all the agents once per step, in random order
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True

        # Create runners
        # with ids = 1.. N
        # Create runners
        for i, time in zip(range(self.num_agents), times):
            a = Runner(i+1, self, time, self.num_agents)
            self.schedule.add(a)
        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        # self.datacollector.collect(self)
        self.schedule.step()
