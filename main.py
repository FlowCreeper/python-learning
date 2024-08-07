from board import Board

b = Board()

b.print_board()

b.insert_element("E",1)
b.insert_element("X",1,3)
b.insert_element("O")
b.insert_element("P",column_position=1)

b.print_board()