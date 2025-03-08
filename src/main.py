import codecs
import requests
import re
from bs4 import BeautifulSoup
import lxml
import html5lib

"""
A tool that converts Aozora Bunko(青空文庫) html files into epub.
"""

if __name__ == "__main__":
    url = "https://www.aozora.gr.jp/cards/000148/files/752_14964.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content.decode("shift_jis"), "xml")
    print(soup.h4())
