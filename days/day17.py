import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(17)
        self.data = dataloader.load_data(debug=False, data_type='str')
        x_target_l = list(map(int, self.data[2][2:-1].split("..")))
        y_target_l = list(map(int, self.data[3][2:].split("..")))
        self.x_target_r = range(x_target_l[0], x_target_l[1] + 1)
        self.y_target_r = range(y_target_l[0], y_target_l[1] + 1)

        self.sign = lambda x: x and (1, -1)[int(x < 0)]

        self.vy_possible = []
        self.vx_possible = []

    def first_solution(self) -> int:
        # use the fact that the location x and y are independent, so we first search for a
        # highest y such that we have an y in the range, and move x accordingly
        self.scan_velocities_ind()
        vy_max = self.vy_possible[-1]
        y_max = self.simulate_trajectory(np.array([0, vy_max]), 'y')
        return y_max

    def scan_velocities_ind(self):
        vy_possible = []
        vx_possible = []
        for vy in range(-200, 500):
            v = np.array([0, vy])
            if self.simulate_trajectory(v, 'y') is not None: vy_possible.append(vy)
        for vx in range(0, 200):
            v = np.array([vx, 0])
            if self.simulate_trajectory(v, 'x'): vx_possible.append(vx)
        self.vy_possible = vy_possible
        self.vx_possible = vx_possible

    def simulate_trajectory(self, v, direction):
        s = np.array([0, 0])
        y_max = 0
        while s[1] >= min(self.y_target_r):
            y_max = max(s[1], y_max)
            s, v = self.simulate_timestep(s, v)
            if s[1] in self.y_target_r and direction == 'y':
                return y_max
            elif s[0] in self.x_target_r and direction == 'x':
                return True
            elif s[0] in self.x_target_r and s[1] in self.y_target_r and direction == 'xy':
                return True
        return None

    def first_answer(self) -> int:
        return 15931

    def second_solution(self) -> int:
        n_paths = 0
        if not (self.vx_possible and self.vy_possible):
            self.scan_velocities_ind()
        for vx in self.vx_possible:
            for vy in self.vy_possible:
                v = np.array([vx, vy])
                if self.simulate_trajectory(v, 'xy'): n_paths += 1
        return n_paths

    def second_answer(self) -> int:
        return 2555

    def simulate_timestep(self, s, v):
        s += v
        v -= [self.sign(v[0]), 1]
        return s, v


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
