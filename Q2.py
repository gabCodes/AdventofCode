#Parse file into list of lists of integers
def fileParser(filename) -> list[list[int]]:
    with open(filename, 'r') as file:
        lines = file.readlines()
        list_of_lists = []

        for i in range(len(lines)):
            lines[i] = lines[i].strip().split()
            list_of_lists.append(list(map(int,lines[i])))

    return list_of_lists

#Check if changes monotonically and checks the difference between each adjacent number is >= 1 and <= 3
def rowChecker(row: list[int]) -> bool:
    assert len(row) > 1, "Row must have at least two elements to determine monotonicity"

    #Discard invalid case where two initial elements are equal
    if row[1] == row[0]:
        return False
    
    ascending = int(row[1] > row[0])

    for i in range(len(row) - 1):
        check = int(row[i+1] > row[i])
        diff = abs(int(row[i+1]) - int(row[i]))

        if diff >= 1 and diff <= 3 and check ^ ascending == 0:
            continue
        
        else:
            return False
        
    return True

#Count the number of valid rows
def validChecker(l1: list[list[str]]) -> int:
    count = 0
    for row in l1:
        if rowChecker(row):
            count += 1

    return count

if __name__ == "__main__":

    data = fileParser("AoC-2.txt")
    print(validChecker(data))
