from unittest import TestCase

from mypackage import mymodule


class TestMyModule(TestCase):
    def test_hey(self):
        with self.assertLogs() as log:
            mymodule.hey()
            self.assertEqual(log.output, ['INFO:mypackage.mymodule:hey'])

    def test_sum_values(self):
        with self.subTest('正常系'):
            self.assertEqual(mymodule.sum_values(1, 2, 3), 6)

        with self.subTest('引数なし'):
            self.assertEqual(mymodule.sum_values(), 0)

        with self.subTest('数値以外を渡す'):
            with self.assertRaises(Exception):
                mymodule.sum_values('123', '456')

        # with self.subTest('かならずエラー'):
        #     self.assertTrue(False)
