def BubleSort(data: list, reverse=False):
    """Pufakchali tartiblash algoritmi tezilig Big O bo'yicha n²-n-1 tezlikda ishaydi taxminiy qilib n²"""

    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            print(data)
        print()
    return data[::-1] if reverse else data


print(
    BubleSort([44, 33, 12, 43, 53, 41, 23, 1321, 5, 1, 5, 6, 11, 5, 111, 3, 2, 4], True)
)
