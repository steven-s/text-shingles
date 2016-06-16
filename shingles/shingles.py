import mmh3
from nltk import ngrams
from shingles.util import generate_random_seeds, jaccard_similarity

class ShingledDocument(object):
    def __init__(self, document_text, random_seed=5, shingle_length=5, minhash_size=200):
        self.shingles = ngrams(document_text.split(), shingle_length)
        self.minhash = []

        for hash_seed in generate_random_seeds(minhash_size, random_seed):
            hash_values = [mmh3.hash(shingle, hash_seed) for shingle in self.shingles]
            self.minhash.append(min(hash_values))

    def similarity(other_shingled_doc):
        return jaccard_similarity(set(self.minhash), set(other_shingled_doc.minhash))

