string: str = list(input())

for index, element in enumerate(string):
    if (index == 0):
        continue
    # Where index is the index of an _ in the string
    if (element == '_'):
        # The _ is between two not-european characters
        if (ord(string[index+1]) > 500 and ord(string[index-1]) > 500):
            string[index] = ''

string = ''.join(string)
