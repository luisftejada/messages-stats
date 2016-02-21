from selenium import webdriver
import unittest
import os
import time

DEBUG = not os.environ.get('OPENSHIFT_MYSQL_DB_HOST')
host = 'localhost' if DEBUG else 'https://stats-luisftejada.rhcloud.com'
port = ':8000' if DEBUG else ''

class StatsFuctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_stats_get1(self):
        url1 = '{server}{port}/stats/get1'.format(server=host, port=port)
        self.browser.get(url1)
        self.assertTrue('"result": "success"' in self.browser.page_source)

    def test_stats_get1_changes_after_one_minute(self):
        # Note this test will fail if the cron has not been setup
        url1 = '{server}{port}/stats/get1'.format(server=host, port=port)
        self.browser.get(url1)
        current_page = self.browser.page_source
        time.sleep(61)
        self.browser.get(url1)
        new_page = self.browser.page_source
        self.assertFalse(current_page == new_page)

    def test_stats_get2_changes_after_one_minute(self):
        # Note this test will fail if the command "python manage.py createcachetable"
        url1 = '{server}{port}/stats/get2'.format(server=host, port=port)
        self.browser.get(url1)
        current_page = self.browser.page_source
        time.sleep(61)
        self.browser.get(url1)
        new_page = self.browser.page_source
        self.assertFalse(current_page == new_page)

    def test_stats_get2(self):
        url1 = '{server}{port}/stats/get2'.format(server=host, port=port)
        self.browser.get(url1)
        self.assertTrue('"result": "success"' in self.browser.page_source)

if __name__ == '__main__':
    unittest.main()
