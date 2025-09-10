from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup)

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)

# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get('href'))

heading = soup.find(name='h1')
# print(heading.getText())

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.get('class'))

company_url = soup.select_one(selector='p a')
# print(company_url)

class_is_heading = soup.find_all(class_='heading')
# print(class_is_heading)

h3_heading = soup.find_all('h3', class_='heading')
# print(h3_heading)

headings = soup.select('.heading')
print(headings)

name = soup.select_one('#name')
# print(name)
