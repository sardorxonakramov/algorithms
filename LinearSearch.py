# Oddiy Linear Search

# 1 masala
# Berilgan sonlar ro‘yxatida foydalanuvchi kiritgan qiymat mavjud bo‘lsa, uning indeksini chiqaring. Agar mavjud bo‘lmasa, -1 chiqaring.


def first_quiz(data: list, find: int) -> int:
    for i in data:
        if find == i:
            return data.index(i)
    return -1


# data = [3, 8, 12, 5, 9, 14, 7, 2]
# print(first_quiz(data=data, find=int(input(">>> "))))

# ------------------------------------------------------------------------------------------------------

# 2 masala
# Ro'yxatda kiritilgan qiymat nechta marta uchrashini aniqlang.


def second_quiz(data: list, find: int):
    count = 0
    for i in data:
        if i == find:
            count += 1
    return count


# data = [5, 1, 5, 3, 5, 2, 4, 1, 5]
# print(second_quiz(data, int(input(">>> "))))

# ------------------------------------------------------------------------------------------------------

# 3 masala
# Ro‘yxatdan eng kichik elementni toping. Faqat chiziqli qidiruv (ya’ni for-loop) bilan bajaring.


def third_quiz(data: list):
    minimum = data[0]
    for i in data:
        if i < minimum:
            minimum = i

    return minimum


# data = [23, 45, 12, 56, 9, 67, 31]
# print(third_quiz(data))

# ------------------------------------------------------------------------------------------------------

# 4 masala
# Ro‘yxatda birinchi uchragan manfiy sonni toping va chiqaring.


def fourth_quiz(data: list):
    for i in data:
        if i < 0:
            return i
    return None


# data = [10, 3, 0, -2, 5, -7, 8]
# print(fourth_quiz(data))

# ------------------------------------------------------------------------------------------------------

# 5 masala
# Ro'yxatdagi eng katta juft sonni aniqlang. Agar juft son yo'q bo‘lsa, None chiqaring.


def fiveth_quiz(data: list):
    # max = -(10**308)
    maximum = None
    for i in data:
        if i % 2 == 0:
            if maximum is None or i > maximum:
                maximum = i
    return maximum


data = [11, 13, 14, 18, 113, 221]
# # data = [1, 3, 5, 7]


def LinearSearch(data: list, target: int):
    for j, i in enumerate(data):
        if i == target:
            return j
    return None


print(LinearSearch(data,113))
