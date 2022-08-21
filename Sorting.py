"""
Фунция для нахождения целой части после деления на 2
"""
def round_half_down(p, r):
    return ((p + r) // 2)


"""
Фунция для объединения двух массивов
"""
def merge(left_part, right_part):
    result = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    if i < len(left_part):
        result += left_part[i:]
    elif j < len(right_part):
        result += right_part[j:]
    return result


"""
Фунция для сортировки массивов с помощью рекурсии
"""
def sort(A, p, r):
    if len(A) < 2:
        return A
    else:
        q = round_half_down(p, r)
        left_part = sort(A[:q], 0, len(A))
        right_part = sort(A[q:], 0, len(A))
        return merge(left_part, right_part)


A = [5, 2, 4, 6, 1, 3, 2, 6]

result = sort(A, 0, len(A))  # p = 0, т.к. в питоне первый индекс = 0
print(result)
