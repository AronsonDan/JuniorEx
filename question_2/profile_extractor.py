from abc import abstractmethod
from bs4 import BeautifulSoup


class ProfileExtractor:
    def __init__(self, html_page):
        self.html_page = BeautifulSoup(open(html_page), "html.parser")
        self.name = None
        self.education = []
        self.skills = []
        self.is_valid = False
        self.validate_template()
        if self.is_valid:
            self.set_name()
            self.set_education()
            self.set_skills()

    def get_name(self):
        return self.name

    def get_education(self):
        return self.education

    def get_skills(self):
        return self.skills

    @abstractmethod
    def validate_template(self):
        pass

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def set_education(self):
        pass

    @abstractmethod
    def set_skills(self):
        pass
