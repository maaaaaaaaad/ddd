mod = 1000000007

def matrix_product(arr1, arr2):
    l = len(arr1)
    new_arr = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                new_arr[i][j] += arr1[i][k] * arr2[k][j]
            new_arr[i][j] %= mod
    return new_arr

def matrix_product2(arr, lst):
    l = len(arr)
    result = [0] * l
    for i in range(l):
        for j in range(l):
            result[i] += arr[i][j] * lst[-j-1]
            result[i] %= mod
    return result

def solution(n):
    A = [1, 3, 10, 23, 62, 170]

    if n <= 6:
        return A[n-1]

    arr = [[1, 2, 6, 1, 0, -1]]
    for i in range(5):
        lst = [0] * 6
        lst[i] = 1
        arr.append(lst)

    mat = [row[:] for row in arr]
    r_matrix = [[0] * 6 for _ in range(6)]
    for i in range(6):
        r_matrix[i][i] = 1

    cnt = n - 3
    while cnt > 0:
        if cnt % 2:
            r_matrix = matrix_product(r_matrix, mat)
        mat = matrix_product(mat, mat)
        cnt //= 2

    result = matrix_product2(r_matrix, A)
    return result[3]