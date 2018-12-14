def validate_string(message: str):
    for symbol in message:
        if symbol != '0' and symbol != '1':
            return False
    return True