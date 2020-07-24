x = input().split()
y = input().split()
num1, num2 = int(x[0]), int(y[0])

d1, d2, d3 = {}, {}, {}

for i in range(1, num1*2+1, 2):
    d1[int(x[i])] = float(x[i+1])

for i in range(1, num2*2+1, 2):
    d2[int(y[i])] = float(y[i+1])

s = set(d1.keys()) | set(d2.keys())

for i in s:
    out = d1.get(i, 0) + d2.get(i, 0)
    if out:
        d3[i] = out

print(len(d3), end='')
if len(d3) != 0:
    for i in sorted(s, reverse=True):
        try:
            print(' {} {:.1f}'.format(i, d3[i]), end='')
        except KeyError:
            continue
