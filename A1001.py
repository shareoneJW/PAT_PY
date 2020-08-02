come_in = input()
a, b = map(int, come_in.split())
# print('{:,}'.format(a + b))
out = a + b
sign = '-' if out < 0 else ''
digits = str(abs(out))

res = ''
while digits:
    digits, last3 = digits[: -3], digits[-3:]
    res = (last3 + ',' + res) if res else last3

print(sign+res)


