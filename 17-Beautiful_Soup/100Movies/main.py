import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)

website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, 'html.parser')
# print(soup)

all_movies = soup.find_all(name='h3', class_='title')
# print(all_movies)

movies_titles = [movie.getText() for movie in all_movies]
movies = movies_titles[::-1]

with open('movies.text', mode='w', encoding='UTF-8') as file:
    for movie in movies:
        file.write(f'{movie}\n')
