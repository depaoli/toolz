#!/usr/bin/env python

import unittest
from depaoli_pylib.type7decrypt import type7decrypt

class TestCaseDP_T7D(unittest.TestCase):

    def setUp(self):
        pass

    def test_type7decrypt(self):
        self.assertEqual(type7decrypt('095C4F1A0A1218000F'), 'password')

if __name__ == '__main__':
    unittest.main()
