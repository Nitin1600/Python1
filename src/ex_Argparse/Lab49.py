import argparse

parser = argparse.ArgumentParser()

parser.add_argument("example")
args = parser.parse_args()
if args.example == "Hello_Python":
    print("Welcome to LearnMore")
else:
    print("Didn't make it")

# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("example", default="Hello, how are you")
# args = parser.parse_args()
#
# if args.example == "Hello":
#     print("Welcome")
# else:
#     print("Didn't make it")
