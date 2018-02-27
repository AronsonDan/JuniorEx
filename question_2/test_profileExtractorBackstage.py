from unittest import TestCase

from question_2.profile_extractor_backstage import ProfileExtractorBackstage


class TestProfileExtractorBackstage(TestCase):
    def setUp(self):
        self.backstage_profile_html_ok_1 = ProfileExtractorBackstage(
            '../samples/backstage/Amanda Forstrom - Professional Profile, Photos, and Video Reels on Backstage -.html')
        self.backstage_profile_html_ok_2 = ProfileExtractorBackstage(
            '../samples/backstage/Joshua Packard - Professional Profile, Photos, and Video Reels on Backstage -.html')

        self.backstage_profile_html_ok_3 = ProfileExtractorBackstage(
            '../samples/backstage/Mark J. Quiles - Professional Profile, Photos, and Video Reels on Backstage -.html')

        self.backstage_profile_html_no_name = ProfileExtractorBackstage(
            '../samples/backstage/no_name.html')

    def test_validate_template(self):
        self.assertTrue(self.backstage_profile_html_ok_1.is_valid)
        self.assertTrue(self.backstage_profile_html_ok_2.is_valid)
        self.assertTrue(self.backstage_profile_html_ok_3.is_valid)
        self.assertFalse(self.backstage_profile_html_no_name.is_valid)

    def test_set_name(self):
        self.assertEqual(self.backstage_profile_html_ok_1.name, 'Amanda Forstrom')
        self.assertEqual(self.backstage_profile_html_ok_2.name, 'Joshua Packard')
        self.assertEqual(self.backstage_profile_html_ok_3.name, 'Mark J. Quiles')
        self.assertIsNone(self.backstage_profile_html_no_name.name)

    def test_set_education(self):
        self.assertEqual(self.backstage_profile_html_ok_1.education, [
            {
                'years': '1970-01-01T00:00:00',
                'major': 'MFA Acting',
                'institution_name': 'University of South Carolina'
            }
        ])
        self.assertEqual(self.backstage_profile_html_ok_2.education, [
            {'major': '2 week summer acting for film', 'institution_name': 'NY Film Academy',
             'years': '2017-09-11T14:40:12'},
            {'major': 'Various acting classes', 'institution_name': "Actor's Technique NY",
             'years': '2017-02-17T15:35:45'},
            {'major': 'NA', 'institution_name': 'Barrow Theater School', 'years': '2017-01-24T18:09:59'},
            {'major': 'NA', 'institution_name': 'The Stage Theater School', 'years': '2017-01-24T18:09:59'},
            {'major': 'NA', 'institution_name': 'Joyful Singing', 'years': '2017-01-24T18:09:59'},
            {'major': 'summer class', 'institution_name': 'A Class Act NY', 'years': '2017-01-24T18:09:59'}
        ])
        self.assertEqual(self.backstage_profile_html_ok_3.education, [
            {'institution_name': 'McKenzie/ Delevan Studios', 'major': 'Voice', 'years': '1970-01-01T00:00:00'},
            {'institution_name': 'Tim Welch Music', 'major': 'Voice', 'years': '1970-01-01T00:00:00'},
            {'institution_name': 'Coupe Dance Studio', 'major': 'Tap Dance/ Theatre Dance',
             'years': '1970-01-01T00:00:00'},
            {'institution_name': 'Willful Productions', 'major': 'Shakespeare Acting & Private Coaching',
             'years': '1970-01-01T00:00:00'},
            {'institution_name': 'The Real Stage', 'major': 'Acting', 'years': '1970-01-01T00:00:00'},
            {'institution_name': 'Montclair State University', 'major': 'M.A. Education Admin. & Educ. Trainer',
             'years': '1970-01-01T00:00:00'},
            {'institution_name': 'William Paterson University', 'major': 'M. Ed. - Elem. Ed./ Bilingual Ed.',
             'years': '1970-01-01T00:00:00'},
            {'institution_name': 'Calvin College', 'major': 'B. A. - Theatre/ Telecommunications',
             'years': '1970-01-01T00:00:00'}
        ])
        self.assertEqual(self.backstage_profile_html_no_name.education, [])

    def test_set_skills(self):
        self.assertEqual(self.backstage_profile_html_ok_1.skills, [
            'Music/Musician',
            'Accents/Dialects',
            'Fight Training',
            'Horseback Riding',
            'Improvisation',
            'Firearms Training',
            'Ballet',
            'Shakespeare Training',
            'Clown Training',
            'Acrobatics',
            'Sight Reading',
            'Athletic',
            'Foreign Language',
            'Singer',
            'Lyrical',
            'Jazz',
            'Tap',
            'Pointe',
            'Basic Ballroom'
        ])
        self.assertEqual(self.backstage_profile_html_ok_2.skills, [])
        self.assertEqual(self.backstage_profile_html_ok_3.skills, [
            'Bilingual/ Biliterate - English/ Spanish',
            'Can Drive Stick Shift (Manual)',
            'Certified School Teacher/ Administrator',
            'First Aid/ Cpr Trained',
            'Improvisation',
            'Lighting Design',
            'Oil Painting',
            'Stage Construction/ Carpentry',
            'Stage/ Prop Design',
            'Tae Kwon Do',
            'Tap',
            'Works Well With Children'
        ])
        self.assertEqual(self.backstage_profile_html_no_name.skills, [])
