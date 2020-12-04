import unittest
from unittest.mock import MagicMock, patch
from real import KeyHolder  # type: ignore
import real   # type: ignore


class TestMock(unittest.TestCase):

    def test_real(self):
        """"""
        self.assertEqual(KeyHolder().get_first_key('first'), 'first_real_key')
        self.assertEqual(KeyHolder().get_second_key('second'), 'second_real_second_key')
        self.assertEqual(real.get_doubled_int(10), 20)

    @unittest.skip("skip this test because this test leak the mock")
    def test_mock_bad_example(self):
        """モックの悪い例
        KeyHolder.get_first_key自体が置き換わっているため、他のテストにこのモックを漏らしてしまっている
        """
        KeyHolder.get_first_key = MagicMock(return_value='mock_key')
        self.assertEqual(KeyHolder('first').get_first_key(), 'mock_key')

    @patch.object(KeyHolder, 'get_second_key', return_value='mock_second_key')
    @patch.object(KeyHolder, 'get_first_key', return_value='mock_key')
    def test_mock_good_example_1(self, mock1: MagicMock, mock2: MagicMock):
        """モックの良い例
        @patch.objectデコレータを使ってるので、モックのスコープが関数に閉じている
        引数に渡ってくるmockオブジェクトの順序が、デコレータの実行順序（内側から外側）になっていることに注意
        """
        self.assertEqual(KeyHolder().get_first_key('first'), 'mock_key')
        self.assertEqual(KeyHolder().get_second_key('second'), 'mock_second_key')
        mock1.assert_called_once_with('first')
        mock2.assert_called_once_with('second')

    def test_mock_good_example_2(self):
        """モックの良い例
        withでpatch.objectのスコープを制限している
        """
        with patch.object(KeyHolder, 'get_first_key', return_value='mock_key') as mock1, \
                patch.object(KeyHolder, 'get_second_key', return_value='mock_second_key') as mock2:
            self.assertEqual(KeyHolder().get_first_key('first'), 'mock_key')
            self.assertEqual(KeyHolder().get_second_key('second'), 'mock_second_key')
            mock1.assert_called_once_with('first')
            mock2.assert_called_once_with('second')

    @patch.object(real, 'get_doubled_int', return_value=999)
    def test_module_func_mock_1(self, mock1: MagicMock):
        """モジュール直下に定義されたfunctionをモックする"""
        self.assertEqual(real.get_doubled_int(11), 999)
        mock1.assert_called_once_with(11)

    @patch.object(real, 'get_doubled_int', return_value=999)
    def test_module_func_mock_2(self, mock1: MagicMock):
        """モジュール直下に定義されたfunctionをモックする"""
        self.assertEqual(real.get_doubled_int(11), 999)
        mock1.assert_called_once_with(11)


if __name__ == '__main__':
    unittest.main()
