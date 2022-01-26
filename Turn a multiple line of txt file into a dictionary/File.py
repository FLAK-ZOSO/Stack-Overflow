with open('file.txt', 'r') as file:
    lines = file.read().split('\n') # lines is a list of the lines of the file
dictionary: dict = {}
for index, line in enumerate(lines):
    line = line.split(' ')
    dictionary[str(index)] = {
        "white": line[0],
        "black": line[1],
        "white score": line[2],
        "black score": line[4]
    }
