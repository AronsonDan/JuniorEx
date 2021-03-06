import re

from question_2.profile_extractor import ProfileExtractor


class ProfileExtractorIndeed(ProfileExtractor):
    def __init__(self, indeed_html_page):
        self.delimiters = ['♦', ',']
        self.regexPattern = '|'.join(map(re.escape, self.delimiters))
        self.remove_from_additional_info = ['Core Competencies include: ', 'Relevant Skills']
        super().__init__(indeed_html_page)

    def validate_template(self):
        self.is_valid = True

    def set_name(self):
        pass

    def set_education(self):
        def find_institution(bs4_element):
            institution_element = bs4_element.find('div', {'class': "edu_school"})
            if institution_element:
                return institution_element.text
            else:
                return None

        def find_major(bs4_element):
            major_element = bs4_element.find('p', {'class': "edu_title"})
            if major_element:
                return major_element.text
            else:
                return None

        def find_years(bs4_element):
            years_element = bs4_element.find('p', {'class': "edu_dates"})
            if years_element:
                return years_element.text
            else:
                return None

        for element in self.html_page.find_all('div', {'class': re.compile('education-section .*')}):
            self.education.append({
                # "institution_name": find_institution(element),
                "major": find_major(element),
                "years": find_years(element)
            })

    def set_skills(self):
        def has_skill_text():
            skills_section = self.html_page.find('span', {'class': "skill-text"})
            if skills_section:
                return skills_section.text
            else:
                return None

        def has_additional_info():
            skills_section = self.html_page.find('div', {'id': "additionalinfo-section"})
            if skills_section:
                return skills_section.text
            else:
                return None

        if has_skill_text():
            skills_string = has_skill_text()
            self.skills = [skill_item.strip() for skill_item in skills_string.split(',')]
        else:
            skills_string = has_additional_info()
            for string_to_remove in self.remove_from_additional_info:
                if skills_string[:len(string_to_remove)] == string_to_remove:
                    skills_string = skills_string[len(string_to_remove):]
            print("skills_string", re.split(self.regexPattern, skills_string))
            self.skills = [skill.strip() for skill in re.split(self.regexPattern, skills_string)]



html_page = '/home/home/environments/pipl_test/samples/indeed/Key achievements as Finance analyst - Key achievements as ... - London _ Indeed.html'
html_page = '/home/home/environments/pipl_test/samples/indeed/OSP Site Engineer - OSP Site Engineer - London _ Indeed.html'
html_page = '/home/home/environments/pipl_test/samples/indeed/Senior Vice President of Contemporary Sourcing - Senior Vice President of ... - New York, NY _ Indeed.html'
soup = ProfileExtractorIndeed(html_page)

# print(soup.get_name())
print("Printing Skills:")
for item in soup.skills:
    print(item)
print("Printing Education:")
for item in soup.education:
    print(item)
