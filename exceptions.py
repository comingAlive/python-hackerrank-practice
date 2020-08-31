def input():
    return 3


def main():
    for _ in range(int(input())):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except BaseException as err:
            print("Error Code:", err)


main()
