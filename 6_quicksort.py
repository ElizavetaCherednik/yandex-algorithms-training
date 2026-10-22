import random

def partition(l, r, x):
    s = e = 0
    for i in range(n):
        if nums[i] == x:
            nums[e], nums[i] = nums[i], nums[e]
            e += 1
        elif nums[i] < x:
            temp = nums[i]
            nums[i] = nums[e]
            nums[e] = nums[s]
            nums[s] = temp
            s += 1
            e += 1
    return s, e

def quicksort(l, r):
    if r - l <= 1:
        return
    x = nums[random.randint(l, r - 1)]
    s, e = partition(l, r, x)
    quicksort(l, s)
    quicksort(e, r)

n = int(input())
nums = list(map(int, input().split()))
quicksort(0, n)
print(*nums)
