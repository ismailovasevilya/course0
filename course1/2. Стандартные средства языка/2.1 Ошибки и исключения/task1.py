try:
    foo()
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
except ZeroDivisionError:
    print("ZeroDivisionError")