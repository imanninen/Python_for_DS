import sys
import os
from argparse import ArgumentParser

# parser = ArgumentParser()
# parser.add_argument("-f", "--file")
# parser.add_argument("-q", "--quiet")
# args = parser.parse_args()

# first task
print(sys.version)
args = sys.argv
# second task
if len(args) > 1:
    dir_to_create = args[1]
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    else:
        print(f"Directory with name {dir_to_create} is already exists!")
# third task
if len(args) > 2:
    dir_to_watch = args[2]
    print(os.listdir(dir_to_watch))



