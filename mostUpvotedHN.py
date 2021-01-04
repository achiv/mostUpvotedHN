from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name = "a", class_ = "storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# article_upvotes = [score.getText() for score in soup.find_all(name = "span", class_ = "score").getText()]

article_upvotes = []

for score in soup.find_all(name = "span", class_ = "score"):
    article_upvotes.append(int(score.getText().split()[0]))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index+1])
print(article_links[largest_index+1])

# print(article_upvotes)
# print(largest_number)
# print(largest_index)
# print(article_texts)
