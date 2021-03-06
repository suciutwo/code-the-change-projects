"""Tests for the user model."""

import unittest

from ctc.models import user as user_model
from ctc.testing import testutil


# Tests don't need docstrings, so pylint: disable=C0111
class UserTests(testutil.CtcTestCase):

    def test_get_current_user_key(self):
        # It should return None when not logged in.
        self.assertEqual(user_model.get_current_user_key(), None)
        self.assertEqual(user_model.User.query().count(), 0)
        # It should create the user and return it when logged in.
        self.testbed.setup_env(
            USER_EMAIL='test@codethechange.org',
            USER_ID='hello',
            overwrite=True)
        user_key = user_model.get_current_user_key()
        self.assertEqual(user_key.id(), 'hello')
        self.assertEqual(user_model.User.query().count(), 1)
        # It should return the existing user without creating when there is
        # already a user.
        user_key = user_model.get_current_user_key()
        self.assertEqual(user_key.id(), 'hello')
        self.assertEqual(user_model.User.query().count(), 1)


if __name__ == '__main__':
    unittest.main()
