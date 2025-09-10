from bs4 import BeautifulSoup
import requests


URL = 'https://news.ycombinator.com/'
response = requests.get(url=URL).text
# print(response)

soup = BeautifulSoup(response, 'html.parser')
# print(soup)

articles = soup.find_all(name='span', class_='titleline')
# print(article_tag)

articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)

    links = article_tag.find(name='a').get('href')
    articles_links.append(links)


article_upvote = [score.getText().split()[0] for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvote)
# print(largest_number)

largest_index = article_upvote.index(largest_number)
# print(largest_index)

print(articles_texts[largest_index])
print(articles_links[largest_index])

# print(articles_links)
# print(articles_texts)
# print(article_upvote)



