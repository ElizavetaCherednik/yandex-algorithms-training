from collections import Counter

g, s = map(int, input().split())
model = input()
text = input()
word = Counter(model)
window = text[:g]
d_window = Counter(window)
c = 0
if d_window == word:
    c += 1
for i in range(g, s):
    d_window[text[i-g]] -= 1
    if d_window[text[i-g]] == 0:
        del d_window[text[i-g]]
    d_window[text[i]] = d_window.get(text[i], 0) + 1
    if d_window == word:
        c += 1
print(c)
