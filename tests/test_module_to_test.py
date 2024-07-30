import unittest
from src.module_to_test import ModuleToTest


class ModuleToTestTestCase(unittest.TestCase):

    def setUp(self):
        self.module = ModuleToTest()

    def test_public_method(self):
        self.assertEqual(self.module.public_method(), 2)
