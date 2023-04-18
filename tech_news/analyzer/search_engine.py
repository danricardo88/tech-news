from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    new_list = search_news({"title": {"$regex": title, "$options": "-i"}})
    tilte_results = []
    for news in new_list:
        tilte_results.append((news["title"], news["url"]))
    return tilte_results


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
