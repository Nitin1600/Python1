# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-tut", "--tutorial", help="Best thing")
# parser.add_argument("-w", "--writer", help="Technical Content")
#
# args = parser.parse_args()
# if args.tutorial == "LMore":
#     print("Congratulations!, You made it!")
#
# if args.writer == "Devansh":
#     print("Technical Content!")

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("tutorial", default="Best_thing")
parser.add_argument("-w", "--writer", default="Technical_Writer")

args = parser.parse_args()
if args.tutorial == "tutorial":
    print("Congratulations!, You made it!")
if args.writer == "Devansh":
    print("Technical Content")
