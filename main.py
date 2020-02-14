from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = new_matrix(0,0)
add_edge(matrix,100,400,0,200,400,0)
add_edge(matrix,200,400,0,200,300,0)
add_edge(matrix,200,300,0,100,300,0)
add_edge(matrix,100,300,0,100,400,0)
draw_lines( matrix, screen, color )

m1 = new_matrix()
ident(m1)
m1[3] = [10,10,0,1]
print_matrix(m1)
print_matrix(matrix)
matrix_mult(m1,matrix)
draw_lines(matrix,screen,color)
print_matrix(matrix)

display(screen)
