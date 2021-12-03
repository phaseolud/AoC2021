from datetime import datetime
import requests
from definitions import ROOT_DIR, SESSION
import numpy as np

class DataLoader:
    """
    Loads the data from the AoC website into the input_data folder
    """

    def __init__(self, day=None):
        self.input_data_folder = ROOT_DIR / "input_data"

        if day is None:
            day = int(datetime.today().strftime("%d"))
        self.day = day

        self.input_file = self.input_data_folder / f"input_{self.day}.txt"
        self.url = f"https://adventofcode.com/2021/day/{day}/input"

    def download_data(self) -> None:
        if not self.input_file.is_file():
            cookies = {"session": SESSION}
            r = requests.get(self.url, cookies=cookies)

            with open(self.input_file, "w") as f:
                f.write(r.text)

            print(f"Data successfully downloaded for day {self.day}")
        else:
            print(f"Data for day {self.day} is already downloaded")

    def load_data(self, data_type='int'):
        return np.loadtxt(self.input_file, dtype=data_type)

if __name__ == "__main__":
    dataloader = DataLoader()
    dataloader.download_data()
