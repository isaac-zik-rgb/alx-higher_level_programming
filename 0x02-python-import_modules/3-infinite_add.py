#!/usr/bin/python3
if __name__ == "__main__":
    """print the result of all argument"""
    import sys
    result = 0
    if len(sys.argv) == 0:
        print("{}".firmat(len(sys.argv)))
    else:
        for i in range(1, len(sys.argv)):
            result += int(sys.argv[i])
        print("{}".format(result))
