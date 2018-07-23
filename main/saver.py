# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest
import time
import common
import random


FILENAME = '1st.txt'
START_WITH = 1
TRESHOLD = 450

class GisParser(unittest.TestCase):

    def setUp(self):

        profile = webdriver.FirefoxProfile()

        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        #profile.set_preference('browser.download.dir', '/home/ysklyarov/Загрузки')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf;application/msword;application/rtf')

        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)

        profile.set_preference("plugin.scan.Acrobat", "99.0")
        profile.set_preference("plugin.scan.plid.all", False)

        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(60)
        self.base_url = "https://moscow.uk/"
        self.verificationErrors = []
        self.accept_next_alert = True

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
                name = driver.find_element_by_class_name("link miniCard__headerTitleLink")
                file.write(name)

                phones = driver.find_elements_by_class_name("contact__phonesItemLink")
                for phone in phones:
                    if phone.get_attribute('text'):
                        file.write("," + phone.get_attribute('text'))

                        #print phone.get_attribute('innerHTML')
                        #print phone.get_attribute('text')

            page += 1
            #driver.find_element_by_xpath("//div[@id='module-1-13-2-1-1']/div/div[2]/div/a/bdo").click()
            #driver.find_element_by_xpath("//div[@id='module-1-13-2-1-1']/div/div/div[3]").click()
            #driver.find_element_by_xpath("//div[@id='module-1-13-2']/div[3]/div[2]/a[2]").click()
            #driver.find_element_by_xpath("//article[@id='module-1-13-1-1-1-13']/div").click()
            #driver.find_element_by_xpath("//div[@id='module-1-13-3']/div[3]/div[2]/a[2]").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()