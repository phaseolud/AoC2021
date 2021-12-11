from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(10)
        self.data = dataloader.load_data(debug=False, data_type='str')
        self.bracket_pairs = {"{}": "", "[]": "", "()": "", "<>": ""}
        self.bracket_point_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self.bracket_point_dict_autocomplete = {'(': 1, "[": 2, "{": 3, "<": 4}
        self.illegal_pairs = []
        for b_pair in self.bracket_pairs.keys():
            new_pairs = ["".join([b_pair[0], b[1]]) for b in self.bracket_pairs.keys() if b != b_pair]
            self.illegal_pairs.extend(new_pairs)

    def first_solution(self) -> int:
        unvalid_brackets = []
        for bracket_line in self.data:
            bracket_line = self.reduce_bracket_line(bracket_line)
            if corrupted_bracket := self.check_corrupted(brackets=bracket_line):
                unvalid_brackets.append(corrupted_bracket)
        point_list = [self.bracket_point_dict[b] for b in unvalid_brackets]
        print(point_list)
        return sum(point_list)

    def reduce_bracket_line(self, bracket_line):
        is_same_size = False
        while not is_same_size:
            line_size = len(bracket_line)
            bracket_line = self.reduce_brackets(brackets=bracket_line)
            is_same_size = line_size == len(bracket_line)
        return bracket_line

    def reduce_brackets(self, brackets):
        for key, value in self.bracket_pairs.items():
            brackets = brackets.replace(key, value)
        return brackets

    def check_corrupted(self, brackets):
        for i in range(len(brackets) - 1):
            if brackets[i:i + 2] in self.illegal_pairs:
                return brackets[i + 1]

    def first_answer(self) -> int:
        return 315693

    def second_solution(self) -> int:
        additional_bracket_points_list = []
        for bracket_line in self.data:
            bracket_line = self.reduce_bracket_line(bracket_line)
            if not self.check_corrupted(brackets=bracket_line):
                additional_bracket_points = 0
                for bracket in bracket_line[::-1]:
                    additional_bracket_points *= 5
                    additional_bracket_points += self.bracket_point_dict_autocomplete[bracket]
                additional_bracket_points_list.append(additional_bracket_points)
        return sorted(additional_bracket_points_list)[len(additional_bracket_points_list) // 2]

    def second_answer(self) -> int:
        return 1870887234


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
