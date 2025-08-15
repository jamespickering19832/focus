import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    "utils", Path(__file__).resolve().parents[1] / "app" / "utils.py"
)
utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utils)
allowed_file = utils.allowed_file

class AllowedFileTestCase(unittest.TestCase):
    def test_allows_csv(self):
        self.assertTrue(allowed_file('data.csv'))

    def test_rejects_txt(self):
        self.assertFalse(allowed_file('notes.txt'))

if __name__ == '__main__':
    unittest.main()
