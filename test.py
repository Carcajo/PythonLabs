import re
import unittest

from commands import reg


class MyTest(unittest.TestCase):
    def test_CommandRegEx(self):
        match_obj = re.match(reg, "add \"Bibster\"")
        self.assertEqual(match_obj.group(1), "add")
        self.assertEqual(match_obj.group(2), " \"Bibster\"")
        self.assertEqual(match_obj.group(3), "Bibster")

        match_obj = re.match(reg, "save")
        self.assertEqual(match_obj.group(1), "save")
        self.assertEqual(match_obj.group(2), None)