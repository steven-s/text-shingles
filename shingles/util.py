import random

def generate_random_seeds(n, seed=5):
    return random.sample(xrange(1, n), seed)

