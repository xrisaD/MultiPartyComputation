import mesa
from ttp.agents import Runner, TrustedThirdParty


class TTPModel(mesa.Model):
    """A model with """

    def __init__(self, times):
        self.num_agents = len(times)

        # activates all the agents once per step, in random order
        self.schedule = mesa.time.BaseScheduler(self)
        self.running = True

        # Create runners
        for i, time in zip(range(self.num_agents), times):
            a = Runner(i, self, time)
            self.schedule.add(a)

        # create trusted third party
        ttp = TrustedThirdParty(self.num_agents, self, self.num_agents)
        self.schedule.add(ttp)

    def step(self):
        self.schedule.step()

