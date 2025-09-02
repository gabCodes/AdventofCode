import numpy as np

#Read file and convert to list of lists
def fileParser(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        list_of_lists = []

        for i in range(len(lines)):
            list_of_lists.append(list(lines[i].strip()))
    
    return list_of_lists

#Check in all 8 directions for XMAS
def dirChecker(arr, x: int, y: int, heading: str) -> int:
    #Define direction mapping
    m = {
    "S"     : [[x, y + 1], [x, y + 2], [x, y + 3]],
    "N"     : [[x, y - 1], [x, y - 2], [x, y - 3]],
    "E"     : [[x + 1, y], [x + 2, y], [x + 3, y]],
    "W"     : [[x - 1, y], [x - 2, y], [x - 3, y]],
    "SE"    : [[x + 1, y + 1], [x + 2, y + 2], [x + 3, y + 3]],
    "SW"    : [[x - 1, y + 1], [x - 2, y + 2], [x - 3, y + 3]],
    "NE"    : [[x + 1, y - 1], [x + 2, y - 2], [x + 3, y - 3]],
    "NW"    : [[x - 1, y - 1], [x - 2, y - 2], [x - 3, y - 3]]
    }

    #Retrieve positions to check
    pos = m[heading]
    check = ""
    for i, j in pos:
        check += arr[j][i]
    
    return int(check == "MAS")

#Check all X's in the array for possible XMAS
def xChecker(arr) -> int:
    v_dim = arr.shape[0]
    h_dim = arr.shape[1]
    count = 0
    for i in range(v_dim):
        for j in range(h_dim):
            if arr[i][j] == 'X':

                #Check vertical and down
                if i + 3 < v_dim:
                    count += dirChecker(arr, j, i, "S")

                #Check vertical and up
                if i - 3 >= 0:
                    count += dirChecker(arr, j, i, "N")

                #Check horizontal and right
                if j + 3 < h_dim:
                    count += dirChecker(arr, j, i, "E")

                #Check horizontal and left
                if j - 3 >= 0:
                    count += dirChecker(arr, j, i, "W")

                #Check diagonal south-east
                if i + 3 < v_dim and j + 3 < h_dim:
                    count += dirChecker(arr, j, i, "SE")
                
                #Check diagonal south-west
                if i + 3 < v_dim and j - 3 >= 0:
                    count += dirChecker(arr, j, i, "SW")
                
                #Check diagonal north-east
                if i - 3 >= 0 and j + 3 < h_dim:
                    count += dirChecker(arr, j, i, "NE")
                
                #Check diagonal north-west
                if i - 3 >= 0 and j - 3 >= 0:
                    count += dirChecker(arr, j, i, "NW")
        
    return count

if __name__ == "__main__":
    #Read file
    file = fileParser("AoC-4.txt")

    #Convert to numpy array
    file = np.array(file)

    print(xChecker(file)) 
