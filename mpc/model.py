import mesa
from mpc.agents import Runner


class MPCModel(mesa.Model):
    """A model with """

    def __init__(self, N):
        self.num_agents = N

        # activates all the agents once per step, in random order
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        # Create agents
        for i in range(self.num_agents):
            a = Runner(i, self, i)
            self.schedule.add(a)

        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        # self.datacollector.collect(self)
        self.schedule.step()
