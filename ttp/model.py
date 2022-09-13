import mesa
from ttp.agents import Runner, TrustedThirdParty


class TPPModel(mesa.Model):
    """A model with """

    def __init__(self, N):
        self.num_agents = N

        # activates all the agents once per step, in random order
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True

        # Create runners
        for i in range(self.num_agents):
            a = Runner(i, self, i)
            self.schedule.add(a)

        # create trusted third party
        ttp = TrustedThirdParty(self.num_agents, self, self.num_agents)
        self.schedule.add(ttp)

        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        # self.datacollector.collect(self)
        self.schedule.step()

