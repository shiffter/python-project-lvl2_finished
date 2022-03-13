import argparse
import os
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff', epilog='Created by shiffter')
    parser.add_argument('file_1', type=str)
    parser.add_argument('file_2', type=str)
    parser.add_argument('-f', '--format', default=None, help='set format of output', type=str)
    args = parser.parse_args()
    path_1 = os.path.abspath(args.file_1)
    path_2 = os.path.abspath(args.file_2)
    generate_diff(path_1, path_2, mode=args.format)


def f(x):
    return x

if __name__ == '__main__':
    main()
