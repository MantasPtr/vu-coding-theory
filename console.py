from src.channel import Channel
from src.encoder import encode_message
from src.decoder import Decoder
from src.console_arg_reader import parse_program_args
import readline
def run():
    k, n, msg, gen_matrix, error_chance = parse_program_args()
    print(f"gen_matrix:       {gen_matrix}")
    channel = Channel(error_chance)
    print(f"message:          {msg}")
    encoded_msg = encode_message(msg, gen_matrix)   
    print(f"encoded message:  {encoded_msg}")
    error_vector, error_count  = channel.generate_errors(encoded_msg)
    print(f"error count:      {error_count}")
    print(f"error vector:     {error_vector}")
    edited_error_vector = eval(read_input("edit mode:", str(error_vector)))
    print(f"edited_error vector: {edited_error_vector}")
    received = channel.add_errors(encoded_msg, edited_error_vector)
    print(f"message received: {received}")
    decoder = Decoder(gen_matrix)
    decoded = decoder.decode(received, len(msg))
    print(f"message decoded:  {decoded}")

def read_input(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)
   finally:
      readline.set_startup_hook()

if __name__ == '__main__':
    run()

