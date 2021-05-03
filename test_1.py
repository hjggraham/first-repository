import alfa as hg
import numpy as np


def test_symplectic():
    my_array=np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['is_symplectic']
    
def test_square():
    my_array=np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['is_square']

def test_dim():
    my_array=np.array([[1, 0], [2, 1]])
    assert hg.check_symplecticity(my_array)['dim_a']==2
    
def test_notsymplectic():
    my_array=np.array([[0]])
    assert not hg.check_symplecticity(my_array)['is_symplectic']


