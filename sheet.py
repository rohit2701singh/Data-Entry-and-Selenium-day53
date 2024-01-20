from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class FillSheet:
    def __init__(self, place_detail, form_url):

        self.__place_detail = place_detail
        self.__fill_google_form(self.__place_detail, form_url)

    def __fill_google_form(self, detail, url):

        for item in detail:

            self.__driver = webdriver.Chrome()
            self.__driver.get(url)

            time.sleep(2)
            rent_fill = self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(2)
            rent_fill.click()
            rent_fill.send_keys(item["place_rent"])

            time.sleep(2)
            address_fill = self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            time.sleep(2)
            address_fill.click()
            address_fill.send_keys(item["address"])

            time.sleep(2)
            address_link_fill = self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            time.sleep(3)
            address_link_fill.click()
            address_link_fill.send_keys(item["address_link"])

            time.sleep(2)
            submit = self.__driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            time.sleep(2)
            submit.click()
            time.sleep(3)

            self.__driver.quit()
