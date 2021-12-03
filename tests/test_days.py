import importlib
from pathlib import Path

import pytest
from parametrized import parametrized
from definitions import DAY_DIR


def load_all_days():
    day_files = Path(DAY_DIR).glob("day*.py")
    days = [day.stem for day in day_files]
    return days


@pytest.mark.parametrize("day", load_all_days())
def test_single_day(day):
    day_module = importlib.import_module(f"days.{day}")
    solution = day_module.Solution()
    assert (solution.first_solution() == solution.first_answer())
    assert (solution.second_solution() == solution.second_answer())
    # also check that we don't return None for both
    assert (solution.first_answer() is not None)
    assert (solution.second_answer() is not None)
# create class
# tests first and second solution
