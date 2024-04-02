a = float(input())
b = float(input())
sigma = 0.001
max_step = 5
k = 0
f_a = a
f_b = b
xm = (a + b) / 2
f_xm = xm
while k < max_step:
    if (b - a > sigma) and (k < max_step):
        c = xm
    else:
        if f_a * f_b <= 0:
            b = xm
            f_b = f_xm
        else:
            a = xm
            f_a = f_xm
    k += 1

print(xm)