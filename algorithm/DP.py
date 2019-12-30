def rec_opt(array, i):
    if i == 0:
        return array[i]
    elif i == 1:
        return max(array[0], array[1])
    else:
        A = rec_opt(array, i - 2) + array[i]
        B = rec_opt(array, i - 1)
        return max(A, B)


if __name__ == '__main__':
    array = [1, 2, 4, 1, 7, 8, 3]
    print(rec_opt(array, len(array) - 1))
