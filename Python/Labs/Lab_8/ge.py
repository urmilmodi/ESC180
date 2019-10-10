def ge_fw(matrix):
    
    # TODO for end cases
    v = len(matrix)
    if len(matrix) > len(matrix[0]):
        v = len(matrix[0])
        
    for k in range(0, v, 1):
        
        # Find 1st Row with non-zero and interchange to top
        for i in range (k, len(matrix), 1): # Go through all the rows
            if not matrix[i][k] == 0: # For the first non-zero col with
                x = list(matrix[k])
                matrix[k] = list(matrix[i])
                matrix[i] = list(x)
                break
        
        # Make all lower rows zero for the first col
        for i in range (k + 1, len(matrix), 1):
            if not matrix[i][k] == 0:
                x = matrix[i][k] / matrix[k][k]
                
                # Reduce the first col to 0
                for j in range (0, len(matrix[i]), 1):
                    matrix[i][j] -= x*matrix[k][j]

    # Remove -0s
    for i in range (0, len(matrix), 1):
        for j in range (0, len(matrix[i]), 1):
            if matrix[i][j] == -0:
                matrix[i][j] = 0.0
    
    return matrix

def ge_bw(matrix):
    
    v = len(matrix)
    if len(matrix) > len(matrix[0]):
        v = len(matrix[0])
    
    # Comment it throughly and do odd cases
    for k in range (v - 1, -1, -1):
        
        n = -1 # Remember the row
        for j in range (k, -1, -1): # For that row go through every col and find non-zero
             
            if not matrix[k][j] == 0:
                n = j
                x = matrix[k][j]
                
                for i in range (0, len(matrix[k]), 1):
                    matrix[k][i] = matrix[k][i] / x
                    
                break
            
        # IF there is a non-zero
        if not n == -1:
            
            # Go through all the rows for that col and check if they are nonzero if not make them
            for i in range (0, len(matrix), 1):
                
                if not i == k: # Don't Cancel the original row
                    
                    if not matrix[i][n] == 0:
                        
                        x = matrix[i][n]
                        
                        # Reduce the value in that col to 0
                        for j in range (0, len(matrix[i]), 1):
                            matrix[i][j] -= x*matrix[k][j]
                        
        test = False # Set False
        for i in range (0, len(matrix), 1):
            
            # See if any non-zero value, if there is make test True
            for j in range (k, len(matrix[i]), 1):
                if not matrix[i][j] == 0:
                    test = True
            
            # If test is False, entire row is 0
            if test == False:
                x = list(matrix[len(matrix) - 1])
                matrix[len(matrix) - 1] = list(matrix[i])
                matrix[i] = list(x)

    # Remove -0s
    for i in range (0, len(matrix), 1):
        for j in range (0, len(matrix[i]), 1):
            if matrix[i][j] == -0:
                matrix[i][j] = 0.0
    
    return matrix