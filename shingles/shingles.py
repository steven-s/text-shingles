from nltk import ngrams
from shingles.util import generate_hash_functions

class ShingledDocument(object):
    def __init__(self, document_text, shingle_length=5, hash_seed=5):
        self._shingles = ngrams(document_text.split(), shingle_length)
