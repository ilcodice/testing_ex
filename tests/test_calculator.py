import unittest
from typing import NoReturn

from src.calculator import Calculator
from src.custom_ex import IncorrectInputError, ZeroDivisionError,ValueError
import operator
import math


class CalculatorAddTestCase(unittest.TestCase):  # Test Case

    def test_add_3_corrrect_input(self) -> None | NoReturn:  # Unit
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = calculator.add(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:
        # Arrange
        calculator = Calculator()
        expected_result = 0

        # Act
        result = calculator.add()

        # Assert
        self.assertEqual(result, expected_result)

    def test_add_with_incorrect_input(self) -> NoReturn:
        # Arrange
        calculator = Calculator()
        x = "6"
        y = [4, 5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x, y)


class CalculatorMultTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(x, y, z)

        # Assert
        self.assertEqual(result, expected_result)

    def test_mult_with_incorrect_input(self):
        # Arrange
        x = []
        y = (1, 2)
        z = "4"

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x, y, z)

    def tearDown(self):
        pass

class CalculateDivisionTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_divi_with_correst_input(self):
        #calculator =Calculator()

        #Arrange
        x = 4
        y = 2
        expected_result = 2

        #Act
        result = self.calculator.division(x,y)

        #Assert
        self.assertEqual(result,expected_result)

    def test_devid_by_zero(self):
        x = 4
        y = 0

        #Act / Assert 
        with self.assertRaises(ZeroDivisionError):
            self.calculator.division(x, y)

    def tearDown(self):
        pass

class CalculationSubtractionTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sub_with_correct_input(self):
        #calculator = Calculator()

        #Arrange
        x = 6
        y = 3
        expected_result =3

        #Act
        result = operator.sub(x,y)

        #Assert
        self.assertEqual(result,expected_result)

    def tearDown(self):
        pass

class CalculatePercentageTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_per_with_correct_input(self):
        

        #Arrange
        x = 80
        y = 20
        expected_result = 16

        #Act
        result = self.calculator.percentage(x,y)
        
        #Assert
        self.assertEqual(result,expected_result)

    def tearDown(self):
        pass

class CalculateSqrtTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator =Calculator()

    def test_sqrt_with_correct_input(self):

        #Arrange
        x =25
        expected_result = 5

        #Act
        result = math.sqrt(x)

        #Assert
        self.assertEqual(result,expected_result)

    def tearDown(self):
        pass

class CalculateLogTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator =Calculator()

    def test_Log_with_correct_input(self):

        #Arrange
        x =25
        expected_result = 3.2188758248682006

        #Act
        result = math.log(x)

        #Assert
        self.assertEqual(result,expected_result)

    def test_log_0_Error(self):
        #Arrange
        x = 0
        #Act/Assert
        with self.assertRaises(ValueError):
            math.log(x) 

    def tearDown(self):
        pass
