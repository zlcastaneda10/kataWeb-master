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

    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(3)
        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')
        self.browser.implicitly_wait(3)
        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')
        self.browser.implicitly_wait(3)
        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')
        self.browser.implicitly_wait(3)
        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador WEB']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')
        self.browser.implicitly_wait(3)
        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')
        self.browser.implicitly_wait(3)
        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('jediondo')
        self.browser.implicitly_wait(3)
        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')
        self.browser.implicitly_wait(3)
        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        self.browser.implicitly_wait(3)
        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)