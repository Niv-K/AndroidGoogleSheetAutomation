import pytest
from Pages.Login_page import *
import pytest
from appium import webdriver
import os
from subprocess import Popen, PIPE, STDOUT
import time


@pytest.fixture()
def login_obj(setup):
     login_page_object = LoginPage(setup)
     return login_page_object

class TestLogin(object):
    def test_login_with_valid_credentials(self,login_obj):
        """
        Description: Verify " Login page" functionality
        Test steps
         1. Login into Indeed's account with valid user ID and passord
        Expected result
         1. When User scrolls down User's email id should match with User's current ID.
        """
        login_obj.click_on_signIn()
        login_obj.sign_in_with_valid_user()
        actual_id,expected_id=login_obj.verify_signin_valid_user()
        print("Id's are {} and {}".format(actual_id , expected_id))

        assert actual_id == expected_id
