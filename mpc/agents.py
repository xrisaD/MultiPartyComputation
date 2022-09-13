import mesa


class Runner(mesa.Agent):
    def __init__(self, unique_id, model, time):
        super().__init__(unique_id, model)
        self.time = time

    def step(self):
        pass
