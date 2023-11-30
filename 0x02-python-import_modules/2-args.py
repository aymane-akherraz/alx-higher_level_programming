#!/usr/bin/python3
def print_args():
    ln = len(sys.argv) - 1
    if ln == 1:
        print("1 argument:\n1: {}".format(sys.argv[ln]))
    else:
        if ln:
            print("{} arguments:".format(ln))
            for i in range(1, ln + 1):
                print("{}: {}".format(i, sys.argv[i]))
        else:
            print("0 arguments.")


if __name__ == "__main__":
    import sys
    print_args()
