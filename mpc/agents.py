import mesa
from mpc.shamir import make_random_shares, recover_secret


class Runner(mesa.Agent):
    def __init__(self, unique_id, model, time, number_of_users):
        super().__init__(unique_id, model)
        self.time = time
        self.s = 0
        self.others = []
        self.points = []
        self.mean = 0
        self.number_of_users = number_of_users
        # compute shares
        self.shares = make_random_shares(self.time, minimum=3, shares=number_of_users)

    def step(self):
        pass
        # share the shares with the right users
        # based on the id of the user
        if self.s == 0:
            agents = self.model.schedule.agents
            for agent, share in zip(agents, self.shares):
                agent.others.append(share[1])
            self.s = 1
        elif self.s == 1:  # step == 1
            point = (self.unique_id, sum(self.others))
            for agent in self.model.schedule.agents:
                agent.points.append(point)
            self.s = 2
        else:
            self.mean = recover_secret(self.points)/self.number_of_users
            #print("MEAN:", self.mean)