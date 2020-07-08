import math

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        
    def add_matrix(self, other_matrix):
        """
        Adds matrix to current instance matrix

        Args: 
            other_matrix::[2D Float Array]

        Returns:
            none
        """
        
        if self._are_same_size(other_matrix.matrix):
            self.matrix = self._add_subtract(other_matrix.matrix, Matrix._add_numbers)
    
    def sub_matrix(self, other_matrix):
        """
        subtracts matrix from current instance matrix

        Args: 
            other_matrix::[2D Float Array]

        Returns:
            none
        """
        
        if self._are_same_size(other_matrix.matrix):
            self.matrix = self._add_subtract(other_matrix.matrix, Matrix._sub_numbers)
        
    def _are_same_size(self, m2):
        """
        Check that two matrices are the same structure and numeric
        
        Args:
            m1::[2D Array]
            m2::[2D Array]
        Returns:
            bool::True if the matrices are the same structure and numeric
            
        """
        m1 = self.matrix
        
        if len(m1) == 0 or len(m2) == 0:
            return False
        
        if len(m1) == len(m2):
            for x in range(len(m1)):
                if len(m1[x]) == len(m2[x]):
                    for y in range(len(m1[x])):
                        if math.isnan(float(m1[x][y])) or math.isnan(float(m2[x][y])): #one of the values is NaN
                            return False
                else: #row x does not have same number of columns between matrices
                    return False
        else: #do not have same number of rows
            return False
        
        return True
    
    def _add_subtract(self, m2, func):
        """
        will receive a function to either add or subtract two matrices

        Args:
            Matrix - m2, the matrix to add or subtract to self

        Reyurns:
            Array - The resulting matrix of the add/subtract
        """
        m1 = self.matrix
        result = []
        
        for x in range(len(m1)):            
            row = []            
            for y in range(len(m1[x])):
                row.append(func(m1[x][y], m2[x][y]))
            
            result.append(row)

        return result
                
    @staticmethod  
    def _add_numbers(x, y):
        """ returns x + y """
        return x + y
   
    @staticmethod
    def _sub_numbers(x, y):
        """ returns x - y """
        return x - y

    def __repr__(self):
        """Return string representing matrix"""

        msg = ""
        for arr in self.matrix:
            msg +="[" + " ".join(str(x) for x in arr) + "]\n"

        return msg