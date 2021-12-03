from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
import numpy as np


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(2)
        self.data = dataloader.load_data(None)

    def first_solution(self) -> int:
        step_count = {'forward': 0, 'down': 0, 'up': 0}
        for instruction, step in self.data:
            step_count[instruction] += step
        return step_count['forward'] * \
               (step_count['down'] - step_count['up'])

    def first_answer(self) -> int:
        return 1728414

    def second_solution(self) -> int:
        orientation = {'horizontal': 0, 'depth': 0, 'aim': 0}
        ud_map = {'up': -1, 'down': 1}
        for instruction, step in self.data:
            if instruction == 'forward':
                orientation['horizontal'] += step
                orientation['depth'] += step * orientation['aim']
            elif instruction in (ud_map.keys()):
                orientation['aim'] += step * ud_map[instruction]
        return orientation['horizontal'] * orientation['depth']

    def second_answer(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
