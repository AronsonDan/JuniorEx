from unittest import TestCase

from question_2.profile_extractor_linkedin import ProfileExtractorLinkedIn


class TestProfileExtractorLinkedIn(TestCase):
    def setUp(self):
        self.linkedIn_profile_html_ok_1 = ProfileExtractorLinkedIn(
            '../samples/linkedin/1003_172bc83cb13a5022.html')
        self.linkedIn_profile_html_ok_2 = ProfileExtractorLinkedIn(
            '../samples/linkedin/1003_75579261d7f86c3f.html')

        self.linkedIn_profile_html_no_name = ProfileExtractorLinkedIn(
            '../samples/linkedin/no_name.html')

    def test_validate_template(self):
        self.assertTrue(self.linkedIn_profile_html_ok_1.is_valid)
        self.assertTrue(self.linkedIn_profile_html_ok_2.is_valid)
        self.assertFalse(self.linkedIn_profile_html_no_name.is_valid)

    def test_set_name(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.get_name(), 'Irit Schwartz')
        self.assertEqual(self.linkedIn_profile_html_ok_2.get_name(), 'Elmar Bergonzini')
        self.assertIsNone(self.linkedIn_profile_html_no_name.get_name())

    def test_set_education(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.get_education(), [
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
        self.assertEqual(self.linkedIn_profile_html_ok_2.get_education(),
                         [{
                             'institution_name': "Libera Università 'Maria SS Assunta'",
                             'major': 'editoria e giornalismo',
                             'years': '2009 – 2014'
                         }]
                         )
        self.assertEqual(self.linkedIn_profile_html_no_name.get_education(), [])

    def test_set_skills(self):
        self.assertEqual(self.linkedIn_profile_html_ok_1.get_skills(), [
            'Deferred Compensation',
            'Recruiting',
            'Organizational...',
            'Human Resources',
            'Employee Relations',
            'HRIS',
            'Onboarding'
        ])
        self.assertEqual(self.linkedIn_profile_html_ok_2.get_skills(), [])
        self.assertEqual(self.linkedIn_profile_html_no_name.get_skills(), [])
