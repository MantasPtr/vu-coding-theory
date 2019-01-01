import random
import copy

class Channel:
    def __init__(self, error_chance = None, seed = None):
        """
        error_chance - probability from 0 to 1 for error to occur
        seed - used for random generator, to allow repeating same random sequences. If not provided uses current time based seed.
        """
        self.random_gen = random.Random(seed)
        self.error_chance = error_chance

    def generate_errors(self, vector: [int]) -> ([int],int):
        """
        Generates error vector and error count
        """
        errorLocations = []
        received_vector = copy.deepcopy(vector)
        for idx in range(len(received_vector)):
            if self._has_error_happend():
                errorLocations.append(idx)
        return [1 if index in errorLocations else 0 for index in range(len(vector))], len(errorLocations)

    def add_errors(self, vector: [int], error_vector: [int] ):
        """
        Generates new vector which has errors added to 'vector' based on 'error_vector'.
        """
        return [vector_value^error_value for (vector_value, error_value) in zip(vector, error_vector)]

    def do_errors(self, vector: [int]):
        """
        Generates new vector with error in random positions based on probability
        """
        error_vector, _ = self.generate_errors(vector)
        vector_with_errors = self.add_errors(vector ,error_vector)
        return vector_with_errors

    def _has_error_happend(self) -> bool:
        """
        Boolean value if error has happened
        """
        random_float = self.random_gen.random()
        return random_float < self.error_chance