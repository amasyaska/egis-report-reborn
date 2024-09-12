import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestIndexPage(StaticLiveServerTestCase):

    def setUp(self):
        self.webdriver = webdriver.Firefox()

    def tearDown(self):
        self.webdriver.close()
    
    def test_correct_input(self):
        self.webdriver.get(self.live_server_url)

        file_amount_input = self.webdriver.find_element(By.XPATH, '//*[@id="xlsx_files_amount"]')
        file_amount_button = self.webdriver.find_element(By.XPATH, '//*[@id="file_amount_button"]')
        
        file_amount_input.send_keys("2")
        file_amount_button.click()

    def test_incorrect_input(self):
        self.webdriver.get(self.live_server_url)

        file_amount_input = self.webdriver.find_element(By.XPATH, '//*[@id="xlsx_files_amount"]')
        file_amount_button = self.webdriver.find_element(By.XPATH, '//*[@id="file_amount_button"]')
        
        file_amount_input.send_keys("ads")
        file_amount_button.click()

        incorrect_input_label = self.webdriver.find_element(By.XPATH, '/html/body/div[2]/div/label')
        self.assertEqual(incorrect_input_label.text, "incorrect input")

