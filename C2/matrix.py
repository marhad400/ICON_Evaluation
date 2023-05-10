import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))
    
    def largest_index(self, matrix):
        ''' Make this function return a tuple of the (row, col) 
            index of the largest value in the matrix '''
        largest = self._matrix[0][0]
        for i in range(self._matrix.shape[0]):
            for j in range(self._matrix.shape[1]):
                if largest < self._matrix[i][j]:
                    largest = self._matrix[i][j]
                    row_largest = i
                    col_largest = j

        return (row_largest,col_largest)
    

    def convolve(self, kernel, matrix):
        ''' Make this function return the result of a 2D convolution '''
        padded_matrix = np.pad(matrix, pad_width=1, mode='constant', constant_values=0)
        # output_dimension = (input_dim + 2*padding - kernel_dim) / (stride) + 1
        output_height = (10 + 2 - 3) // 1 + 1
        output_width = (10 + 2 - 3) // 1 + 1
        # turns out to be dimensions of original matrix when padded with 1 layer of zeros

        output_matrix = np.zeros_like(matrix)

        for row in range(1, output_height):
            for col in range(1, output_width):
                submatrix = padded_matrix[row-1:row+2, col-1:col+2]
                output_matrix[row][col] = np.sum(np.multiply(submatrix, kernel))

        return output_matrix

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run() 