"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    x = y = z = w = ""
    for point in matrix:
        x += str(point[0]) + " "
        y += str(point[1]) + " "
        z += str(point[2]) + " "
        w += str(point[3]) + " "
    print(f'%s\n%s\n%s\n%s' % (x,y,z,w))

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            matrix[r][c] = 1 if r == c else 0


#multiply m1 by m2, modifying m2 to be the product
# 4x4 by 4xn
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for point in m2:
        x = point[0]
        y = point[1]
        z = point[2]
        w = point[3]
        for c in range(4):
            point[c] = m1[0][c]*x + m1[1][c]*y + m1[2][c]*z + m1[3][c]*w



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

if __name__ == "__main__":
    m1 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
    m2 = [[1,2,3,1],[4,5,6,1]]
    # print_matrix(m1)
    # print_matrix(m2)
    matrix_mult(m1,m2)
    print_matrix(m2)
