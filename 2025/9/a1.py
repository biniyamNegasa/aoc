def get_input():
    matrix = []
    while True:
        try:
            col, row = map(int, input().strip().split(","))
            matrix.append([row, col])
        except EOFError:
            break
    return matrix


matrix = get_input()
n = len(matrix)
mx_area = 0
for i in range(n):
    row1, col1 = matrix[i]
    for j in range(i + 1, n):
        row2, col2 = matrix[j]
        height = abs(row1 - row2) + 1
        width = abs(col1 - col2) + 1
        mx_area = max(mx_area, height * width)
print(mx_area)
