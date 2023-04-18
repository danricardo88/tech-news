import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    select = Selector(text=html_content)
    lks = select.css(".cs-overlay-link::attr(href)").getall()
    return lks


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    select = Selector(text=html_content)
    lnk = select.css(".next.page-numbers::attr(href)").get()
    return lnk


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    select = Selector(text=html_content)
    url = select.css("link[rel='canonical']::attr(href)").get()
    title = select.css("h1.entry-title::text").get().strip()
    timestamp = select.css("li.meta-date::text").get()
    writer = select.css("span.author a::text").get()
    reading_time = select.css("li.meta-reading-time::text").get().split()[0]
    category = select.css("div.meta-category span.label::text").get()
    summary = select.css(".entry-content p").xpath("string()").get().strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
