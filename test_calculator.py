from CalculatorFunctions import add_function, subtract_function, divide_function, multiply_function 
def test_add():
    assert add_function(1,2) == 3
    assert add_function(4,6) == 10
    assert add_function(0,1) == 1
    assert add_function(3,4) == 7
    assert add_function(9,3) == 12
def test_sub():
    assert subtract_function(2,1) == 1
    assert subtract_function(5,5) == 0
    assert subtract_function(2,5) == -3
    assert subtract_function(9,2) == 7
    assert subtract_function(8,4) == 4
def test_div():
    assert divide_function