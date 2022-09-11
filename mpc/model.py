import mesa

class MPCModel(mesa.Model):
    """A model with """

    def __init__(self, N):
        self.num_agents = N
        #self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        # # Create agents
        # for i in range(self.num_agents):
        #     a = MoneyAgent(i, self)
        #     self.schedule.add(a)
        #     # Add the agent to a random grid cell
        #     x = self.random.randrange(self.grid.width)
        #     y = self.random.randrange(self.grid.height)
        #     self.grid.place_agent(a, (x, y))

        # self.datacollector = mesa.DataCollector(
        #     model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        # )

    def step(self):
        # self.datacollector.collect(self)
        self.schedule.step()