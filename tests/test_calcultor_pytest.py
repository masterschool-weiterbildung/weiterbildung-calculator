from my_package.calculator import calculate

class TestCalculator:


    def setup_method(self, method):
        print(f"Setting up {method}")

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_addition(self):
        assert calculate("2+2") == 4

    def test_addition1(self):
        assert calculate("4+4") == 8

    def test_subtraction(self):
        assert calculate("4-1") == 3

    def test_subtraction1(self):
        assert calculate("5-2") == 3

    def test_multiplication(self):
        assert calculate("1*1") == 1

    def test_multiplication1(self):
        assert calculate("3*3") == 9

    def test_division(self):
        assert calculate("9/3") == 3.0

    def test_division1(self):
        assert calculate("8/2") == 4.0

    def test_division_remainder(self):
        assert calculate("6~3") == (2, 0)

    def test_division_remainder1(self):
        assert calculate("7~3") == (2, 1)
