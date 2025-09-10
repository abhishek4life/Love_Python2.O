A = [[1,2,3], [4,5,6]]
B = [[1,7], [2,6], [3,5]]

result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)

A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 7, 9], [2, 6, 8]]  # B should have the same dimensions as A

result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

for row in result:
    print(row)

A = [1, 2, 3]
B = [4, 5, 6]

dot_product = sum(A[i] * B[i] for i in range(len(A)))

print(dot_product)
