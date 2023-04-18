# from tech_news.analyzer.reading_plan import (
#     ReadingPlanService,
# )  # noqa: F401, E261, E501
# import pytest
# from unittest.mock import MagicMock


# posts = [
#     {
#         "url": "https://blog.betrybe.com/tecnologia/5-motivos-para-estudar",
#         "title": "5 motivos para estudar na Trybe",
#         "timestamp": "01-07-2021",
#         "writer": "Tryber",
#         "reading_time": 5,
#         "summary": "A Trybe é uma escola de desenvolvimento",
#         "category": "Estudo",
#     },
#     {
#         "url": "https://blog.betrybe.com/tecnologia/noticia-muito-longa/",
#         "title": "Notícia muito longa",
#         "timestamp": "01-07-2021",
#         "writer": "Tryber",
#         "reading_time": 70,
#         "summary": "A Trybe é uma escola de desenvolvimento de software que",
#         "category": "Estudo",
#     },
#     {
#         "url": "https://blog.betrybe.com/tecnologia/uma-noticia-rapida",
#         "title": "Uma notícia rápida",
#         "timestamp": "01-07-2021",
#         "writer": "Tryber",
#         "reading_time": 10,
#         "summary": "Uma notícia rápida que pode ser lida em 10 minutos",
#         "category": "Estudo",
#     },
# ]


# def test_reading_plan_group_news():

#     with pytest.raises(ValueError):
#         ReadingPlanService.group_news_for_available_time(-1)

#     # Mockando a função find_news
#     ReadingPlanService.find_news = MagicMock(return_value=posts)

#     # Executando a função group_news_for_available_time
#     grouped = ReadingPlanService.group_news_for_available_time(30)

#     # Validando os resultados
#     assert len(grouped["readable"]) == 1
#     assert grouped["readable"][0]["unfilled_time"] == 25
#     assert len(grouped["unreadable"]) == 1
#     assert grouped["unreadable"][0][0] == "Notícia muito longa"
#     assert grouped["unreadable"][0][1] == 70
