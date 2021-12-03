from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
import numpy as np


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(1)
        self.data = dataloader.load_data()

    def first_solution(self) -> int:
        data_shifted = np.roll(self.data, 1)
        difference = self.data - data_shifted
        return (difference[1:] > 0).sum()

    def first_answer(self) -> int:
        return 1681

    def second_solution(self) -> int:
        windowed_sum = np.convolve(np.ones(3, dtype='int'), self.data, mode='valid')
        windowed_sum_shifted = np.roll(windowed_sum, 1)
        difference = windowed_sum - windowed_sum_shifted
        return (difference[1:] > 0).sum(0)

    def second_answer(self) -> int:
        return 1704


if __name__ == "__main__":
    day = Solution()
    print(day.first_solution())
    print(day.second_solution())
