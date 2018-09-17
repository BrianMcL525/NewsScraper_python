"""
program: news_scraper.py
Author: Brian McLaughlin

Uses the Beautiful Soup web scraper to pull rss data from a news feed url.
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "http://www.espn.com/espn/rss/nfl/news"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("-"* 60)