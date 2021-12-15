from queue import PriorityQueue

import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(15)
        self.data = dataloader.load_data(debug=False, data_type='int', delimiter=1)
        self.map = np.pad(self.data, ((1, 1), (1, 1)), 'constant', constant_values=0)
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def first_solution(self) -> int:
        start_node = [1, 1]
        end_node = [self.data.shape[0], self.data.shape[1]]
        came_from, cost_so_far = self.dijkstra(start_node, end_node)
        return cost_so_far[self.c2i(end_node)]

    def dijkstra(self, start_node, end_node):
        frontier = PriorityQueue()
        frontier.put((0, start_node))
        came_from = {self.c2i(start_node): None}
        cost_so_far = {self.c2i(start_node): 0}

        while not frontier.empty():
            current = frontier.get()[1]
            if current == end_node:
                break

            for n in self.neighbors(current):
                ni = self.c2i(n)
                new_cost = cost_so_far[self.c2i(current)] + self.map[tuple(n)]
                if ni not in cost_so_far or new_cost < cost_so_far[ni]:
                    cost_so_far[ni] = new_cost
                    priority = new_cost
                    frontier.put((priority, n))
                    came_from[ni] = current
        return came_from, cost_so_far

    def c2i(self, coordinate):
        height, width = self.map.shape
        return width * coordinate[0] + coordinate[1]

    def neighbors(self, current_node) -> list[list[int, int]]:
        neighbors = []
        for d in self.directions:
            new_coordinate = list(map(int.__add__, current_node, d))
            if self.map[tuple(new_coordinate)] != 0:
                neighbors.append(new_coordinate)
        return neighbors

    def first_answer(self) -> int:
        return 626

    def second_solution(self) -> int:
        height, width = self.data.shape
        new_data = np.zeros((height * 5, width * 5), dtype='int')
        for i in range(5):
            for j in range(5):
                new_data[i * height: (i + 1) * height, j * width: (j + 1) * width] = \
                    (self.data + i + j - 1) % 9 + 1
        self.map = np.pad(new_data, ((1, 1), (1, 1)), 'constant', constant_values=0)
        self.data = new_data

        start_node = [1, 1]
        end_node = [self.data.shape[0], self.data.shape[1]]
        came_from, cost_so_far = self.dijkstra(start_node, end_node)
        return cost_so_far[self.c2i(end_node)]

    def second_answer(self) -> int:
        return 2966


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
