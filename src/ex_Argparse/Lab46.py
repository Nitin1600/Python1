import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", help="firstnumber")
parser.add_argument("num2", help="secondnumber")
parser.add_argument("operation", help="operation")

args = parser.parse_args()

print(args.num1)
print(args.num2)
print(args.operation)

n1 = int(args.num1)
n2 = int(args.num2)

if args.operation == "add":
    result = n1 + n2
    # print("The result is: ", result)

elif args.operation == "sub":
    result = n1 - n2
    # print("The result is: ", result)

elif args.operation == "mul":
    result = n1 * n2
    # print("The result is: ", result)

elif args.operation == "div":
    result = n1 / n2
    # print("The result is: ", result)

else:
    print("Unmatched argument")

print("The result is: ", result)