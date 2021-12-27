import numpy as np

from helpers.data import DataLoader
from helpers.day_solution_class import SolutionTemplate


class Solution(SolutionTemplate):

    def __init__(self):
        dataloader = DataLoader(20)
        debug = False
        self.alg_map = str(dataloader.load_data(data_type='str', debug=debug, max_rows=1, comments='%', deletechars='', delimiter=' '))
        self.image = dataloader.load_data(data_type='str', debug=debug, skip_header=2, comments='%', deletechars='', delimiter=1)

        n_pad = 100
        # pad the image, to account for the infinite image
        self.image = np.pad(self.image, pad_width=n_pad, constant_values='.')

    def first_solution(self) -> int:
        image = self.image.copy()
        for i in range(2):
            image = self.apply_image_algorithm(image)
            image = image[1:-1, 1:-1]
        return (image == '#').sum()

    def apply_image_algorithm(self, image):
        n, m = image.shape
        new_image = image.copy()
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                new_image[i, j] = self.apply_alg_map(image, i, j)
        return new_image

    def first_answer(self) -> int:
        return 5583

    def second_solution(self) -> int:
        image = self.image.copy()
        for i in range(50):
            image = self.apply_image_algorithm(image)
            image = image[1:-1, 1:-1]
        return (image == '#').sum()

    def second_answer(self) -> int:
        return 19592

    def apply_alg_map(self, image, i, j):
        new_str = ""
        sub = image[(i - 1): (i + 2), (j - 1): (j + 2)]
        new_str = "".join(sub.flatten()).replace(".", '0').replace('#', '1')
        return self.alg_map[int(new_str, 2)]

if __name__ == "__main__":
    solution = Solution()
    print(solution.first_solution())
    print(solution.second_solution())
