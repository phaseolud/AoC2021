import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(11)
        self.data = dataloader.load_data(debug=False, data_type='int', delimiter=1)
        self.n_octopus = self.data.size

    def first_solution(self) -> int:
        total_flashes = 0
        octopus = np.pad(np.copy(self.data), 1, mode='constant', constant_values=-2147483648)
        for day in range(100):
            has_flashed, octopus, total_flashes = self.simulate_octopus_timestep(octopus, total_flashes)
            octopus = (1 - has_flashed) * octopus
        return total_flashes

    def simulate_octopus_timestep(self, octopus, total_flashes):
        has_flashed = np.zeros(octopus.shape, dtype='int')
        octopus += 1
        while True:
            tf_prev = total_flashes
            nines = np.where((1 - has_flashed) * octopus > 9)

            for n in range(len(nines[0])):
                nine_loc = (nines[0][n], nines[1][n])
                octopus[nine_loc[0] - 1:nine_loc[0] + 2, nine_loc[1] - 1:nine_loc[1] + 2] += 1
                has_flashed[tuple(nine_loc)] = 1
                total_flashes += 1
            if tf_prev == total_flashes:
                break
        return has_flashed, octopus, total_flashes

    def first_answer(self) -> int:
        return 1632

    def second_solution(self) -> int:
        total_flashes = 0
        octopus = np.pad(np.copy(self.data), 1, mode='constant', constant_values=-2147483648)
        step = 0
        while True:
            step += 1
            has_flashed, octopus, total_flashes = self.simulate_octopus_timestep(octopus, total_flashes)
            octopus = (1 - has_flashed) * octopus
            if has_flashed[1:-1, 1:-1].sum() == self.n_octopus:
                return step

    def second_answer(self) -> int:
        return 303


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
