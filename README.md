# Text Shingles Library

This is python 3 library to support measuring the similarity of pieces of text based on their [MinHash](https://en.wikipedia.org/wiki/MinHash) signature generated from their k-shingle form.

## API

Text can be represented in MinHash form by creating a new `ShingledText` instance and passing in text as well as optional values for the `random_seed` for hashing (default 5), the `shingle_length` aka the k in k-shingles (default 5), and the `minhash_size` for the size of the MinHash signature (default 200). Variables for the list form of the `minhash` and iterator representation of `shingles` are available for the object. A `similarity` function is also available to compute the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) of the two MinHash objects.

## Requirements

This library utilizes Python 3, [NLTK](http://www.nltk.org), and [Murmur Hash](https://pypi.python.org/pypi/mmh3/2.3.1)
