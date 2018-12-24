import src.matrix_generator as matrix_generator
from src.exceptions import InvalidArgumentError
from src import parser
def handle_generate_matrix(params: dict) -> str:
    k, n = _assure_params(params,["k","n"])
    gen_matrix = matrix_generator.generate(int(k),int(n))
    return parser.list_to_matrix(gen_matrix)
    
def _assure_params(params: dict, names: list) -> ():
    values = []
    for key in names:
        param = params.get(key)
        if not param:
            raise InvalidArgumentError(f"Request did not have parameter ${key} in request body")
        values.append(param)
    return tuple(values)
    