import argparse
import src.matrix_generator as matrix_generator
from src.exceptions import InvalidArgumentError
from src.byte_converter import validate_string
from src.channel import Channel
from src.encoder import encode_message
from src.decoder import Decoder

def run():
    k, n, msg, gen_matrix, error_chance = _read_args()
    
    
    print(f"gen_matrix {gen_matrix}")
    
    channel = Channel(error_chance)
    print(f"message: {msg}")
    encoded_msg = encode_message(msg, gen_matrix)   
    print(f"encoded message: {encoded_msg}")
    received = channel.send(encoded_msg)
    print(f"message received: {received}")
    decoder = Decoder(gen_matrix)
    decoded = decoder.decode(received, len(msg))
    print(f"message decoded: {decoded}")
    


def _read_args():
    args = _parse_args()
    k = args.k
    n = args.n
    msg = args.msg
    gen_matrix = args.m
    error_chance = args.e
    if (gen_matrix is None):
        gen_matrix = matrix_generator.generate(k,n)
    else:
        gen_matrix = eval(gen_matrix)
    
    _validate_msg(msg, k)
    msg = [int(letter) for letter in msg]
    if not (0 <=  error_chance <= 1):
        raise InvalidArgumentError(f"invalid error chance")
    
    return k, n, msg, gen_matrix, error_chance

def _parse_args():
    parser = argparse.ArgumentParser(description='Encodes vector or a file using a binary matrix then decodes using step by step decoding')
    parser.add_argument('k', metavar="k", type=int, help='Code dimension')
    parser.add_argument('n', metavar="n", type=int, help='Code length')
    parser.add_argument('msg', metavar="msg", type=str, help='message to send')
    parser.add_argument('--m', metavar="matrix", type=str, default=None, help='Generator matrix')
    parser.add_argument('--e', metavar="error_chance",  type=float, default=0.1, help='error chance (0-1)')
    return parser.parse_args()

def _validate_msg(msg, k):
     if not validate_string(msg):
        raise InvalidArgumentError("Invalid character in message")
   
if __name__ == '__main__':
    run()

