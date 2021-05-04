import alfa as hg
import numpy as np


def test_method1():
    my_array=np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['is_symplectic']
    assert hg.check_symplecticity(my_array)['is_square']
    assert hg.check_symplecticity(my_array)['dim_a']==3
    
def test_method2():
    my_array=np.array([[0]])
    assert not hg.check_symplecticity(my_array)['is_symplectic']


