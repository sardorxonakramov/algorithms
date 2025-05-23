def first_quiz(data: list, target: int):

    left = 0
    right = len(data) - 1
    qadam = 1
    while left <= right:
        mid = (left + right) // 2
        print(qadam)
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        qadam += 1

    return None


# data = [1, 3, 4, 6, 7, 8, 10, 12, 23, 45, 56, 78, 99]
# print(first_quiz(data, int(input(">>> "))))


def BinarySearch(data: list, target):

    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return None
