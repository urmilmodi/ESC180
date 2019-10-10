from ge import *

def printMatrix(matrix):
    for i in range (0, len(matrix), 1):
        v = ""
        for j in range (0, len(matrix[0]), 1):
            v += str(matrix[i][j]) + "\t"
        print(v)
    print("---------")

def main():
    printMatrix(ge_bw(ge_fw([[1,2,3],[4,5,6],[7,8,9]])))
    printMatrix(ge_bw(ge_fw([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])))
    printMatrix(ge_bw(ge_fw([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])))

main()