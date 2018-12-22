import random
import copy

class Channel:
    def __init__(self, error_chance ,seed = None):
        self.random_gen = random.Random(seed)
        self.error_chance = error_chance

    def send(self, vector):
        errorLocations = []
        received_vector = copy.deepcopy(vector)
        for idx in range(len(received_vector)):
            if self._error_happend():
                errorLocations.append(idx)
                received_vector[idx] ^= 1
        return received_vector

    def _error_happend(self) -> bool:
        random_float = self.random_gen.random()
        return random_float < self.error_chance