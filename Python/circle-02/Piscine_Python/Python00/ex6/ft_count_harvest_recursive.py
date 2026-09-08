def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def count(day):
        if day > n:
            print("Harvest time!")
            return
        print("Day", day)
        count(day + 1)

    count(1)
