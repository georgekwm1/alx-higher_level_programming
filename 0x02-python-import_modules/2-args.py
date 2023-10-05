#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv)
    if arg_length - 1 > 1:
        print("{} arguments:".format(arg_length - 1))
        for position in range(1, arg_length):
            print("{}: {}".format(position, str(sys.argv[position])))
    elif arg_length - 1 == 1:
        print("{} argument:".format(arg_length - 1))
        for position in range(1, arg_length):
            print("{}: {}".format(position, str(sys.argv[position])))
    else:
        print("{} arguments.".format(arg_length - 1))
