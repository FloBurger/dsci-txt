def solve_puzzle (clues):
    plist = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    top = clues[0:4]
    right = clues[4:8]
    bot = clues[8:12]
    bot = bot[::-1]
    left = clues[12:16]
    left = left[::-1]
    for row in range(len(plist)):
        for column in range(len(plist[row])):
            print("row:",row, " column:", column)
            if row == 0:
                if top[column] == 1:
                    print("top")
                    plist[row][column] = 4
            if column == 3:
                if right[row] == 1:
                    #print("right", row, column)
                    plist[row][column] = 4
            if row == 3:
                if bot[column] == 1:
                    print("bot", row, column)
                    plist[row][column] = 4
            if column == 0:
                if left[row] == 1:
                    print("left" ,row, column)
                    plist[row][column] = 4
                
            #print(plist[row][column])
            
    return plist
            
    


clues =( 2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3 )

print(solve_puzzle(clues))