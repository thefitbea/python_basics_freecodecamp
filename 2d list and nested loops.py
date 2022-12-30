#2D list

num_grid=[2,3,4,5]#normal list

two_d_num_grid=[
  #c1 #c2 #c3
    [1,2,3],#row0
    [4,5,6],#row1
    [7,8,9],#row2
    [0]#row3
]

print(two_d_num_grid[1][0])#row index(horizontally) then column index(vertically)
print(two_d_num_grid[2][2])

print("\n")

#nested for loop

for row in two_d_num_grid:
    #print(row)
    for col in row:
        print(col)