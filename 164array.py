n = int(input())
s = bin(n)[2:]
i2 = s.rindex('1')
print(len(s)-i2, end='')
