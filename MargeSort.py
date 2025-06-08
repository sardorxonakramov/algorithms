# Merge sortni qayta ishlash kerak sababi yaxshi tushunmadim va bu usitda ko'p amallarni ishlay olmadim


def marge(data):
    length = len(data)
    if length < 2:
        return data
    else:

        x, y = marge(data[: length // 2]), marge(data[length // 2 :])
        if x[0] > y[0]:
            return x + y
        else:
            return y + x


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


data = [44, 33, 12, 43, 53, 41, 23, 1321, 5, 1, 5, 6, 11, 5, 111, 3, 2, 4]
print(data)
mergeSort(data)
print(data)
