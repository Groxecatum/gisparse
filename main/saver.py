# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time
import random


FILENAME = '1st.csv'
START_WITH = 1
TRESHOLD = 450

class GisParser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.base_url = "https://moscow.uk/"
        self.verificationErrors = []

    def test_save(self):
        driver = self.driver
        file = open(FILENAME, "a")
        page = 1
        while True:
            driver.get("https://2gis.kz/almaty/search/салон красоты/page/" + str(page))
            articles = driver.find_elements_by_xpath("//article")
            time.sleep(random.randint(2, 3))
            if not articles:
                break

            for article in articles:
                time.sleep(random.randint(2, 3))
                article.click()

                name = article.find_element_by_class_name("miniCard__headerTitleLink")
                nameStr = ''
                if name:
                    nameStr = name.get_attribute('text').replace(",", " ")

                print nameStr
                file.write(('\n' + nameStr).encode('utf-8'))

                address = article.find_element_by_class_name("miniCard__address")
                #print address.get_attribute('innerHTML').replace("&nbsp;", "")
                addressStr = ''
                if address:
                    addressStr = address.get_attribute('innerHTML').replace(",", " ").replace("&nbsp;", "")

                print addressStr
                file.write(("," + addressStr).encode('utf-8'))

                # Именно Driver - ищем не в article
                phones = driver.find_elements_by_class_name("contact__phonesItemLink")
                for phone in phones:
                    phoneStr = ''
                    if phone:
                        phoneStr = phone.get_attribute('text')

                    if phoneStr:
                        file.write(("," + phoneStr).encode('utf-8'))
                        print phoneStr
            page += 1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()