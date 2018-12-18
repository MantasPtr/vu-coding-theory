class InvalidArgumentError(ValueError):
    def __init__(self, message, expression = None):
        self.expression = expression            
        self.message = message     

class InvalidStateError(ValueError):
    def __init__(self, message, expression = None):
        self.expression = expression            
        self.message = message       