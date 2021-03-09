def getInvCount(arr) :

    inv_count = 0
    for i in range(0, 2) :
        for j in range(i + 1, 3) :

            # Value 0 is used for empty space
            if (arr[j][i] > 0 and arr[j][i] > arr[i][j]) :
                inv_count += 1
    return inv_count

# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle) :

    # Count inversions in given 8 puzzle
    invCount = getInvCount(puzzle)

    # return true if inversion count is even.
    return (invCount % 2 == 0)

    # Driver code
puzzle = [[2, 8, 1],[3, 4, 6],[7, 5, 0]]
if(isSolvable(puzzle)) :
    print("Solvable")
else :
    print("Not Solvable")