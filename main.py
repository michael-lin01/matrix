from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = new_matrix()
add_edge(matrix,200,300,0,300,300,0)
add_edge(matrix,300,300,0,300,200,0)
add_edge(matrix,300,200,0,200,200,0)
add_edge(matrix,200,200,0,200,300,0)

draw_lines( matrix, screen, color )
display(screen)
