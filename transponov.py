def transpose(arr):
    matrix = []
    if len(arr) == 0:
        return []
    if arr[0] == []:
        return [[]]
    for i in range(0, len(arr[0])):
        for j in range(0, len(arr)):
            if j == 0:
                matrix.append([])
            matrix[i].append(arr[j][i])
    return matrix
print(transpose([]))