import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(7)
        self.data = dataloader.load_data(data_type='int', kwargs={"delimiter": ','})

    def first_solution(self) -> int:
        max_pos = np.max(self.data)
        cost = np.zeros(max_pos, dtype='int')
        for pos in range(max_pos):
            cost[pos] = np.linalg.norm(self.data - pos, 1)
        return np.min(cost)

    def first_answer(self) -> int:
        return 352707

    def second_solution(self) -> int:
        max_pos = np.max(self.data)
        cost = np.zeros(max_pos, dtype='int')
        for pos in range(max_pos):
            abs_distance = np.abs(self.data - pos)
            cost[pos] = ((abs_distance * (abs_distance + 1)) / 2).sum()
        return np.min(cost)

    def second_answer(self) -> int:
        return 95519693


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
