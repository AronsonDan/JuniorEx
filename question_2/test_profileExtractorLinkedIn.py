from unittest import TestCase

from question_2.profile_extractor_linkedin import ProfileExtractorLinkedIn


class TestProfileExtractorLinkedIn(TestCase):
    def setUp(self):
        self.linkedIn_profile_html_ok_1 = ProfileExtractorLinkedIn(
            '/home/home/environments/pipl_test/samples/linkedin/1003_172bc83cb13a5022.html')
        self.linkedIn_profile_html_ok_2 = ProfileExtractorLinkedIn(
            '/home/home/environments/pipl_test/samples/linkedin/1003_75579261d7f86c3f.html')

        self.linkedIn_profile_html_no_name = ProfileExtractorLinkedIn(
            '/home/home/environments/pipl_test/samples/linkedin/no_name.html')

    def test_validate_template(self):
        self.assertTrue(self.linkedIn_profile_html_ok_1.is_valid)
        self.assertTrue(self.linkedIn_profile_html_ok_2.is_valid)
        self.assertFalse(self.linkedIn_profile_html_no_name.is_valid)

    def test_set_name(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.name, 'Irit Schwartz')
        self.assertEqual(self.linkedIn_profile_html_ok_2.name, 'Elmar Bergonzini')
        self.assertIsNone(self.linkedIn_profile_html_no_name.name)

    def test_set_education(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.education, [
            {
                'years': '2010 – 2011',
                'institution_name': 'The Open University',
                'major': 'Human Resource Management and Organizational Behavior'},
            {
                'years': '2001 – 2003',
                'institution_name': 'University of Derby the extension in Israel',
                'major': 'BA in Business Management specializing in Human Resources'
            }
        ])
        self.assertEqual(self.linkedIn_profile_html_ok_2.education,
                         [{
                             'institution_name': "Libera Università 'Maria SS Assunta'",
                             'major': 'editoria e giornalismo',
                             'years': '2009 – 2014'
                         }]
                         )
        self.assertEqual(self.linkedIn_profile_html_no_name.education, [])

    def test_set_skills(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.skills, [
            'Deferred Compensation',
            'Recruiting',
            'Organizational...',
            'Human Resources',
            'Employee Relations',
            'HRIS',
            'Onboarding'
        ])
        self.assertEqual(self.linkedIn_profile_html_ok_2.skills, [])
        self.assertEqual(self.linkedIn_profile_html_no_name.skills, [])
