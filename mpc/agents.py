import mesa
from mpc.shamir import make_random_shares, recover_secret


class Runner(mesa.Agent):
    def __init__(self, unique_id, model, time, number_of_users, minimum):
        self.minimum = minimum
        super().__init__(unique_id, model)
        self.time = time
        self.s = 0
        self.others = []
        self.points = []
        self.mean = 0
        self.number_of_users = number_of_users
        # compute shares
        self.shares = make_random_shares(self.time, minimum=self.minimum, shares=self.number_of_users)

    def step(self):
        # share the shares with the right users
        # based on the id of the user
        if self.s == 0:
            agents = self.model.schedule.agents
            for agent, share in zip(agents, self.shares):
                agent.others.append(share[1])
            self.s = 1
        elif self.s == 1:  # step == 1
            point = (self.unique_id, sum(self.others))
            all_agents = self.model.schedule.agents
            for agent_id in range(self.unique_id, self.unique_id - self.minimum, -1):
                all_agents[agent_id-1].points.append(point)
            self.s = 2
        else:
            self.mean = recover_secret(self.points)/self.number_of_users
            # print("MEAN:", self.mean)