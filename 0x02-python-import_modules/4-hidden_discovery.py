#!/usr/bin/python3
def print_names():
    for n in dir(h):
        if not n.startswith("__"):
            print(n)


if __name__ == "__main__":
    import hidden_4 as h
    print_names()
