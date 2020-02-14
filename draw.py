from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for i in range(0,len(matrix),2):
        draw_line(matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],screen,color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])


def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

if __name__ == "__main__":
    #m1 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
    m1 = []
    add_point(m1,1,2,3)
    add_point(m1,4,5,6)
    add_edge(m1,7,8,9,10,11,12)
    #m2 = [[1,2,3,1],[4,5,6,1]]
    m2 = []
    add_edge(m2,1,2,3,4,5,6)
    print_matrix(m1)
    print_matrix(m2)
    matrix_mult(m1,m2)
    print_matrix(m2)
    ident(m1)
    matrix_mult(m1,m2)
    print_matrix(m2)
