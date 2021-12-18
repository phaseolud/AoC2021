from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate
import ast


class SnailFishNumber:

    def __init__(self, nums=None, depths=None, groups=None):
        if nums is None:
            nums = []
        if depths is None:
            depths = []
        if groups is None:
            groups = []
        self.nums: list[int] = nums
        self.depths: list[int] = depths
        self.groups: list[tuple] = groups

    def process_list(self, data, depth=0, group=(), group_c=0):
        depth += 1
        for d in data:
            group_c += 1
            if isinstance(d, list):
                for sub_d in self.process_list(d, depth, group + (group_c,)):
                    yield sub_d
            else:
                yield d, depth, group + (group_c,)

    def parse_from_list(self, snailfish_list):
        self.processed = list(self.process_list(snailfish_list))
        self.nums = []
        self.depths = []
        self.groups = []
        for e in self.processed:
            self.nums.append(e[0])
            self.depths.append(e[1])
            self.groups.append(e[2])

    def parse_from_str(self, snailfish_str):
        self.vec = ast.literal_eval(snailfish_str)
        self.parse_from_list(self.vec)

    def __add__(self, other):
        numbers = self.nums + other.nums
        depth = list(map(lambda x: x + 1, self.depths + other.depths))
        groups = list(map(lambda x: (1,) + x, self.groups)) + list(map(lambda x: (2,) + x, other.groups))
        return SnailFishNumber(numbers, depth, groups)

    def __str__(self):
        return f"numbers: {self.nums}, depths: {self.depths}, groups: {self.groups}"

    def __repr__(self):
        return repr(f"SFN({len(self.nums)})")

    def reduce(self):
        can_reduce = True
        while can_reduce:
            can_explode = True
            while can_explode:
                for i in range(len(self.depths) - 1):
                    if self.depths[i] == self.depths[i + 1] and \
                            self.groups[i][:-1] == self.groups[i + 1][:-1] and self.depths[i] > 4:
                        self.explode([i, i + 1])
                        break
                else:
                    can_explode = False

            # split
            for i in range(len(self.nums)):
                if self.nums[i] >= 10:
                    self.split(i)
                    break
            else:
                can_reduce = False
        return self

    def split(self, split_index):
        num = self.nums[split_index]
        group = self.groups[split_index]
        depth = self.depths[split_index]

        snum0 = num // 2
        snum1 = num - snum0

        self.nums.pop(split_index)
        self.nums.insert(split_index, snum0)
        self.nums.insert(split_index + 1, snum1)

        self.groups.pop(split_index)
        self.groups.insert(split_index, group + (1,))
        self.groups.insert(split_index + 1, group + (2,))

        self.depths.pop(split_index)
        self.depths.insert(split_index, depth + 1)
        self.depths.insert(split_index + 1, depth + 1)

    def magnitude(self):
        can_reduce = True
        nums = self.nums.copy()
        groups = self.groups.copy()
        depths = self.depths.copy()
        while can_reduce:
            current_depth = max(depths)
            for i in range(len(depths) - 1):
                if depths[i] == current_depth and depths[i] == depths[i+1] \
                    and groups[i][:-1] == groups[i + 1][:-1]:
                    new_num = 3*nums[i] + 2 * nums[i+1]
                    nums[i] = new_num
                    depths[i] -= 1
                    groups[i] = groups[i][:-1]
                    nums.pop(i + 1)
                    depths.pop(i + 1)
                    groups.pop(i + 1)
                    break
            can_reduce = len(nums) > 1
        return nums

    def explode(self, pair_indices):
        # explode
        if pair_indices[0] != 0:
            self.nums[pair_indices[0] - 1] += self.nums[pair_indices[0]]
        if pair_indices[1] != len(self.nums) - 1:
            self.nums[pair_indices[1] + 1] += self.nums[pair_indices[1]]

        # remove pair_indices[1], and make indices[0] 1 higher
        self.nums.pop(pair_indices[1])
        self.groups.pop(pair_indices[1])
        self.depths.pop(pair_indices[1])

        self.depths[pair_indices[0]] -= 1
        self.nums[pair_indices[0]] = 0
        self.groups[pair_indices[0]] = self.groups[pair_indices[0]][:-1]



class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(18)
        self.data_raw = dataloader.load_data(data_type='str', debug=False)

        # convert the lists to two lists: numbers, depth
        self.data = []
        for row in self.data_raw:
            # loop over every list element/character and check if isint or not
            s = SnailFishNumber()
            s.parse_from_str(row)
            self.data.append(s)

    def first_solution(self) -> int:
        current_s = self.data[0]
        for s in self.data[1:]:
            current_s = current_s + s
            current_s.reduce()
        return current_s.magnitude()[0]

    def first_answer(self) -> int:
        return 3981

    def second_solution(self) -> int:
        magnitudes: list[int] = []
        for s0 in self.data:
            for s1 in self.data:
                if s0 != s1:
                    magnitudes.append((s0 + s1).reduce().magnitude()[0])
        return max(magnitudes)

    def second_answer(self) -> int:
        return 4687


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
