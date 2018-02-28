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
        self.assertIsNone(self.indeed_profile_html_ok_1.get_name())
        self.assertIsNone(self.indeed_profile_html_ok_2.get_name())
        self.assertIsNone(self.indeed_profile_html_ok_3.get_name())

    def test_set_education(self):
        self.assertEqual(self.indeed_profile_html_ok_1.get_education(), [
            {'years': 'September 2011 to October 2012', 'major': 'MSc in International Economics'},
            {'years': 'September 2009 to July 2011', 'major': 'MSc in International Finance and Financial Engineering'},
            {'years': 'September 2006 to June 2009', 'major': 'BA in International Business'},
            {'years': None, 'major': 'PhD in Economics'}
        ])
        self.assertEqual(self.indeed_profile_html_ok_2.get_education(), [
            {'major': 'Bachelor of Science in Civil Engineering', 'years': 'January 1983 to January 1988'}
        ]
                         )
        self.assertEqual(self.indeed_profile_html_ok_3.get_education(), [
            {'years': None, 'major': 'B.A. in Psychology & Sociology'},
            {'years': None, 'major': 'Industrial Organizational Psychology'}
        ])

    def test_set_skills(self):
        self.assertEqual(self.indeed_profile_html_ok_1.get_skills(), [
            'Teaching: Class management',
            'Motivating pupils',
            'Marking coursework',
            'Subject matter knowledge',
            'Organising activities etc.'
        ])
        self.assertEqual(self.indeed_profile_html_ok_2.get_skills(),
                         ['Professional Driver', 'DrProfessional Driver', 'Drafting and Computer Literate (MS Word',
                          'Excel', 'Powerpoint', 'Pagemaker and Adobe Corel Draw)'])
        self.assertEqual(self.indeed_profile_html_ok_3.get_skills(), [
            'Strategic Operational Planning & Leadership',
            'Policy Development',
            'Process Improvement Product Development',
            'Production',
            'Quality Assurance',
            'Strategic and Global Sourcing International Business',
            'Cost Reduction',
            'Cost & Benefit Analysis',
            'Expense Control'
        ])
