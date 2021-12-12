import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
from collections import Counter

class Solution(SolutionTemplate):

    def __init__(self):
        self.visited_paths = []
        dataloader = DataLoader(12)
        self.data = dataloader.load_data(debug=False, data_type='str', delimiter='-')
        self.data_graph = {}
        self.wbcount = 0
        for row in self.data:
            self.data_graph.setdefault(row[0], []).append(row[1])
            self.data_graph.setdefault(row[1], []).append(row[0])


    def first_solution(self) -> int:
        self.visited_paths = []
        current_node = 'start'
        self.walk_breath_first([current_node])
        return len(self.visited_paths)

    def walk_breath_first(self, current_path, small_cave_twice=False):
        self.wbcount += 1
        possible_paths = []
        for next_node in self.data_graph[current_path[-1]]:
            revisit_cave_condition = next_node not in current_path
            if small_cave_twice:
                counter = Counter(filter(str.islower, current_path + [next_node]))
                revisit_cave_condition = (sum(counter.values()) < len(counter) + 2 and next_node != 'start')
            if revisit_cave_condition or str.isupper(next_node):
                possible_path = current_path + [next_node]
                if possible_path[-1] == 'end':
                    self.visited_paths.append(possible_path)
                else:
                    possible_paths.append(possible_path)

        if not possible_paths: return

        for path in possible_paths:
            self.walk_breath_first(path, small_cave_twice=small_cave_twice)

    def first_answer(self) -> int:
        return 5076

    def second_solution(self) -> int:
        self.visited_paths = []
        current_node = 'start'
        self.walk_breath_first([current_node], small_cave_twice=True)
        return len(self.visited_paths)

    def second_answer(self) -> int:
        return 145643


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
