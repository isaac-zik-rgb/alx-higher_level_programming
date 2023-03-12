#!/usr/bin/python3
if __name__ == "__main__":
    """ a prigarm that make operation on numbers"""
    from calculator_load_5 import add, sub, mul, div
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {'+':add, '-':sub, '*':mul, '/':div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
