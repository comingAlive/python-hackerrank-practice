def input():
    return "08 05 2015"


def main():
    from collections import namedtuple
    n, Student = int(input()), namedtuple('Student', input())
    print("{:.2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))


main()
