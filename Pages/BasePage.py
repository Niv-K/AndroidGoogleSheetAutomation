import re
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Pages.constants import *
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class BasePage(object):
    def __init__(self,setup):
        self.driver = setup
        # self.resource_handler = resource_handler

    def find_my_element(self,by_locator_tuple):
        by = self.get_locator_type(by_locator_tuple[0])
        locator = str(by_locator_tuple[1])
        element = self.driver.find_element(*(by.lower(), locator))
        return element

    def get_locator_type(self,locator_type_text):
        """
        Get locator type
        :param locator_type:
        :return: locator type text
        :returType: str
        """
        by = str(locator_type_text).lower()
        all_by = {
            "id":By.ID,
            "xpath":By.XPATH,
            "css selector":By.CSS_SELECTOR,
            "class name":By.CLASS_NAME,
            "tag name":By.TAG_NAME,
            "link text":By.LINK_TEXT,
            "partial link text":By.PARTIAL_LINK_TEXT,
            "name":By.NAME
        }
        locator_type = all_by.get(by)
        if locator_type:
            return locator_type
        else:
            raise Exception("Unsupported locator Type. Please change the locator type in the object repo")


    def click_element(self,by_locator_tuple,wait_time = THIRTY_SEC):
        """
        Click on element until its clickabale
        :param tuple by_locator_tuple: e.g.(By.ID,'abc')
        :param int wait_time: Time in second

        """
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator_tuple))
        self.find_my_element(by_locator_tuple).click()

    def enter_text_element(self, by_locator_tuple,value, wait_time=THIRTY_SEC):
        """
        Click on element until its clickabale
        :param tuple by_locator_tuple: e.g.(By.ID,'abc')
        :param int wait_time: Time in second

        """

        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator_tuple))
        el1 = self.find_my_element(by_locator_tuple)
        el1.send_keys(value)

    def click_on_keyboard_return_key(self):
        """
        Clicks on keycode(66) for Return key on Keyboard
        :return: None
        """
        self.driver.press_keycode(66)

    def hide_keyboard_for_otheruse(self):
        self.driver.hide_keyboard()

    def get_element_text(self,by_locator_tuple,wait_time = THIRTY_SEC):
        """
        Click on element until its clickabale
        :param tuple by_locator_tuple: e.g.(By.ID,'abc')
        :param int wait_time: Time in second
        :return: Text of element
        :rettype: str
        """

        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator_tuple))
        return self.find_my_element(by_locator_tuple).text

    def scroll_up(self,ele,fromX,fromY,toX,toY):
        """
        :param ele: Element from where user wants to click
        :param fromX: from X co-ordinate
        :param fromY: from Y co-ordinate
        :param toX:   to X co-ordinate
        :param toY:   to Y co-ordinate
        :return: None
        """
        screen_size = self.driver.get_window_size()
        action = TouchAction(self.driver)
        time.sleep(2)
        # action.press(x=325, y=1115).move_to(x=364, y=431).release().perform()
        # action.tap(x=fromX,y=fromY).perform()
        # action.press(x=fromX, y=fromY).move_to(x=fromX, y=fromY).release().perform()
        self.driver.swipe(fromX,fromY,toX,toY,400)

