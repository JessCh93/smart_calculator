import art


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(calc_dict["*"](4,8))

print(art.logo)
first_num = int(input("Write the first number to calculate : "))
print(f"The number you have entered is {first_num}")
continue_calculating = True
while continue_calculating:

    oper_choice = input("Choose one of the following math operation : '+', '-' , '*' or '/' : ")
    print(f"The following operation {oper_choice} is chosen")
    last_num = int(input("Write down the second number to operate : "))
    print(f"The second number is {last_num}")

    result = calc_dict[oper_choice](first_num, last_num)
    print(f"The result of {first_num} {oper_choice} {last_num} is {result} ")

    ask_to_cont = input("Do you want to continue working with the previous result ? answer 'yes' or 'no'")
    if ask_to_cont == 'yes':
        first_num = result
        print(f"The calculation will continue from {result} as the first entry")
    else:
        continue_calculating = False
        print("Thank you for using smart calculation. Have a nice day :)")



