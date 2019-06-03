import numpy as np
import random


class RandomVariable:

    def __init__(self, dict):
        self.dict = dict

    def sample(self):
        '''
        Returns a random variable e.g 3, 2, etc
        '''
        keys = list(self.dict.keys())
        values = list(self.dict.values())
        return np.random.choice(keys, 1, p=values)

    def sample_no_np(self):
        total = 0
        random_val = random.random()
        for k, v in self.dict.items():
            total += v
            if random_val <= total:
                return k

    def all_outcomes(self):
        print(self.dict.values())
        return set(self.dict)

    def pmf(self, t):
        t = str(t)
        return self.dict.get(t)
