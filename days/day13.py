import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(13)
        self.coordinates = dataloader.load_data('int', delimiter=",", skip_footer=12)
        self.fold_instructions = dataloader.load_data('str', skip_header=795, usecols=2)

        ymax = np.max(self.coordinates[:, 1]) + 1
        xmax = np.max(self.coordinates[:, 0]) + 1
        self.paper = np.zeros((ymax, xmax), dtype='int')
        for c in self.coordinates:
            self.paper[c[1], c[0]] = 1

    def first_solution(self) -> int:
        paper = self.paper
        axis, line = self.fold_instructions[0].split("=")
        line = int(line)
        paper = self.fold(paper, line, axis)

        return np.count_nonzero(paper)


    def fold(self, paper, line: int, axis: str):
        if axis == 'x':
            right = paper[:, line + 1:]
            left = paper[:, :line]
            if np.shape(right)[1] <= line:
                right = np.pad(right, ((0, 0), (0, line - right.shape[1])))
            else:
                left = np.pad(left, ((0, 0), (line - right.shape[1], 0)))
            return left + np.fliplr(right)
        elif axis == 'y':
            lower = paper[line + 1:, :]
            upper = paper[:line]
            if np.shape(lower)[0] <= line:
                lower = np.pad(lower, ((0, line - lower.shape[0]), (0, 0)))
            else:
                upper = np.pad(upper, ((lower.shape[0] - line, 0), (0, 0)))
            return upper + np.flipud(lower)

    def first_answer(self) -> int:
        return 655

    def second_solution(self) -> int:
        paper = self.paper
        for instruction in self.fold_instructions:
            axis, line = instruction.split("=")
            line = int(line)
            paper = self.fold(paper, line, axis)
        for row in paper:
            for cell in row:
                print("#" if cell else ".", sep='', end="")
            print("")
        return 1

    def second_answer(self) -> int:
        return 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
