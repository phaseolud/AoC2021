from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(1)
        self.data = dataloader.load_data()

    def first_solution(self) -> int:
        pass

    def first_answer(self) -> int:
        pass

    def second_solution(self) -> int:
        pass

    def second_answer(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
