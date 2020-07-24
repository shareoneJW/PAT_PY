come_in = input()
x, y = map(int, come_in.split())

out = x + y
sign = '-' if out < 0 else ''
out = abs(out)

if len(str(out)) <= 3:
    print(sign+str(out))
else:
    print(sign, end='')
    string = ''
    while out // 1000:
        string = ',' + '{:03}'.format(out % 1000) + string
        out = out // 1000
    else:
        string = str(out) + string
    print(string)