import unittest


class TestSimpleChild(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """各クラスが実行される直前に一度だけ呼び出される"""
        print('setUpClass called.')

    @classmethod
    def tearDownClass(cls):
        """各クラスが実行された直後に一度だけ呼び出される"""
        print('tearDownClass called.')

    def setUp(self):
        """各テストメソッドが実行される直前に呼び出される"""
        print('setUp called.')

    def tearDown(self):
        """各テストメソッドが実行された直後に呼び出される"""
        print('tearDown called.')

    def test_lower(self):
        print(f'test_lower called. self_id: {id(self)}')
        self.assertEqual('HOGE'.lower(), 'hoge')

    def test_upper(self):
        print(f'test_upper called. self_id: {id(self)}')
        self.assertEqual('hoge'.upper(), 'HOGE')

    @unittest.skip("this test method will be skipped")
    def test_split(self):
        print(f'test_split called. self_id: {id(self)}')
        self.assertEqual(len('aa bb'.split()), 2)


if __name__ == '__main__':
    unittest.main()
