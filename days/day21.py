from functools import cache

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(21)
        self.data_raw = dataloader.load_data(data_type='str')
        self.data = list(map(int, self.data_raw[:, 4]))
        self.die_state = 0

    def first_solution(self) -> int:
        player1, player2 = self.data
        die_rolls = 0
        playing = True
        score1 = score2 = 0
        while playing:
            player1, score1 = self.roll_die(player1, score1)
            die_rolls += 3
            if score1 >= 1000: break
            player2, score2 = self.roll_die(player2, score2)
            die_rolls += 3
            if score2 >= 1000: break
        losing_score = score1 if score1 < score2 else score2
        return losing_score * die_rolls

    def roll_die(self, player, score):
        die_values = []
        for i in range(3):
            self.die_state = (self.die_state) % 100 + 1
            die_values.append(self.die_state)
        player = (player + sum(die_values) - 1) % 10 + 1
        score += player
        return player, score

    def first_answer(self) -> int:
        return 897798

    def second_solution(self) -> int:
        return max(self.simulate_dirac_rolls(self.data[0], self.data[1], 0, 0, 1))

    def second_answer(self) -> int:
        pass

    @cache
    def simulate_dirac_rolls(self, player1, player2, score1, score2, turn):
        if score1 >= 21:
            return 1, 0
        if score2 >= 21:
            return 0, 1
        wins = (0, 0)
        if turn == 1:
            for die1 in range(1, 4):
                for die2 in range(1, 4):
                    for die3 in range(1, 4):
                        die_sum = die1 + die2 + die3
                        new_player1 = (player1 + die_sum - 1) % 10 + 1
                        new_score1 = score1 + new_player1
                        (win1, win2) = self.simulate_dirac_rolls(new_player1, player2, new_score1, score2, 2)
                        wins = (wins[0] + win1, wins[1] + win2)
        else:
            for die1 in range(1, 4):
                for die2 in range(1, 4):
                    for die3 in range(1, 4):
                        die_sum = die1 + die2 + die3
                        new_player2 = (player2 + die_sum - 1) % 10 + 1
                        new_score2 = score2 + new_player2
                        (win1, win2) = self.simulate_dirac_rolls(player1, new_player2, score1, new_score2, 1)
                        wins = (wins[0] + win1, wins[1] + win2)
        return wins


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
