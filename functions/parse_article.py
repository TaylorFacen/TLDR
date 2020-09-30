from bs4 import BeautifulSoup
from readability import Document
import requests

def parse_article(url):
    """ Fetches the main article text from a given url """
    # Fetch the contents of the url
    response = requests.get(url)

    # Get the main article section from the page
    doc = Document(response.text)
    article_html = doc.summary()

    # Remove the html tags
    article_text = BeautifulSoup(article_html, "lxml").get_text()

    return article_text