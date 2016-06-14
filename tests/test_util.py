import unittest

from shingles.util import *

class UtilTestCase(unittest.TestCase):
    def test_generate_random_seeds(self):
        seeds = generate_random_seeds(20, 8)
        same_seeds = generate_random_seeds(20, 8)
        diff_seeds = generate_random_seeds(20)

        self.assertEqual(20, len(seeds))
        self.assertEqual(seeds, same_seeds)
        self.assertNotEqual(seeds, diff_seeds)

    def test_jaccard_similarity(self):
        set_a = set([1, 2, 3, 4, 5, 6])
        set_b = set([4, 5, 6, 7, 8, 9])

        self.assertEqual(3/9, jaccard_similarity(set_a, set_b))
