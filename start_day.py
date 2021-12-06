import datetime

from definitions import DAY_DIR, HELPER_DIR
from pathlib import Path
import shutil
import sys

from helpers.data import DataLoader


def copy_template_to_day(day) -> None:
    day_file = DAY_DIR / f"day{day}.py"
    template_file = HELPER_DIR / "day_template.py.template"
    with open(template_file, 'r') as f:
        file_content = f.read()
    file_content_day = file_content.replace("<<DAY>>", str(day))
    with open(day_file, 'w') as f:
        f.write(file_content_day)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        day = sys.argv[1]
    else:
        day = int(datetime.datetime.today().strftime("%d"))
    copy_template_to_day(day)
    dataloader = DataLoader(day)
    dataloader.download_data()

