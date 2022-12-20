text = input()

vowels_sum = 0
a = 1
e = 2
i = 3
o = 4
u = 5

for ch in text:
    if ch in (a, e, i, o, u):
        vowels_sum = sum(ord(ch) for ch in text)
        print(vowels_sum)
