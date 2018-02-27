import re

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/home/home/environments/pipl_test/samples/linkedin/1003_172bc83cb13a5022.html"), "html.parser")
# soup = BeautifulSoup(open("/home/home/environments/pipl_test/samples/linkedin/1003_75579261d7f86c3f.html"), "html.parser")

name = soup.find('span', {'class': 'full-name'}).text
print(name)

education = soup.find_all('div', {'class': "editable-item section-item", 'id': re.compile('education.*')})
for item in education:
    print("Education Item:", item)

skills = soup.find_all('span', {'class': "endorse-item-name-text"})
for item in skills:
    print("Skills Item:", item)
