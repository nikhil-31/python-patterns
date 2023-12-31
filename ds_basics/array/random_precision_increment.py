
a = [9, 9, 9]

res = ''.join(map(str, a))
res = int(res) + 1
res = [int(i) for i in str(res)]
print(res)


def plus_one(A):
    A[-1] += 1

    for i in reversed(range(len(A))):
        if A[i] != 10:
            break
        
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 0
        A.append(0)

    return A

A1 = [1, 4, 9]
A2 = [9, 9, 9]

print(plus_one(A1))
print(plus_one(A2))