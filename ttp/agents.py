import mesa


class TrustedThirdParty(mesa.Agent):
    def __init__(self, unique_id, model):
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)


class Runner(mesa.Agent):
    def __init__(self, unique_id, model):
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)

    def step(self):
        pass