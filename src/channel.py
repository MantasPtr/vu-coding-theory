import random
import copy

class Channel:
    def __init__(self, error_chance, seed = None):
        self.random_gen = random.Random(seed)
        self.error_chance = error_chance

    def generate_errors(self, vector: [int]):
        errorLocations = []
        received_vector = copy.deepcopy(vector)
        for idx in range(len(received_vector)):
            if self._has_error_happend():
                errorLocations.append(idx)
        return [1 if index in errorLocations else 0 for index in range(len(vector))], len(errorLocations)

    def add_errors(self, vector: [int], error_vector: [int] ):
        return [vector_value^error_value for (vector_value, error_value) in zip(vector, error_vector)]

    def _has_error_happend(self) -> bool:
        random_float = self.random_gen.random()
        return random_float < self.error_chance