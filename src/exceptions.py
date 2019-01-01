class InvalidArgumentError(ValueError):
    def __init__(self, message, expression = None):
        self.expression = expression            
        self.message = message     

class InvalidStateError(ValueError):
    def __init__(self, message, expression = None):
        """exception for things that should never happen"""
        self.expression = expression            
        self.message = message       

class ValidationError(ValueError):
    def __init__(self, message, expression = None):
        """exception for bad values provided by the user"""
        self.expression = expression            
        self.message = message       
