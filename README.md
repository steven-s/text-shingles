# Document Shingles Library

This is python 3 library to support measuring the similarity of documents based on their [MinHash](https://en.wikipedia.org/wiki/MinHash) signature generated from their k-shingle form.

## API

Documents can be represented in MinHash form by creating a new `ShingledDocument` instance and passing in values for the `random_seed` for hashing (default 5), the `shingle_length` aka the k in k-shingles (default 5), and the `minhash_size` for the size of the MinHash signature (default 200). Variables for the list form of the `minhash` and iterator reprsentation of `shingles` are available for the object. A `similarity` function is also available to compute the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) of the two MinHash objects.
