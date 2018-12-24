import src.matrix_generator as matrix_generator
from src.exceptions import InvalidArgumentError
from src import parser
from src.encoder import encode_message
from src.decoder import Decoder
from src.channel import Channel

def handle_generate_matrix(params: dict) -> str:
    k, n = _assure_params(params,["k", "n"])
    gen_matrix = matrix_generator.generate(int(k), int(n))
    return parser.list_to_matrix(gen_matrix)

def handle_encode(params: dict) -> ():
    vector_str, gen_matrix_str, error_chance_str = _assure_params(params, ["vector","gen_matrix","error_chance"])
    vector = parser.vector_to_list(vector_str)
    gen_matrix = parser.matrix_to_list(gen_matrix_str)
    encoded = encode_message(vector, gen_matrix)
    
    error_chance = float(error_chance_str)
    channel = Channel(error_chance)
    error_vector, error_count = channel.generate_errors(encoded)

    encoded_str = parser.list_to_vector(encoded)
    error_vector_str = parser.list_to_vector(error_vector)
   
    return encoded_str, error_vector_str, error_count

def handle_send(params: dict) -> ():
    gen_matrix_str, encoded_vector_str, error_vector_str, message_len_str = _assure_params(params, ["gen_matrix", "encoded_vector", "error_vector", "message_len"])
    gen_matrix = parser.matrix_to_list(gen_matrix_str)
    encoded = parser.vector_to_list(encoded_vector_str)
    error_vector = parser.vector_to_list(error_vector_str)
    message_len = int(message_len_str)
    channel = Channel()
    received = channel.add_errors(encoded, error_vector)
    print(received)
    decoder = Decoder(gen_matrix)
    print(message_len)
    decoded = decoder.decode(received, message_len)

    received_str = parser.list_to_vector(received)
    decoded_str = parser.list_to_vector(decoded)
    return received_str, decoded_str

def _assure_params(params: dict, names: list) -> ():
    values = []
    for key in names:
        param = params.get(key)
        if not param:
            raise InvalidArgumentError(f"Request did not have parameter {key} in request body")
        values.append(param)
    return tuple(values)
    