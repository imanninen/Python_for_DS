import sys
import os
from argparse import ArgumentParser


def print_pythin_version():
    print(sys.version)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-c", "--command")
    parser.add_argument("-p", "--path")
    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"Something goes wrong: {e}")
        exit(1)
    return args


def create_dir_by_path(dir_to_create):
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    else:
        print(f"Directory {dir_to_create} is already exists!")


def print_parent_dir():
    print(os.listdir("./.."))
