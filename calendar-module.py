def input():
    return "08 05 2015"


def main():
    import calendar
    m, d, y = map(int, input().split())
    print(calendar.day_name[calendar.weekday(y, m, d)].upper())


main()
