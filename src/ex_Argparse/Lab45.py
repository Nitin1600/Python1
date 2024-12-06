# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument("num1", help="primary")
# parser.add_argument("num2", help="secondary")
# parser.add_argument("operation", help="operation")
#
# args = parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", help="first_nmber")
parser.add_argument("num2", help="second_number")
parser.add_argument("operation", help="operation")

args = parser.parse_args()
print(args.num1)
print(args.num2)
print(args.operation)

n1 = int(args.num1)
n2 = int(args.num2)

result = n1 + n2
print("The result is: ", result)