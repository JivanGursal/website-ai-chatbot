import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_website(start_url, max_pages=5):
    visited = set()
    text_data = []

    def crawl(url):
        if url in visited or len(visited) >= max_pages:
            return
        visited.add(url)

        try:
            res = requests.get(url, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")

            # Remove scripts & styles
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)
            text_data.append(text[:2000])  # limit per page

            # Crawl internal links
            for link in soup.find_all("a", href=True):
                next_url = urljoin(url, link["href"])
                if urlparse(next_url).netloc == urlparse(start_url).netloc:
                    crawl(next_url)

        except:
            pass

    crawl(start_url)
    return "\n".join(text_data)
