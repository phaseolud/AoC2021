import math

import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(5)
        self.data = dataloader.load_data(data_type='str')
        self.pdata = self.process_data()
        self.xmax = np.max(self.pdata[:, [0, 2]]) + 1
        self.ymax = np.max(self.pdata[:, [1, 3]]) + 1

    def process_data(self):
        # return the data in the format (x1, y1), (x2, y2)
        x1y1 = np.array(list(map((lambda x: x.split(',')), self.data[:, 0]))).astype('int')
        x2y2 = np.array(list(map((lambda x: x.split(',')), self.data[:, 2]))).astype('int')
        return np.concatenate((x1y1, x2y2), axis=1)

    def first_solution(self) -> int:
        # check if we have horizontal/vertical lines
        vent_grid = np.zeros((self.xmax, self.ymax), dtype='int')
        vent_grid = self.fill_grid_with_straight_lines(vent_grid)
        return np.sum(vent_grid > 1)

    def fill_grid_with_straight_lines(self, vent_grid):
        for (x1, y1, x2, y2) in self.get_straight_lines():
            x1, x2 = (x1, x2 + 1) if x2 >= x1 else (x2, x1 + 1)
            y1, y2 = (y1, y2 + 1) if y2 >= y1 else (y2, y1 + 1)
            vent_grid[x1:x2, y1:y2] += 1
        return vent_grid

    def get_straight_lines(self):
        hor = self.pdata[self.pdata[:, 1] == self.pdata[:, 3]]
        vert = self.pdata[self.pdata[:, 0] == self.pdata[:, 2]]
        return np.concatenate((hor, vert), axis=0)

    def first_answer(self) -> int:
        return 7438

    def second_solution(self) -> int:
        vent_grid = np.zeros((self.xmax, self.ymax), dtype='int')
        vent_grid = self.fill_grid_with_straight_lines(vent_grid)
        # add diagonal lines
        vent_grid = self.add_diag_lines(vent_grid)
        return np.sum(vent_grid > 1)

    def add_diag_lines(self, vent_grid):
        for (x1, y1, x2, y2) in self.pdata:
            if not (x1 == x2 or y1 == y2):
                line_length_step = abs(x1 - x2)
                slope = int((y2 - y1)/(x2 - x1))
                start_point = (x1, y1) if x2 > x1 else (x2, y2)
                for t in range(line_length_step + 1):
                    vent_grid[start_point[0] + t, start_point[1] + t * slope] += 1
        return vent_grid

    def print_vent_grid(self, vent_grid):
        for line in vent_grid.transpose():
            print("".join(map(str, line)).replace("0", "."))

    def second_answer(self) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
