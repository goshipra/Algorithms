lis1 = [1, 2, 3, 4, 5, 6, 7]
lis2 = [4, 5, 6, 7, 8, 8, 9]

res = []
i = 0
j = 0
while i < len(lis1) and j < len(lis2):
    if lis1[i] < lis2[j]:
        res.append(lis1[i])
        i += 1
    else:
        res.append(lis2[j])
        j += 1


res = res +lis1[i:]+ lis2[j:]


print(res)
