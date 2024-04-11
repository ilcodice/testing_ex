from .custom_ex import IncorrectInputError
import operator
import math

class Calculator:
    def add(self, *args: float) -> float:  # type: ignore
        return sum(args)

    def multiply(self, *args: float):  # (1,2,3)
        try:
            result: float = 1
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")


    def division(self, *args: float):  # (1,2,3)
        try:
            result: float = args[0]
            for i in args[1:]:
                result /= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")
        
        
    def subtraction(self, *args: float):  # (1,2,3)
        return operator.sub(args)
    
    def percentage(self,x,y):
        x = (x*y)/100
        return x
    def sqrt(x):
        return math.sqrt(x)
    
    def log(self,x):
        return math.log(x)