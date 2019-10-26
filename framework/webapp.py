import os
from datetime import datetime
from exceptions.exceptions import (ElementNotClickableException,
                                   ElementNotFoundException)
from traceback import print_stack
from urllib.parse import urljoin

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

import utilities.custom_logger as cl
from test_config.config import config


class WebBrowser():
    instance = None

    log = cl.CustomLogger()

    def __init__(self, context):
        self.driver = context.driver
        self.context = context

    def get_element(self, element):
        """Espera e retorna o elemento

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        """
        try:
            el = self.wait_element(element, timeout=10)
            self.log.info("Element found in get element... "+element)
        except:
            el = None
            self.log.info("Element not found in get element...")
        return el

    def wait_element(self, element, timeout=10):
        """Espera o elemento ser exibido na tela pelo tempo definido pelo usuário    

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        @param timeout(int): tempo máximo de espera
        """
        try:
            self.log.info("Waiting for :: " + str(timeout) +
                          " :: seconds for element "+element)
            element = WebDriverWait(self.context.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element))
            )
            print("---------------------------------------\n")
            print("el:", element)
        except ElementNotFoundException:
            self.log.error("Element was not found in wait element...")
            raise
        except TimeoutException:
            self.log.error("Element was not found in wait element...")
            raise

        return element

    def click_on(self, element):
        """Clica no elemento

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        """
        try:
            element = self.get_element(element)
            element.click()
            self.log.info("Clicked on : ", element)
        except (ElementNotClickableException, ElementNotFoundException):
            print_stack()
            raise

    def send_keys(self, element, text=""):
        """Envia texto ao elemento

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        @param text(str)
        """
        try:
            element = self.get_element(element)
            element.send_keys(text)
            self.log.info("Keys sent to: ", element)
        except ElementNotFoundException:
            self.log.error("Could not send keys to element: ", element)
            print_stack()
            raise

    def select_element_by_text(self, element, text=""):
        """Seleciona o elemento em um menu do tipo select pelo atributo texto    

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        @param text(str)
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(element))
            select = Select(element)
            select.select_by_visible_text(text)
            self.log.info("Selected element from menu: " + element)
        except:
            self.log.info("Could not select element: " + element)
            print_stack()

    def select_element_by_index(self, element, index=0):
        """select element passing index argument
        
        Arguments:
            element {[webelement]}
        
        Keyword Arguments:
            index {int} (default: {0})
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(By.XPATH(element)))
            select = Select(element)
            select.select_by_index(index)
            self.log.info("Selected element from menu: " + element)
        except:
            self.log.info("Could not select element: " + element)
            print_stack()

    def is_element_present(self, element):
        """Verifica se o elemento está presente. Retorna true caso esteja
        e false caso não.    

        @param locator_type(str): tipo de locator usado na busca
        @param locator(str): identificador do elemento
        """
        try:
            element = self.get_element(element)
            if element:
                self.log.info("Element found...")
                return True
            else:
                self.log.info("Element not found...")
                return False
        except:
            self.log.info("Element not found...")
            return False

    def go_to_page(self, url):
        self.driver.get(url)

    def TakeScreenshot(self, resultMessage):
        """Tira screenshot da tela e salva no diretório do teste

        @param resultMessage(str): parte do nome do arquivo
        """
        folder_name = os.path.join(str(pytest.time_start_format), self.context.scenario.name.replace(
            '@', '').replace(' ', '').replace('-', '_') + '/')
        pytest.screenshotDirectory = os.path.join('screenshots/', folder_name)
        file_name = str(datetime.now().strftime("%H_%M_%S")) + \
            '_' + resultMessage.replace(' ', '_') + '.png'
        final_file = pytest.screenshotDirectory + file_name
        try:
            if not os.path.exists(pytest.screenshotDirectory):
                os.makedirs(pytest.screenshotDirectory)
            self.driver.save_screenshot(final_file)
            self.log.info("Screenshot saved to: " + final_file)
        except:
            self.log.error("### Exception Ocurred")
            print_stack()

    def alert_handler(self, action='accept', text=None):
        alert_obj = self.context.driver.switch_to.alert
        if action == 'accept':
            if text:
                alert_obj.send_keys()
            alert_obj.accept()
        elif action == 'cancel':
            alert_obj.dismiss()
