import unittest

from shingles.shingles import *

paragraph = u"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

class ShingledDocumentTestCase(unittest.TestCase):
    def test_shingling_short_document(self):
        short_doc = u'hello there, im short'
        with self.assertRaises(ValueError):
            ShingledDocument(short_doc)

    def test_shingling_paragraph(self):
        shingled_document = ShingledDocument(paragraph, 5, 5, 20)
        self.assertEqual(20, len(shingled_document.minhash))
