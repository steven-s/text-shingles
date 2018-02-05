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

    def test_minhash_similarity(self):
        minhash_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        minhash_b = [1, 2, 3, 7, 8, 9, 10, 11, 12]

        self.assertEqual(3/9, minhash_similarity(minhash_a, minhash_b))

