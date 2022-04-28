import unittest
import subprocess


class TestArgumentParser(unittest.TestCase):

    def setUp(self) -> None:
        print('Before tests')

    def tearDown(self) -> None:
        print('After tests')

    def test_parser_version(self):
        version = subprocess.run(['rss_reader', '--version'], check=True, capture_output=True, text=True)
        self.assertEqual(version.stdout, 'RSS-Reader version is 4.0.0\n')

    def test_parser_help(self):
        helper = subprocess.run(['rss_reader', '--help'], check=True, capture_output=True, text=True)
        self.assertEqual(helper.returncode, 0)

if __name__ == '__main__':
    unittest.main()
