def Sort(data: list, reverse=False):
    result = []
    length = len(data)
    if length:
        for i in range(length):
            index = 0
            minimum = data[0]
            for j in range(len(data)):
                if minimum > data[j]:
                    minimum = data[j]
                    index = j
            result.append(data.pop(index))
        return result[::-1] if reverse else result
    else:
        return "Siz bo'sh ro'yxat berdingiz "


data = [5, 1, 5, 3, 5, 2, 4, 1, 5]

print(Sort(data, True))


def selection_sort(data: list, reverse=False):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if (data[j] < data[min_index] and not reverse) or (
                data[j] > data[min_index] and reverse
            ):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data


data = [5, 3, 6, 1, 4]
print(selection_sort(data.copy()))  # [1, 3, 4, 5, 6]
print(selection_sort(data, True))  # [6, 5, 4, 3, 1]
print(data)


def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        target_index = i
        for j in range(i + 1, n):
            if reverse:
                if arr[j] > arr[target_index]:
                    target_index = j
            else:
                if arr[j] < arr[target_index]:
                    target_index = j
        arr[i], arr[target_index] = arr[target_index], arr[i]
    return arr
