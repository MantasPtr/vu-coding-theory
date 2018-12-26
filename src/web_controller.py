import src.matrix_generator as matrix_generator
from src.exceptions import InvalidArgumentError
from src import parser
from src.encoder import encode_message
from src.decoder import Decoder
from src.channel import Channel
from src import validator

def handle_generate_matrix(params: dict) -> str:
    k_str, n_str = _assure_params(params,["k", "n"])
    k, n = validator.validate_k_n(k_str,n_str)

    gen_matrix = matrix_generator.generate(k, n)
    
    return parser.list_to_matrix(gen_matrix)

def handle_encode(params: dict) -> ():
    vector_str, gen_matrix_str, error_chance_str = _assure_params(params, ["vector","gen_matrix","error_chance"])
    vector = validator.validate_vector(vector_str)
    gen_matrix = validator.validate_gen_matrix(gen_matrix_str)
    error_chance = validator.validate_error_chance(error_chance_str)
    
    encoded = encode_message(vector, gen_matrix)
    channel = Channel(error_chance)
    error_vector, error_count = channel.generate_errors(encoded)

    encoded_str = parser.list_to_vector(encoded)
    error_vector_str = parser.list_to_vector(error_vector)
   
    return encoded_str, error_vector_str, error_count

def handle_send(params: dict) -> ():
    gen_matrix_str, encoded_vector_str, error_vector_str, message_len_str = _assure_params(params, ["gen_matrix", "encoded_vector", "error_vector", "message_len"])
    gen_matrix = validator.validate_gen_matrix(gen_matrix_str)
    encoded = validator.validate_vector(encoded_vector_str)
    error_vector = validator.validate_error_vector(error_vector_str, encoded)
    message_len = int(message_len_str)
    channel = Channel()
    received = channel.add_errors(encoded, error_vector)
    decoder = Decoder(gen_matrix)
    decoded = decoder.decode(received, message_len)

    received_str = parser.list_to_vector(received)
    decoded_str = parser.list_to_vector(decoded)
    return received_str, decoded_str

def _assure_params(params: dict, names: list) -> ():
    values = []
    for key in names:
        param = params.get(key)
        if param is None:
            raise InvalidArgumentError(f"Request did not have parameter {key} in request body")
        values.append(param)
    return tuple(values)
    