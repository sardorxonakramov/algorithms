from random import randrange


def QuickSort(data: list, reverse=False):
    """Malumotlarni tartiblab beruvchi funkisya
    data: List bering\nreverse: True teskari tartibda chiqarish uchun"""

    if len(data) < 2:
        return data

    else:
        pivot = data[randrange(len(data))]
        kichik = [i for i in data if i < pivot]
        katta = [i for i in data if i > pivot]
        pivot = [i for i in data if pivot == i]

        sorted_data = QuickSort(kichik) + pivot + QuickSort(katta)

        return sorted_data[::-1] if reverse else sorted_data


print(QuickSort([44, 3, 12, 43, 53, 41, 23, 1321, 5, 1, 5, 6, 1, 5, 1, 3, 2, 4],True))
print(QuickSort(["SAlom", "bolta", "Kampir", "Alik", "anor", "olma", "nok"],True))


# pivot - boshlanishi
