n = int(input())
w = input()
s = input()
stack = []
d = {")": "(",
     "]": "["}

for i in range(len(s)):
    if s[i] not in d:
        stack.append(s[i])
    elif s[i] in d:
        stack.pop()

result = []
for j in range(1, n - len(s) + 1):
    for skobka in w:
        if (skobka not in d) and (n - len(s) - j + 1 >= len(stack) + 2):
            result.append(skobka)
            stack.append(skobka)
            break
        elif (skobka in d) and stack and stack[-1] == d[skobka]:
            result.append(skobka)
            stack.pop()
            break
print(s + "".join(result))
