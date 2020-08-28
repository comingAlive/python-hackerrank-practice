def input():
    return "HACK 2"


def main():
    from itertools import permutations

    s, n = input().split()
    for i in permutations(sorted(s), int(n)):
        print(''.join(i))


main()
