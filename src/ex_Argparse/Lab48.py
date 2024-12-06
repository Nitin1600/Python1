import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num", help="Enter the number to get square of it", type=int)
args = parser.parse_args()

print(args.num ** 2)

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("num", help="enter number to get square of it.", type=int)
# args=parser.parse_args()
# print(args.num ** 2)