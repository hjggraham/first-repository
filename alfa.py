import numpy as np


def check_symplecticity(matrix, precision=10 ** -12):
    """This is to check wether a matrix is simplectic.
     
    Parameters
    ----------
    in_value
        A matrix that we want to check if it is simplectic.
    Returns
    -------
    bool
        True/False depending on whether it symplectic or not.
    Examples
    --------
    >>> matrix1 = np.array([[1, 0], [2, 1]])
    >>> check_symplecticity(matrix1)['is_symplectic']
    True

    >>> matrix2 = np.array([[3, 4], [2, 5]])
    >>> check_symplecticity(matrix2)['is_symplectic']
    False
    """


    my_dict = {}
    my_dict['is_square'] = False
    my_dict['is_symplectic'] = False

    try:
        my_dict['dim_a'], my_dict['dim_b'] = np.shape(matrix)
    except:
        raise Exception("Sorry, I need 2D arrays!")

    if my_dict['dim_a'] == my_dict['dim_b']:
        my_dict['is_square'] = True

        if (my_dict['dim_a'] % 2 == 0) & (my_dict['dim_a'] > 0):
            # Even
            # creating omega matrix
            identity_n = int(my_dict['dim_a']/2)
            identity_m = np.identity(identity_n)
            zeros = np.zeros((identity_n, identity_n))
            my_dict['omega'] = np.block([[zeros, identity_m],
                                        [-identity_m, zeros]])
            # final check for symplectic matrix
            l_side = matrix.T @ my_dict['omega'] @ matrix
            if ((l_side - my_dict['omega']) < precision).all():
                my_dict['is_symplectic'] = True

    return my_dict
