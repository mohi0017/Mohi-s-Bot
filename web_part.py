import re
import requests
from bs4 import BeautifulSoup

def search_wikipedia(query):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srprop": "",
        "utf8": ""
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "query" in data and "search" in data["query"]:
            search_results = data["query"]["search"]
            if search_results:
                page_id = search_results[0]["pageid"]
                return get_wikipedia_page(page_id)
    return None

def get_wikipedia_page(page_id, num_sentences=3):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "format": "json",
        "pageid": page_id,
        "prop": "text",
        "section": 0, 
        "utf8": ""
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "parse" in data and "text" in data["parse"]:
            content_html = data["parse"]["text"]["*"]
            content_text = clean_html(content_html)
            shortened_text = shorten_text(content_text, num_sentences)
            return shortened_text
    return None

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for element in soup(["sup", "table", "style"]):
        element.decompose()
    text = soup.get_text(separator="\n")
    return text

def shorten_text(text, num_sentences):
    paragraphs = text.split("\n\n")
    if paragraphs:
        # Extract the text from the paragraphs
        text = " ".join([paragraph.strip() for paragraph in paragraphs])
        # Remove citations and references
        text = re.sub(r"\[\d+\]", "", text)
        # Extract the desired number of sentences
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
        shortened_text = ". ".join(sentences[:num_sentences])
        return shortened_text
    return None

def get_Query(query):
    try:
        result = search_wikipedia(query)
        if result:
            return result
    except:
        return None