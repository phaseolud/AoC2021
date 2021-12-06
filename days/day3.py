import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(3)
        self.data = dataloader.load_data(data_type='int', kwargs={'delimiter': 1})

    def first_solution(self) -> int:
        n_numbers = len(self.data)
        bit_count = self.data.sum(axis=0)
        gamma = list(map(int, bit_count > n_numbers / 2))
        epsilon = [1 - x for x in gamma];
        gamma_dec = int(''.join(list(map(str, gamma))), 2)
        epsilon_dec = int(''.join(list(map(str, epsilon))), 2)
        return gamma_dec * epsilon_dec

    def first_answer(self) -> int:
        return 1131506

    def second_solution(self) -> int:
        bitlist_ox = np.copy(self.data)
        bitlist_co2 = np.copy(self.data)
        n_bits = len(self.data[0])
        for bit in range(n_bits):
            if len(bitlist_ox) > 1:
                n_numbers_ox = len(bitlist_ox)
                most_common_ox = int(bitlist_ox[:, bit].sum(axis=0) >= n_numbers_ox / 2)
                bitlist_ox = bitlist_ox[bitlist_ox[:, bit] == most_common_ox]
            if len(bitlist_co2) > 1:
                n_numbers_co2 = len(bitlist_co2)
                least_common_co2 = 1 - int(bitlist_co2[:, bit].sum(axis=0) >= n_numbers_co2 / 2)
                bitlist_co2 = bitlist_co2[bitlist_co2[:, bit] == least_common_co2]

        ox_dec = int("".join(map(str, bitlist_ox[0])), 2)
        co2_dec = int("".join(map(str, bitlist_co2[0])), 2)
        return ox_dec * co2_dec

    def second_answer(self) -> int:
        return 7863147


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
