from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 0 ]
matrix = new_matrix(0,0)
add_edge(matrix,250,330,0,292,330,0)
add_edge(matrix,391,388,0,373,285,0)
add_edge(matrix,373,285,0,407,201,0)
add_edge(matrix,407,201,0,250,141,0)
add_edge(matrix,250,120,0,292,330,0)
add_edge(matrix,292,330,0,391,388,0)
add_edge(matrix,292,330,0,373,285,0)
add_edge(matrix,373,285,0,268,214,0)
add_edge(matrix,314,244,0,265,149,0)
add_edge(matrix,314,244,0,407,201,0)
add_edge(matrix,250,120,0,265,149,0)
for i in range(250,266):
    add_edge(matrix,250,120,0,i,int(60/157*(i-250)+141),0)
draw_lines( matrix, screen, color )
for point in matrix:
    point[0] = 500-point[0]
draw_lines( matrix, screen, color )

display(screen)
