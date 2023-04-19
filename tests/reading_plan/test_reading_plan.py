from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock

mock = [
    {
        "url": "https://blog.betrybe.com/tecnologia/5-motivos-para-não",
        "title": "5 motivos para não estudar na Trybe",
        "timestamp": "01-07-2021",
        "reading_time": 5,
        "writer": "Tryber",
        "summary": "A Trybe é uma escola de desenvolvimento",
        "category": "Estudo",
    },
    {
        "url": "https://blog.betrybe.com/tecnologia/noticia-muito-longa/",
        "title": "Notícia muito longa",
        "timestamp": "01-07-2021",
        "reading_time": 70,
        "writer": "Tryber",
        "summary": "A Trybe é uma escola de desenvolvimento de software que",
        "category": "Estudo",
    },
]

response_mock = {
    "readable": [
        {
            "unfilled_time": 1,
            "chosen_news": [("5 motivos para não estudar na Trybe", 4)],
        }
    ],
    "unreadable": [("Notícia longa", 100)],
}


def test_reading_plan_group_news():

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock)

    grouped = ReadingPlanService.group_news_for_available_time(30)
    print(grouped)

    assert len(grouped["readable"]) == 1
    assert grouped["readable"][0]["unfilled_time"] == 25
    assert len(grouped["unreadable"]) == 1
