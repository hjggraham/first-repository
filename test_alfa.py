import alfa as hg
import numpy as np
import pytest
precision = 10 ** -12


def test_symplectic():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['is_symplectic']


def test_square():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['is_square']


def test_dima():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_a'] == 2


def test_even():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_a'] % 2 == 0


def test_positive():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_a'] > 0


def test_dimb():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_b'] == 2


def test_notsymplectic():
    my_array = np.array([[0]])
    assert not hg.check_symplecticity(my_array)['is_symplectic']


def test_omega():
    my_array = np.array([[1, 0], [2, 1]])
    assert ((hg.check_symplecticity(my_array)['omega'] - np.array([[0, 1], [-1, 0]])) < precision).all()


def test_square2():
    my_array = np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_a'], hg.check_symplecticity(my_array)['dim_b'] == np.shape(my_array)
