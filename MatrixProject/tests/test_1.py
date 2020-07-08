import unittest

from matrix_pkg_mello244688.MatrixDist import Matrix

class TestMMatrix(unittest.TestCase):
    def test_add_ints(self):

        m1 = [
            [7, 8, 9],
            [6, 3, 0],
            [6, 6, 6]
        ]

        m2 = [
            [0, 8, 7],
            [5, 2, 8],
            [3, 8, 2]
        ]

        matrix = Matrix(m1)
        matrix2 = Matrix(m2)

        r = [
            [7, 16, 16],
            [11, 5, 8],
            [9, 14, 8]
        ]

        result = Matrix(r)

        matrix.add_matrix(matrix2)

        self.assertEqual(matrix.matrix, result.matrix)

    def test_sub_ints(self):

        m1 = [
            [7, 8, 9],
            [6, 3, 0],
            [6, 6, 6]
        ]

        m2 = [
            [0, 8, 7],
            [5, 2, 8],
            [3, 8, 2]
        ]

        matrix = Matrix(m1)
        matrix2 = Matrix(m2)

        r = [
            [7, 0, 2],
            [1, 1, -8],
            [3, -2, 4]
        ]

        result = Matrix(r)

        matrix.sub_matrix(matrix2)

        self.assertEqual(matrix.matrix, result.matrix)

if __name__ == '__main__':
    unittest.main()

