from src.exceptions import InvalidArgumentError

def split(message: [int], length: int) -> [[int]]:
    """Splits message into provided length vectors"""
    if (length < 1):
        raise InvalidArgumentError("cannot split vector into arrays of length less than 1")
    # from 0 to length of message, step size - length should be code dimension
    for position in range(0, len(message), length):
        splitted = message[position:position + length]
        yield splitted
        
def append_0_if_short(vector: [int], length) -> [int]:
    """adds 0 if the vector length shorter than 'length'"""
    for _ in range(len(vector),length):
        vector.append(0)
    return vector