import pytest
from appium import webdriver
import os
from subprocess import Popen, PIPE, STDOUT
import time


# class ResourceHandler(object):
#
#     driver = None
#     nodejs_process = None

@pytest.fixture(scope = "session")
def setup(request):
    node = StartNode()
    node.start_nodejs()
    print("--->Done Starting Appium")


    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                         # self.driver = webdriver.Remote(command_executor='http://0.0.0.0:4723/wd/hub',
                                         desired_capabilities={
                                           'platformName': 'Android',
                                           # 'deviceName': 'Samsung Galaxy S7 edge',
                                           'deviceName': 'Moto X',
                                           'noReset': 'True',
                                            'appPackage':'com.indeed.android.jobsearch',
                                            'appActivity':'com.indeed.android.jobsearch.MainActivity'
                                            # 'unicodeKeyboard':'True',
                                            # 'resetKeyboard':'True'
                                             # 'inputType':'textNoSuggestion'
                                           # 'appPackage': 'com.dice.app.jobs',
                                           # 'appActivity': 'com.dice.app.jobs.activities.MainDiceActivity'


                                         })

    def tear_down():
        driver.quit()
        node.stop_nodejs()
        print("--->Done,Closing driver and node")

    request.addfinalizer(tear_down)
    return driver

class StartNode():
    nodejs_process = None

    def start_nodejs(self):
        """Tries to start Node JS web server with Appium module"""
        # appium_home = self.get_env_variable("APPIUM_HOME", "Appium checkout folder", "/usr/local/bin")
        # nodejs_bin = self.get_env_variable('NODEJS_BIN', "Node JS executable", "/usr/local/bin/node")

        working_directory = os.getcwd()
        # os.chdir(appium_home)
        self.nodejs_process = Popen(["appium"], stdout=PIPE, stderr=STDOUT)
        os.chdir(working_directory)
        self.wait_nodejs()
        print("==>Done Starting nodejs")

    def stop_nodejs(self):
        """Stops Node JS if server was started"""
        if self.nodejs_process is not None:
          self.nodejs_process.terminate()
          self.nodejs_process = None

    def get_env_variable(self, name, description=None, example=None):
        appium_home = os.environ.get(name)
        if not appium_home:
          print("Appium not present")
        return appium_home

    def wait_nodejs(self):
        """Waits Node JS server to start"""
        i = 0
        time.sleep(0.5)
        while True:
          nodejs_stdout = self.nodejs_process.stdout.readline()
          print("====>", nodejs_stdout)

          if "Could not start" in str(nodejs_stdout):
            # let's try to reuse existing Node JS server
            break

          if not "listener started" in str(nodejs_stdout):
            if i == 10:
              raise Exception("Unable to start nodejs")
            else:
              i += 1
              time.sleep(0.5)
          else:
            break

        time.sleep(0.5)


