num = int(input())

for i in range(2, num):
        if (num%i == 0):
            print("The number is NOT prime")
            break
else:
    print("The number IS prime")
