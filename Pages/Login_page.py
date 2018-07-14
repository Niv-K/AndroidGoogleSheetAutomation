from Pages.BasePage import *
from Pages.readexceldata import *

class LoginPage(BasePage):
    object_repo_data = convert_sheet_to_dict("Test_login","ObjectRepository")
    SIGNIN_BTN = get_locator_tuple_from_list_of_dictionary(object_repo_data,"Sign_in_btn")
    EMAIL_TEXTBOX = get_locator_tuple_from_list_of_dictionary(object_repo_data,"Email_textbox")
    PASSWORD_TEXTBOX = get_locator_tuple_from_list_of_dictionary(object_repo_data,"Password_textbox")
    LOGIN_BTN = get_locator_tuple_from_list_of_dictionary(object_repo_data,"Login_btn")
    WHAT_TEXT = get_locator_tuple_from_list_of_dictionary(object_repo_data,"What_text")
    VALID_USER_ID_ACCOUNT = get_locator_tuple_from_list_of_dictionary(object_repo_data,"account_confirmation")
    data_repo = convert_sheet_to_dict("Test_login","DataRepository")
    ACCOUNT_EMAIL = data_repo['Email']
    PASSWORD = data_repo['Password']


    def __init__(self,setup):
        # self.driver = setup.driver
         super(LoginPage,self).__init__(setup)

    def click_on_signIn(self):

        """
        Click on sign in btn,gets locator type and locator from Object Repo sheet.

        """
        self.scroll_up(self.SIGNIN_BTN, 325, 1115, 365, 431)
        self.click_element(self.SIGNIN_BTN)

    def sign_in_with_valid_user(self):
        """
        Finds element to input text field,gets text field from google sheet.

        Enters input in Email field Data is read from google sheet.
        Enters password in password field Data is read from google sheet
        """
        self.enter_text_element(self.EMAIL_TEXTBOX,self.ACCOUNT_EMAIL)
        self.click_on_keyboard_return_key()
        self.enter_text_element(self.PASSWORD_TEXTBOX, self.PASSWORD)
        self.hide_keyboard_for_otheruse()
        self.click_element(self.LOGIN_BTN)

    def verify_signin_valid_user(self):
        """
        Finds element with xpath for user's account gets it from from google sheet.
        gets data for data verification from google sheet. i.e read value user email id.
        :return: text from attribute field.

        """
        self.scroll_up(self.SIGNIN_BTN, 325, 1115, 365, 431)
        account_id = self.get_element_text(self.VALID_USER_ID_ACCOUNT)
        return account_id,self.ACCOUNT_EMAIL



