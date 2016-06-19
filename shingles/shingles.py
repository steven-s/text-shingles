import mmh3
from nltk import ngrams
from shingles.util import generate_random_seeds, jaccard_similarity

class ShingledDocument:
    def __init__(self, document_text, random_seed=5, shingle_length=5, minhash_size=200):
        split_text = document_text.split()
        if len(split_text) < shingle_length:
            raise ValueError(u'input document is too short for specified shingle length of {}'.format(shingle_length))

        self.minhash = []
        self.shingles = ngrams(split_text, shingle_length)

        for hash_seed in generate_random_seeds(minhash_size, random_seed):
            min_value = float('inf')
            for shingle in ngrams(split_text, shingle_length):
                value = mmh3.hash(' '.join(shingle), hash_seed)
                min_value = min(min_value, value)
            self.minhash.append(min_value)

    def similarity(self, other_shingled_doc):
        return jaccard_similarity(set(self.minhash), 
                set(other_shingled_doc.minhash))

