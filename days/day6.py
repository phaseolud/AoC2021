import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(6)
        self.data = dataloader.load_data(data_type='int', kwargs={'delimiter': ','})

    def first_solution(self) -> int:
        fish_list = np.copy(self.data)
        for day in range(18):
            fish_list -= 1
            n_new_fish = (fish_list == -1).sum()
            fish_list[fish_list == -1] = 6
            fish_list = np.append(fish_list, 8 * np.ones(n_new_fish, dtype='int'))
        return len(fish_list)

    def first_answer(self) -> int:
        return 391888

    def second_solution(self) -> int:
        # we count the number of fish that have n days to reproduce
        fish_day_to_repr = np.zeros(9, dtype='int64')
        for day in self.data:
            fish_day_to_repr[day] += 1
        for day in range(256):
            fish_day_to_repr = np.roll(fish_day_to_repr, -1)
            # the fish at day[end] (/8) are the number of fish that have new offspring -> keep on 8
            # should also add to day 6 all the fish
            fish_day_to_repr[6] += fish_day_to_repr[-1]
        return fish_day_to_repr.sum()

    def second_answer(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
