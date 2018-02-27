from unittest import TestCase

from question_2.profile_extractor_indeed import ProfileExtractorIndeed


class TestProfileExtractorIndeed(TestCase):
    def setUp(self):
        self.indeed_profile_html_ok_1 = ProfileExtractorIndeed(
            '../samples/indeed/Key achievements as Finance analyst - Key achievements as ... - London _ Indeed.html')
        self.indeed_profile_html_ok_2 = ProfileExtractorIndeed(
            '../samples/indeed/OSP Site Engineer - OSP Site Engineer - London _ Indeed.html')
        self.indeed_profile_html_ok_3 = ProfileExtractorIndeed(
            '../samples/indeed/Senior Vice President of Contemporary Sourcing - Senior Vice President of ... - New York, NY _ Indeed.html')

    def test_validate_template(self):
        self.assertTrue(self.indeed_profile_html_ok_1.is_valid)
        self.assertTrue(self.indeed_profile_html_ok_2.is_valid)
        self.assertTrue(self.indeed_profile_html_ok_3.is_valid)

    def test_set_name(self):
        self.assertIsNone(self.indeed_profile_html_ok_1.name)
        self.assertIsNone(self.indeed_profile_html_ok_2.name)
        self.assertIsNone(self.indeed_profile_html_ok_3.name)

    def test_set_education(self):
        self.assertEqual(self.indeed_profile_html_ok_1.education, [
            {'major': 'MSc in International Economics',
             'institution_name': 'London Metropolitan Business School, London Metropolitan University - London',
             'years': 'September 2011 to October 2012'},
            {'major': 'MSc in International Finance and Financial Engineering',
             'institution_name': 'Westminster Business School, University of - Westminster',
             'years': 'September 2009 to July 2011'},
            {'major': 'BA in International Business',
             'institution_name': 'London Metropolitan Business School, London Metropolitan University - London',
             'years': 'September 2006 to June 2009'},
            {'major': 'PhD in Economics', 'institution_name': 'City University - London', 'years': None}
        ])
        self.assertEqual(self.indeed_profile_html_ok_2.education, [
            {'years': 'January 1983 to January 1988', 'major': 'Bachelor of Science in Civil Engineering',
             'institution_name': 'University of Nueva Caceres'}
        ]
                         )
        self.assertEqual(self.indeed_profile_html_ok_3.education, [
            {'institution_name': 'Skidmore College', 'major': 'B.A. in Psychology & Sociology', 'years': None},
            {'institution_name': 'Baruch College', 'major': 'Industrial Organizational Psychology', 'years': None}
        ])

    def test_set_skills(self):
        self.assertEqual(self.indeed_profile_html_ok_1.skills, [])
        self.assertEqual(self.indeed_profile_html_ok_2.skills, [])
        self.assertEqual(self.indeed_profile_html_ok_3.skills, [])
