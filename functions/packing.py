def sum(num1, num2):
    return num1 + num2


def sum_n(*numbers):
    sum = 0
    for num in numbers:
        sum += num

    return sum


if __name__ == "__main__":
    print(sum_n(1, 2, 3, 4, 5))

    theTuple = (1, 2, 3, 4, 5, 6)

    print(sum_n(*theTuple))

    theList = [1, 2, 3, 4, 5, 6]

    print(sum_n(*theList))
