import pytest

from my_package.calculator import addition_numbers, calculate


def test_addition():
	assert calculate("2+2") == 4
def test_addition1():
	assert calculate("4+4") ==  8
def test_subtraction():
	assert calculate("4-1") == 3
def test_subtraction1():
	assert  calculate("5-2") == 3
def test_multiplication():
	assert calculate("1*1") == 1
def test_multiplication1():
	assert calculate("3*3") == 9
def test_division():
	assert calculate("9/3") == 3.0
def test_division1():
	assert calculate("8/2") == 4.0
def test_division_remainder():
	assert calculate("6~3") == (2,0)
def test_division_remainder1():
	assert calculate("7~3") == (2,1)

