def checkSimp(matrix):
    '''This is to check wether a matrix is simplectic'''
    my_dict = {}
    #test
    #imput has to be in np.array()
    #to determine wether it is a square matrix
    my_dict['dim_a'], my_dict['dim_b'] = np.shape(matrix)
    if my_dict['dim_a'] == my_dict['dim_b']:
        print('This is a square matrix')
    else:
        print('Not simplectic')
    #creating omega matrix
    identity_n = my_dict['dim_a']/2
    identity_m = np.identity(int(identity_n))
    zeros = np.zeros((int(identity_n), int(identity_n)))
    my_dict['omega'] = np.block([[zeros, identity_m], 
                                 [-identity_m, zeros]])
    #final check for symplectic matrix
    if (my_dict['omega'] == matrix.T@my_dict['omega']@matrix).all:
        my_dict['is_simplectic'] = True
    else:
        my_dict['is_simplectic'] = False
    return my_dict
