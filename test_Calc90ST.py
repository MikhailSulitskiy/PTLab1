from typing import Dict, Tuple
#from src.Types import DataType
from Types import DataType
#from src.Calc90ST import Calc90ST
from Calc90ST import Calc90ST
import pytest

RatingsType = Dict[str, float]


class Calc90ST():

    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 90),
                    ("русский язык", 90),
                    ("программирование", 90)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],
            "Семенов Семен Семенович":
                [
                    ("математика", 90),
                    ("русский язык", 90),
                    ("литература", 90)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 90,
            "Семенов Семен Семенович": 90
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data:
    Tuple[DataType,
          RatingsType]) -> None:
        calc_rating = Calc90ST(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data:
    Tuple[DataType, RatingsType]) -> None:
        rating = Calc90ST(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]

        for student in input_data[1]:
            rating_score = input_data[1][student]

            assert pytest.approx(rating_score,
                                 abs=0.001) == rating[student]