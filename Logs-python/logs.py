import logging
import os
import binascii
from datetime import datetime, timedelta

LOGGING_ENABLED = True
LOGGING_FILENAME= 'logs.log'

class Success:
    """
    Clase que representa un mensaje de éxito.
    """
    def __init__(self, returnFunc="", function="", duration=timedelta(), additional_info=None):
        if not isinstance(function, str):
            raise TypeError("La función debe ser una cadena")

        self.returnFunc = returnFunc
        self.function = function
        self.duration = duration
        self.additional_info = additional_info

    def to_dict(self):
        """
        Convierte el mensaje en un diccionario con formato JSON.
        """
        message_dict = {
            "success": True,
            "returnFunc": self.returnFunc,
            "meta": {
                "function": self.function,
                "code_id": binascii.b2a_hex(os.urandom(20)).decode()
            },
            "duration": self.duration.total_seconds(),
            "date": datetime.utcnow().isoformat()
        }
        
        if self.additional_info:
            message_dict["additional_info"] = self.additional_info
        
        return message_dict

class Failed:
    """
    Clase que representa un mensaje de error.
    """
    def __init__(self, error_type="", error_info="", function="", duration=timedelta(), additional_info=None):
        if not isinstance(function, str):
            raise TypeError("La función debe ser una cadena")

        self.error_type = error_type
        self.error_info = error_info
        self.function = function
        self.duration = duration
        self.additional_info = additional_info

    def to_dict(self):
        """
        Convierte el mensaje en un diccionario con formato JSON.
        """
        message_dict = {
            "success": False,
            "message": None,
            "error": {
                "type": self.error_type,
                "info": self.error_info
            },
            "meta": {
                "function": self.function,
                "code_id": binascii.b2a_hex(os.urandom(20)).decode()
            },
            "duration": self.duration.total_seconds(),
            "date": datetime.utcnow().isoformat()
        }
        
        if self.additional_info:
            message_dict["additional_info"] = self.additional_info
        
        return message_dict

logging.basicConfig(filename=LOGGING_FILENAME, level=logging.INFO)
logger = logging.getLogger(__name__)

def log_function():
    """
    Decorador para registrar información sobre la ejecución de una función en un archivo de registro.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                if LOGGING_ENABLED:
                    end_time = datetime.now()
                    duration = end_time - start_time
                    message = Success(returnFunc=result, function=func.__name__, duration=duration).to_dict()
                    logger.info(message)
                return result
            
            except Exception as e:
                if LOGGING_ENABLED:
                    end_time = datetime.now()
                    duration = end_time - start_time
                    message = Failed(error_type=type(e).__name__, error_info=str(e), function=func.__name__, duration=duration).to_dict()
                    logger.error(message)
                raise e
            
        return wrapper
    return decorator

@log_function()
def example_function(x, y):
    return x + y

@log_function()
def example_function2(x, y):
    return x / y
# force none
@log_function()
def example_function3(x, y):
    return None

@log_function()
def example_function4(x, y):
    return x * y

# force error
@log_function()
def example_function5(x, y):
    raise ValueError("Error grave")

#wait for 5 seconds
@log_function()
def example_function6(x, y):
    import time
    time.sleep(5)
    return x * y

if __name__ == '__main__':
    example = example_function(1, 2)
    print("example_function(1, 2) = ", example)
    example = example_function2(1, 2)
    print("example_function2(1, 2) = ", example)
    example = example_function3(1, 2)
    print("example_function3(1, 2) = ", example)
    example = example_function4(1, 2)
    print("example_function4(1, 2) = ", example)
    example = example_function5(1, 2)
    print("example_function5(1, 2) = ", example)
    example = example_function6(1, 2)
    print("example_function6(1, 2) = ", example)
