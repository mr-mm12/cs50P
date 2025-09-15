exp = input("Expression: ").strip().split(" ")

# unpack
num1, op, num2 = exp[0], exp[1], exp[2]

# convert strings to numbers
num1 = float(num1)
num2 = float(num2)

# do the operation
if op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
elif op == "-":
    print(num1 - num2)
elif op == "+":
    print(num1 + num2)
else:
    print("Usage: number_one symbol number_two")

# Mohammad_Reza_Mokhtari_Kia
