#!/usr/bin/python3
def add_args(argv):
    ln = len(argv) - 1
    s = 0
    if ln == 0:
        print("{}".format(ln))
    else:
        for i in range(1, ln + 1):
            s += int(argv[i])
        print(s)


if __name__ == "__main__":
    import sys
    add_args(sys.argv)
