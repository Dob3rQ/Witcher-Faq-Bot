import requests

WIKI_API_URL = "https://ru.wikipedia.org/w/api.php"

def search_wikipedia(query):
    """Ищет статью в Википедии по запросу."""
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
    }

    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    if "query" in data and "search" in data["query"]:
        search_results = data["query"]["search"]
        if search_results:
            title = search_results[0]["title"]  # Берем первую найденную статью
            return title
    return None

def get_wikipedia_summary(title):
    """Получает краткое описание статьи по её названию."""
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,  # Только вводная часть
        "explaintext": True,  # Без HTML
        "titles": title,
    }

    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    pages = data.get("query", {}).get("pages", {})
    for page_id, page_data in pages.items():
        if "extract" in page_data:
            return page_data["extract"], f"https://ru.wikipedia.org/wiki/{title.replace(' ', '_')}"

    return None, None

def find_best_wikipedia_article(user_question):
    """Ищет лучшую статью и возвращает краткое описание + ссылку."""
    title = search_wikipedia(user_question)
    if not title:
        return None, None

    summary, url = get_wikipedia_summary(title)
    return summary, url
