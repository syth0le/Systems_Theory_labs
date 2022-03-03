import dataclasses
from enum import Enum
from random import randint, shuffle
from typing import List


class NotGoatDoorException(BaseException):
    pass


@dataclasses.dataclass
class Statistics:
    wins: int
    loses: int
    overall: int
    win_ratio: float
    lose_ratio: float


class MontyHallChoices(Enum):
    GOAT_1 = 'GOAT 1'
    GOAT_2 = 'GOAT 2'
    AUTO = 'Audi RS6'

    @classmethod
    def choices(cls) -> List[str]:
        return list(i.value for i in cls)


class MontyHallSimulator:
    def __init__(self, iterations: int = 10000) -> None:
        self.choices = MontyHallChoices.choices()
        self.door_amount = 3
        self.counter = 0
        self.iterations = iterations
        self.is_turned = False

    def startup(self):
        for _ in range(self.iterations):
            random_index = randint(1, self.door_amount)
            choice = self.choices.pop(random_index-1)

            random_index_between_two = randint(1, len(self.choices))
            if self.choices[random_index_between_two-1] == MontyHallChoices.AUTO.value:
                stayed = self.choices.pop(random_index_between_two - 1)
                door_with_goat = self.choices[0]
            else:
                door_with_goat = self.choices.pop(random_index_between_two - 1)
                stayed = self.choices[0]

            if door_with_goat not in [MontyHallChoices.GOAT_1.value, MontyHallChoices.GOAT_2.value]:
                raise NotGoatDoorException

            if self.is_turned:
                choice = stayed

            if choice == MontyHallChoices.AUTO.value:
                self.counter += 1

            self.__reset()

    def get_statistics(self) -> Statistics:
        loses = self.iterations - self.counter
        win_ratio = self.counter / self.iterations
        lose_ratio = loses / self.iterations
        return Statistics(
            overall=self.iterations,
            wins=self.counter,
            loses=loses,
            win_ratio=win_ratio,
            lose_ratio=lose_ratio,
        )

    def __reset(self) -> None:
        self.choices = MontyHallChoices.choices()
        shuffle(self.choices)

    def reset_attributes(self) -> None:
        self.counter = 0
        self.__reset()

    def switch_mode(self) -> None:
        self.is_turned = not self.is_turned

