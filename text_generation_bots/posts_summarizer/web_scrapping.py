import requests
from bs4 import BeautifulSoup

def extract_article_text(url: str) -> str:
    # Fetch page
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # Remove scripts and styles
    for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
        tag.decompose()

    # Try to detect article container
    article = (
        soup.find("article") or 
        soup.find("div", class_="article") or
        soup.find("div", class_="content") or
        soup.find("main") or
        soup
    )

    # Extract text
    text = article.get_text(separator="\n")

    # Clean whitespace
    clean_text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])

    return clean_text
