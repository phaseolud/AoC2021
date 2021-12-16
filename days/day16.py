import operator

import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(16)
        self.debug = False
        self.data = (dataloader.load_data(debug=self.debug, data_type='str'))
        self.op = {
            0: np.sum,
            1: np.prod,
            2: np.amin,
            3: np.amax,
            5: lambda x: x[0] > x[1],
            6: lambda x: x[0] < x[1],
            7: lambda x: x[0] == x[1]
        }
        self.op_default = {
            0: 0,
            1: 1,
        }

    def first_solution(self) -> int:
        # make it iterable for debug, where we have several lines
        versions = ()
        data = self.data
        if not self.data.shape:
            data = [self.data]
        for row in data:
            bin_data = self.hex2binary(str(row))
            versions, lit_vals, length = self.process_package(bin_data)
            if self.debug:
                print(versions, sum(versions), lit_vals, length)
        return sum(versions)


    def first_answer(self) -> int:
        return 897

    def second_solution(self) -> int:
        lit_vals = ()
        data = self.data
        if not self.data.shape:
            data = [self.data]
        for row in data:
            bin_data = self.hex2binary(str(row))
            versions, lit_vals, length = self.process_package(bin_data)
            if self.debug:
                print(versions, sum(versions), lit_vals, length)
        return lit_vals[0]

    def second_answer(self) -> int:
        return 9485076995911

    @staticmethod
    def hex2binary(hex_num):
        n_bits = len(hex_num) * 4
        return bin(int(hex_num, 16))[2:].zfill(n_bits)

    def process_package(self, package: str) -> (tuple[int], tuple[int], int):
        versions = (int(package[:3], 2),)
        pid = int(package[3:6], 2)
        lit_vals = ()
        length = 0
        pre_length = 0
        if pid == 4:
            lit_val, length = self.calculate_literal_value(package)
            lit_vals += (lit_val,)
            return versions, lit_vals, length
        else:
            # operator packet
            length_type_id = int(package[6])
            if length_type_id == 0:
                pre_length = 22
                total_length_sub = int(package[7:22], 2)
                while length < total_length_sub:
                    subpackage = package[22 + length:]
                    versions_sub, lit_vals_sub, l = self.process_package(subpackage)
                    length += l
                    versions += versions_sub
                    lit_vals += lit_vals_sub

            elif length_type_id == 1:
                n_subpackets = int(package[7:18], 2)
                pre_length = 18
                for i in range(n_subpackets):
                    subpackage = package[18 + length:]
                    versions_sub, lit_vals_sub, l = self.process_package(subpackage)
                    versions += versions_sub
                    lit_vals += lit_vals_sub
                    length += l

            # check the length of lit_vals:
            if len(lit_vals) == 1 and pid in self.op_default.keys():
                lit_vals += (self.op_default[pid], )
            # add the operators
            agg = int(self.op[pid](lit_vals))
            return versions, (agg, ), length + pre_length

    @staticmethod
    def calculate_literal_value(package):
        next_group = 1
        ng = 0
        lit_val = ""
        while next_group:
            group = package[6 + ng * 5:11 + ng * 5]
            next_group = int(group[0])
            lit_val += group[1:]
            ng += 1
        package_length = 11 + (ng - 1) * 5
        return int(lit_val, 2), package_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
