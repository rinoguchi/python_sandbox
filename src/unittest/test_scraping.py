import unittest
import requests
from requests import Response
from scraping_base_test_case import ScrapingBaseTestCase  # type: ignore
from bs4 import BeautifulSoup


class TestScraping(ScrapingBaseTestCase):

    @classmethod
    def setUpClass(cls):
        print('TestScraping.setUpClass started.')
        cls.port_num = 9001
        super().setUpClass()
        print('TestScraping.setUpClass finished.')

    def test_get_body_text(self):
        print('test_get_body_text started.')
        response: Response = requests.get(f'http://localhost:{TestScraping.port_num}/hello_world.html')
        soup: BeautifulSoup = BeautifulSoup(response.text)
        self.assertEqual(soup.body.text, 'hello world!!')
        print('test_get_body_text finished.')

    def test_get_body_length(self):
        print('test_get_body_length started.')
        response: Response = requests.get(f'http://localhost:{TestScraping.port_num}/hello_world.html')
        soup: BeautifulSoup = BeautifulSoup(response.text)
        self.assertEqual(len(soup.body.text), 13)
        print('test_get_body_length finished.')


if __name__ == '__main__':
    unittest.main()
