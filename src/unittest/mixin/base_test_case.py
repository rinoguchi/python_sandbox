import unittest
import time

from test_webserver import TestWebserver  # type: ignore


class BaseTestCase(unittest.TestCase):
    port_num: int = 9000  # default値。継承先で上書きして利用する

    @classmethod
    def setUpClass(cls):
        print('BaseTestCase.setUpClass started.')
        if TestWebserver in cls.__mro__:
            cls.start_web_server(cls.port_num, cls.__name__)
        time.sleep(1)  # Webサーバが立ち上がるのを1秒待機
        print('BaseTestCase.setUpClass finished.')

    @classmethod
    def tearDownClass(cls):
        print('BaseTestCase.tearDownClass started.')
        if TestWebserver in cls.__mro__:
            cls.stop_web_server(cls.port_num)
        print('BaseTestCase.tearDownClass finished.')
