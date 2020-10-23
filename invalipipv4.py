import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from keyboard import press
import logging

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:4545/wd/hub',
            desired_capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': True
            })
        
    def test_ipv4(self):
        driver = self.driver
        driver.get('https://censys.io/ipv4')
        search = driver.find_element_by_id("q")
        search.send_keys("256.49.198.99")
        press('enter')

    def tearDown(self):
        self.driver.close()

logging.basicConfig(filename='standout.log', level=logging.DEBUG,
                    format='%(asctime)s|%(filename)s|%(message)s|%(pathname)s')

if __name__ == "__main__":
    unittest.main()
