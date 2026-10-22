n, k = map(int, input().split())
lst = list(map(int, input().split()))
deq = []
result = []
for i in range(n):
    if deq and deq[-1] > lst[i]:
        while deq and deq[-1] > lst[i]:
            deq.pop()
    deq.append(lst[i])
    if i > 0 and deq[0] == lst[i - 1]:
        deq.pop(0)
    if i < n - 1 and (i + 1) % k == 0:
        result.append(deq[0])
print(*result)
