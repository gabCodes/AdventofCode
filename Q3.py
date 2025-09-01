import re

#Parses text file into a string
def fileParser(filename: str) -> str:
    with open(filename, 'r') as file:
        content = file.read()
        content.replace("\n", "")
    return content


if __name__ == "__main__":

    #Load content
    content = fileParser("AoC-3.txt")

    #Pattern to check for
    pattern = r"mul\(([0-9]+),([0-9]+)\)"

    matches = re.findall(pattern, content)
    total = 0

    #Sum of multiplications
    for group in matches:
        total += int(group[0]) * int(group[1])

    print(total)
