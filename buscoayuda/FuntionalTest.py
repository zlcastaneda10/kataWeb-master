import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class FunctionalTest(TestCase):
    def setUp(self):
        #self.browser = webdriver.Chrome('C:/chromedriver.exe')
        self.browser = webdriver.Chrome('/Users/ChrisMartin/PycharmProjects/demokatatdd_django-002/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Busco Ayuda', self.browser.title)

