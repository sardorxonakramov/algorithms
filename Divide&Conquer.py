def ekub(x, y):
    if y == 0:
        return x
    else:
        return ekub(y, x % y)


def yer(x, y):
    kv = ekub(x, y)
    soni = (x * y ) // (kv * kv)
    return f"{soni} - ta kvadrat \n{kv} - kvadrat hajimi"


# print(yer(50, 25))


def summa(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + summa(lst[1::])


# print(summa([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


def ekuk(x, y):
    return abs(x * y) // ekub(x, y)


print(yer(168,64))
