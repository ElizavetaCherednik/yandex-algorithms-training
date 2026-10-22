def lbinsearch(l, p, check, checkparams):
    while l < p:
        m = (l + p) // 2
        if check(m, checkparams):
            p = m
        else:
            l = m + 1
    return l

def checkisge(raznica, params):
    lst, n, r, c = params
    result = 0
    i = 0
    while i <= n - c:
        if lst[i + c - 1] - lst[i] <= raznica:
            result += 1
            i += c
        else:
             i += 1
        if result >= r:
            return True
    return False

n, r, c = map(int, input().split())
lst = []
for i in range(n):
    height = int(input())
    lst.append(height)
lst.sort()
raz = []
for i in range(n - c + 1):
    raz.append(lst[i + c - 1] - lst[i])
raz.sort()

print(lbinsearch(0, max(lst) - min(lst), checkisge, (lst, n, r, c)))
