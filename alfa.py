def check_simplecticity(matrix, precision = 10 ** -12):
    '''This is to check wether a matrix is simplectic'''
    my_dict = {}
    #imput has to be in np.array()
    #to determine wether it is a square matrix
    my_dict['dim_a'], my_dict['dim_b'] = np.shape(matrix)
    if my_dict['dim_a'] == my_dict['dim_b']:
        my_dict['is_square'] = True
    else:
        my_dict['is_square'] = False
    #creating omega matrix
    identity_n = int(my_dict['dim_a']/2)
    identity_m = np.identity(identity_n)
    zeros = np.zeros((identity_n, identity_n))
    my_dict['omega'] = np.block([[zeros, identity_m], 
                                [-identity_m, zeros]])
    #final check for symplectic matrix
    l_side = matrix.T @ my_dict['omega'] @ matrix
    if (l_side - my_dict['omega'] < precision).all():
        my_dict['is_simplectic'] = True
    else:
        my_dict['is_simplectic'] = False
    return my_dict