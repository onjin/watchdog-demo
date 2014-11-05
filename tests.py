#!/usr/bin/env python
# encoding: utf-8

import unittest
from mylib import some, one


class SomeTestCase(unittest.TestCase):
    def test_some_case(self):
        self.assertTrue(some(1))


class OneTestCase(unittest.TestCase):
    def test_one_case(self):
        self.assertFalse(one(0))
        self.assertTrue(one(1))
