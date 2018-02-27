import re
from question_2.profile_extractor import ProfileExtractor


class ProfileExtractorLinkedIn(ProfileExtractor):
    def __init__(self, html_page):
        super().__init__(html_page)

    def validate_template(self):
        if self.html_page.find('span', {'class': 'full-name'}):
            self.is_valid = True

    def set_name(self):
        self.name = self.html_page.find('span', {'class': 'full-name'}).text

    def set_education(self):
        def find_institution(bs4_element):
            institution_element = bs4_element.find('h4', {'class': "summary fn org"})
            if institution_element:
                return institution_element.text
            else:
                return None

        def find_major(bs4_element):
            major_element = bs4_element.find('span', {'class': "major"})
            if major_element:
                return major_element.text
            else:
                return None

        def find_years(bs4_element):
            years_element = bs4_element.find('span', {'class': "education-date"})
            if years_element:
                return years_element.text
            else:
                return None

        for element in self.html_page.find_all('div', {'class': "editable-item section-item",
                                                       'id': re.compile('education.*')}):
            self.education.append({
                "institution_name": find_institution(element),
                "major": find_major(element),
                "years": find_years(element)
            })

    def set_skills(self):
        for element in self.html_page.find_all('span', {'class': "endorse-item-name-text"}):
            self.skills.append(element.text)


# html_page = '/home/home/environments/pipl_test/samples/linkedin/1003_172bc83cb13a5022.html'
# html_page = '/home/home/Downloads/JuniorEx/samples/linkedin/1003_75579261d7f86c3f.html'
# # html_page = '/home/home/environments/pipl_test/samples/linkedin/no_name.html'
# soup = ProfileExtractorLinkedIn(html_page)
#
# print(soup.get_name())
#
# for item in soup.skills:
#     print(item)
#
# for item in soup.education:
#     print(item)
