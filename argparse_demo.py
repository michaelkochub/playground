# Messing around with argparse library and considering
# whether I should use it in my wmata script

import argparse as argp

def find_longest(s):
    arr = get_lengths(s)
    return arr.pop()[1]

def find_shortest(s):
    arr = get_lengths(s, True)
    return arr.pop()[1]

def get_lengths(strs, max_first=False):
    return sorted([(len(s), s) for s in strs], reverse=max_first)

def main():
    parser = argp.ArgumentParser(description='Process some strings.')

    parser.add_argument('strings', metavar='S', type=str, nargs='+', help='strings to process')
    parser.add_argument('-l', '--longest', dest='process', action='store_const',
        const=find_longest, default=find_shortest,
        help='find the longest string (default: find the shortest)')

    args = parser.parse_args()

    print(args.process(args.strings))

if __name__ == '__main__':
    main()
