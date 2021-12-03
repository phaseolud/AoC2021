from abc import ABC, abstractmethod


class SolutionTemplate(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def first_solution(self) -> int:
        pass

    @abstractmethod
    def first_answer(self) -> int:
        pass

    @abstractmethod
    def second_solution(self) -> int:
        pass

    @abstractmethod
    def second_answer(self) -> int:
        pass
