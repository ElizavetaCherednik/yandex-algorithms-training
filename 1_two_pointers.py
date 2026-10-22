def date(lst, r):
    last = 1
    c = 0
    for first in range(len(distance)):
        while last < len(distance) and distance[first] + r >= distance[last]:
            last += 1
        c += len(distance) - last
    return c

n, r = map(int, input().split())
distance = list(map(int, input().split()))
print(date(distance, r))
