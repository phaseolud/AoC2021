from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(8)
        self.data = dataloader.load_data(data_type='str')

    def first_solution(self) -> int:
        # the pipe is always at the tenth location:
        number_segments = {1: 2, 4: 4, 7: 3, 8: 7}
        signal_patterns = self.data[:, :10]
        output_values = self.data[:, 11:]
        return sum([1 for output_value in output_values.flatten() if len(output_value) in number_segments.values()])

    def first_answer(self) -> int:
        return 274

    def second_solution(self) -> int:
        number_segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
        sum_out = 0
        for row in self.data:
            row_signal = row[:10]
            output = row[11:]

            # first find the possible values of 1
            one = next(filter(lambda x: len(x) == 2, row_signal))
            four = next(filter(lambda x: len(x) == 4, row_signal))
            eight = next(filter(lambda x: len(x) == 7, row_signal))
            seven = next(filter(lambda x: len(x) == 3, row_signal))

            letter_a = self.str_diff(one, seven)

            zero_nine_six = list(filter(lambda x: len(x) == 6, row_signal))
            # filter six out by checking if both of 1 are in there
            zero_nine = list(filter(lambda x: set(one).issubset(x), zero_nine_six))
            six = next(filter(lambda x: not set(one).issubset(x), zero_nine_six))
            five = next(filter(lambda x: set(x).issubset(six) and x != six, row_signal))

            letters_de = self.str_diff(*zero_nine)
            letter_e = next(filter(lambda x: x not in four, letters_de))
            letter_d = next(filter(lambda x: x in four, letters_de))
            zero = next(filter(lambda x: letter_e in x, zero_nine))
            nine = next(filter(lambda x: letter_d in x, zero_nine))

            two_three = list(filter(lambda x: len(x) == 5 and x != five, row_signal))
            two = next(filter(lambda x: letter_e in x, two_three))
            three = next(filter(lambda x: letter_e not in x, two_three))

            numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
            numbers = list(map(lambda x: "".join(sorted(x)), numbers))
            number_to_int = dict(zip(numbers, map(str, range(10))))
            output_num = int("".join(number_to_int["".join(sorted(number))] for number in output))
            sum_out += output_num
        return sum_out

    @staticmethod
    def str_diff(str1, str2) -> str:
        return "".join(set.symmetric_difference(set(str1), set(str2)))

    def second_answer(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
