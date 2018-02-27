from json import JSONDecodeError

from question_2.profile_extractor import ProfileExtractor
import json


class ProfileExtractorBackstage(ProfileExtractor):
    def __init__(self, backstage_html_page):
        self.profile_json = None
        self.education_json = None
        super().__init__(backstage_html_page)

    def validate_template(self):
        self.parse_js()
        if self.profile_json and self.profile_json['display_name']:
            self.is_valid = True

    def set_name(self):
        self.name = self.profile_json['display_name']

    def set_education(self):
        for education_item in self.education_json:
            self.education.append({
                'major': education_item['degree'],
                'years': education_item['created_datetime'],
                'institution_name': education_item['school']
            })

    def set_skills(self):
        for profile_item in self.profile_json['skills']:
            self.skills.append(profile_item['name'])

    def parse_js(self):
        data = str(self.html_page.find_all("script")[9])
        data_array = data.split("\n")
        cleaned_profile_object = data_array[6][:len(data_array[6]) - 1].lstrip("profile_data = ")
        cleaned_education_object = data_array[10][:len(data_array[10]) - 1].lstrip("education_data = ")
        try:
            json_object_profile = json.loads(cleaned_profile_object)
            json_object_education = json.loads(cleaned_education_object)
            self.profile_json = json_object_profile
            self.education_json = json_object_education
        except JSONDecodeError:
            self.is_valid = False

# html_page = '/home/home/environments/pipl_test/samples/backstage/Amanda Forstrom - Professional Profile, Photos, and Video Reels on Backstage -.html'
# html_page = '/home/home/environments/pipl_test/samples/backstage/Joshua Packard - Professional Profile, Photos, and Video Reels on Backstage -.html'
# html_page = '/home/home/environments/pipl_test/samples/backstage/Mark J. Quiles - Professional Profile, Photos, and Video Reels on Backstage -.html'
#
# soup = ProfileExtractorBackstage(html_page)
#
# print("Printing Name:", soup.get_name())
#
# print("Printing Skills:")
# for item in soup.skills:
#     print(item)
#
# print("Printing Education:")
# for item in soup.education:
#     print(item)
