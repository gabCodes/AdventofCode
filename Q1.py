import numpy as np
def fileParser(filename) -> tuple[list[int], list[int]]:
    with open(filename, 'r') as file:
        #Load lines from file
        lines = file.readlines()
        list1 = []
        list2 = []

        #Add each number to respective list bucket
        for i in range(len(lines)):
            lines[i] = lines[i].split()
            list1.append(int(lines[i][0]))
            list2.append(int(lines[i][1]))
            
    return (list1, list2)


if __name__ == "__main__":

    #Parse text file into two lists
    l1, l2 = fileParser("AoC-1.txt")

    #Sort lists
    l1.sort()
    l2.sort()
    
    #Convert lists to numpy arrays for easier manipulation
    l1 = np.array(l1)
    l2 = np.array(l2)
    l3 = l1 - l2
    l3 = np.abs(l3)

    print(sum(l3))