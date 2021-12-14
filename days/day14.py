import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
import re
from collections import Counter
import sys

class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(14)
        debug = False
        self.template = str(dataloader.load_data(data_type='str', debug=debug, max_rows=1))
        self.pair_insertions = dataloader.load_data(data_type='str', debug=debug, delimiter=" -> ", skip_header=2)
        self.pair_map = dict(self.pair_insertions)
        self.pair_map_insert = dict()
        for pair, ins in self.pair_insertions:
            self.pair_map_insert[pair] = pair[0] + ins + pair[1]
        self.pattern = re.compile("|".join(self.pair_map_insert.keys()))

    def first_solution(self) -> int:
        template = self.template
        for i in range(10):
            template = self.insert_pairs(template)
        counter = Counter(template)
        ordered = counter.most_common()
        return ordered[0][1] - ordered[-1][1]

    def insert_pairs(self, template) -> str:
        new_string = ""
        for i in range(len(template) - 1):
            new_string += self.pair_map_insert[template[i:i+2]][0:2]
        return new_string + template[-1]

    def first_answer(self) -> int:
        return 4244

    def second_solution(self) -> int:
        # create initial count of pairs in the template
        pair_map_count = dict.fromkeys(self.pair_map.keys(), 0)
        for i in range(len(self.template) - 1):
            pair_map_count[self.template[i:i+2]] += 1

        for i in range(40):
            pair_map_count_old = pair_map_count.copy()
            for key, value in pair_map_count_old.items():
                if value != 0:
                    new_key1 = self.pair_map_insert[key][0:2]
                    new_key2 = self.pair_map_insert[key][1:3]

                    # add the found keys to the dictionary count
                    pair_map_count[new_key1] += value
                    pair_map_count[new_key2] += value

                    # also subtract
                    pair_map_count[key] -= value

        element_count = Counter()
        for key, value in pair_map_count.items():
            element_count[key[0]] += value
            # element_count[key[1]] -= value
        element_count[self.template[-1]] += 1
        ordered = element_count.most_common()
        return ordered[0][1] - ordered[-1][1]




    def second_answer(self) -> int:
        return 4807056953866


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
