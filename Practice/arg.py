import sys

if __name__ == "__main__":
    args = sys.argv

    for i, arg in enumerate(args):
        print(f'{i}th arg is {arg}')