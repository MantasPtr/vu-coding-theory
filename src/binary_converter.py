from src import parser

def text_to_bits(text: str) -> [int]:
    # 'Š'.encode('utf-8').decode('utf-8')
    binary_text = text.encode('utf-8')
    bit_str = ''.join(format(b,'08b') for b in binary_text)
    bit_vector = parser.vector_to_list(bit_str)
    return bit_vector

def bits_to_text(vector :[int]) -> str:
    vector_str = parser.list_to_vector(vector)
    # group by 8 bits into a byte
    vector_bytes_values = [int(vector_str[i:i+8],2) for i in range(0,len(vector_str),8)]
    return ''.join(chr(v) for v in vector_bytes_values)
