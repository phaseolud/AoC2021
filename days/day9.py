import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        self.directions = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
        self.min_height_locations = []
        self.visited_locations = np.array([])
        dataloader = DataLoader(9)
        self.data = dataloader.load_data(data_type='int', debug=False, delimiter=1)
        self.data_padded = np.pad(self.data, 1, mode='constant', constant_values=9)

    def first_solution(self) -> int:
        height, width = self.data.shape
        min_height = []
        min_height_locations = []
        for n in range(1, height + 1):
            for m in range(1, width + 1):
                neighbors = self.get_neighbors(m, n)
                if np.min(neighbors) > self.data_padded[n, m]:
                    min_height.append(self.data_padded[n, m] + 1)
                    min_height_locations.append([n, m])
        self.min_height_locations = min_height_locations
        return sum(min_height)

    def get_neighbors(self, m, n):
        neighbors = [self.data_padded[n - 1, m], self.data_padded[n + 1, m], self.data_padded[n, m - 1],
                     self.data_padded[n, m + 1]]
        return neighbors

    def first_answer(self) -> int:
        return 603

    def second_solution(self) -> int:
        # a bit dirty because we are dependent of the first function to run first...
        basin_sizes = []
        for (n_min, m_min) in self.min_height_locations:
            self.visited_locations = np.array([[n_min, m_min]])
            self.take_steps([n_min, m_min])
            basin_sizes.append(len(self.visited_locations))
        return int(np.prod(np.sort(basin_sizes)[-3:]))

    def take_steps(self, current_location):
        for direction in self.directions:
            new_location = current_location + direction
            if (self.visited_locations == new_location).all(1).any() or self.data_padded[tuple(new_location)] == 9:
                continue
            self.visited_locations = np.append(self.visited_locations, [new_location], 0)
            self.take_steps(new_location)

    def second_answer(self) -> int:
        return 786780


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
