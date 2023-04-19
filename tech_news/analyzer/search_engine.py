from tech_news.database import search_news
from datetime import datetime

MONTHS = {
    "01": "janeiro",
    "02": "fevereiro",
    "03": "março",
    "04": "abril",
    "05": "maio",
    "06": "junho",
    "07": "julho",
    "08": "agosto",
    "09": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro",
}


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({"title": {"$regex": title, "$options": "-i"}})
    title_results = []
    for news in news_list:
        title_results.append((news["title"], news["url"]))
    print(news_list)
    return title_results


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    date_form = datetime.strptime(
        date, '%Y-%m-%d').strftime('%d/%m/%Y')
    news = search_news({'timestamp': {'$eq': date_form}})
    return [(new['title'], new['url']) for new in news]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
