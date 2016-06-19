import unittest

from shingles.shingles import *

paragraph = u"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

rearranged_paragraph = u"""
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqual. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo conseua
"""

another_paragraph = u"""
Apparently she had forgotten her age and by force of habit employed all
the old feminine arts. But as soon as the prince had gone her face
resumed its former cold, artificial expression. She returned to the
group where the vicomte was still talking, and again pretended to
listen, while waiting till it would be time to leave. Her task was
accomplished.
"""

class ShingledDocumentTestCase(unittest.TestCase):
    def test_shingling_short_document(self):
        short_doc = u'hello there, im short'
        with self.assertRaises(ValueError):
            ShingledDocument(short_doc)

    def test_shingling_paragraph(self):
        shingled_document = ShingledDocument(paragraph, 5, 5, 20)
        self.assertEqual(20, len(shingled_document.minhash))

    def test_similarity(self):
        shingled_doc = ShingledDocument(paragraph, 5, 5, 20)
        rearranged_shingled_doc = ShingledDocument(
                rearranged_paragraph, 5, 5, 20)
        shingled_diff_doc = ShingledDocument(another_paragraph, 5, 5, 20)
        self.assertTrue(0.6 <= shingled_doc.similarity(
            rearranged_shingled_doc))
        self.assertTrue(0.5 > shingled_doc.similarity(shingled_diff_doc))

