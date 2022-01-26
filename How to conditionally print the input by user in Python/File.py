var = input()
print(f"Your answer: {var}") if var else print('')

# This is an inline if statement, that prints a newline if the input's returned value is False: ''.

def ask(question, *options):
    print(question)
    for index, option in enumerate(options):
        if option:
            print(f"{index} {option}")
    answer = input()
    print(f"Your answer: {answer}") if var else print('')