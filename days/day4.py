import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Day4DataLoader(DataLoader):
    def __init__(self):
        super(Day4DataLoader, self).__init__(day=4)

    def load_data(self, data_type='int', kwargs=None):
        with open(self.input_file, 'r') as f:
            draws = list(map(int, f.readline().split(",")))
        cards = np.genfromtxt(self.input_file, dtype='int', skip_header=2)
        cards = cards.reshape((-1, 5, 5))
        return draws, cards


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = Day4DataLoader()
        self.data = dataloader.load_data()

    def first_solution(self) -> int:
        (draws, cards) = self.data
        card_mask = np.zeros(cards.shape, dtype='int')
        winner = -1
        drawn_number = -1
        for drawn_number in draws:
            card_mask[cards == drawn_number] = 1
            (is_bingo, winner) = self.find_bingos(card_mask)
            if is_bingo:
                break
        return drawn_number * ((1 - card_mask[winner[0]]) * cards[winner[0]]).sum()

    @staticmethod
    def find_bingos(card_masks):
        is_bingo = 0
        winner = -1
        winning_cards_indices = np.argwhere(np.logical_or(card_masks.sum(axis=1) == 5, card_masks.sum(axis=2) == 5))
        if len(winning_cards_indices):
            is_bingo = True
            winner = winning_cards_indices[:, 0]
        return is_bingo, winner

    def first_answer(self) -> int:
        return 65325

    def second_solution(self) -> int:
        # there can be multiple bingos :(
        (draws, cards) = self.data
        card_mask = np.zeros(cards.shape, dtype='int')
        card_mask2 = np.copy(card_mask)
        winners = []
        for drawn_number in draws:
            card_mask[cards == drawn_number] = 1
            card_mask2[cards == drawn_number] = 1
            (is_bingo, winner) = self.find_bingos(card_mask)
            if is_bingo:
                winners.extend(winner)
                card_mask[winner] = 0
            if len(set(winners)) == cards.shape[0]:
                break
        ordered_winners_unique = list(dict.fromkeys(winners))
        return drawn_number * ((1 - card_mask2[ordered_winners_unique[-1]]) * cards[ordered_winners_unique[-1]]).sum()

    def second_answer(self) -> int:
        return 4624


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
