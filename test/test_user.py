from unittest import TestCase

from kik.user import User


class UserTest(TestCase):
    def test_from_json(self):
        user = User.from_json({
            'firstName': 'First',
            'lastName': 'Last',
            'profilePicUrl': 'http://foo.bar/profile',
            'profilePicLastModified': 1458657367
        })
        self.assertEqual(user.first_name, 'First')
        self.assertEqual(user.last_name, 'Last')
        self.assertEqual(user.profile_pic_url, 'http://foo.bar/profile')
        self.assertEqual(user.profile_pic_last_modified, 1458657367)

    def test_from_json_no_picture(self):
        user = User.from_json({
            'firstName': 'First',
            'lastName': 'Last',
            'profilePicUrl': None,
            'profilePicLastModified': None
        })
        self.assertEqual(user.first_name, 'First')
        self.assertEqual(user.last_name, 'Last')
        self.assertEqual(user.profile_pic_url, None)
        self.assertEqual(user.profile_pic_last_modified, None)
