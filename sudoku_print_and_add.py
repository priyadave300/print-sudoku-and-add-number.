##here in print_sudoku()we run first main for loop to transverse across each row and then another for loop 
##to transverse across each element of each row from range(0,9). Then we have if condn where we check whether 
##i !=0 and also whether i% 3==0 for row and if yes then print(). then for j !=0 and j%3 ==0 then print " " 
##and then use end and then print eleements and when j is at 8 print() for new line and then return sudoku
def print_sudoku(sudoku: list):
    for i in range(0,9):
        if i !=0 and i % 3 == 0:
            print()
        for j in range(0,9):
            if j !=0 and j % 3 == 0:
                print(" ", end ="")
            if sudoku[i][j]== 0:
                print("_", end =" ")
            if sudoku[i][j]!= 0:
                print(sudoku[i][j], end= " ")
        print()
    return sudoku

##here we ask user for row_no and col_no and the num then row[column_no] will be the new no and then 
##return sudoku
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    row = sudoku[row_no]
    row[column_no] = number
    return sudoku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)
