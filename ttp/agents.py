import mesa

from statistics import mean


class TrustedThirdParty(mesa.Agent):
    def __init__(self, unique_id, model, totalRunners):
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)
        self.values = []
        self.totalRunners = totalRunners

    def step(self):
        # if the ttp has the time of all runners' times
        if len(self.values) == self.totalRunners:
            # compute the mean value
            m = mean(self.values)
            # share it with the runners
            for a in self.model.schedule.agents:
                a.mean = m


class Runner(mesa.Agent):
    def __init__(self, unique_id, model, time):
        # initialize the parent class with required parameters
        super().__init__(unique_id, model)
        self.time = time
        self.mean = 0
        self.s = 0

    def step(self):
        if self.s == 0:
            ttp = self.model.schedule.agents[-1]
            ttp.values.append(self.time)
            self.s = 1
