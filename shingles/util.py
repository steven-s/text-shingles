import random


def generate_random_seeds(n, seed=5):
    random.seed(seed)
    return random.sample(range(1, n + 1), n)


def minhash_similarity(minhash_a, minhash_b):
    match_count = 0
    for a_item, b_item in zip(minhash_a, minhash_b):
        if a_item == b_item:
            match_count += 1
    return match_count / len(minhash_a)
