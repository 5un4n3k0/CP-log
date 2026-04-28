m = float(input()) / 1000

VV = 0


if 0.1 <= m <= 5:
    VV = m * 10
elif 6 <= m <= 30:
    VV = m + 50
elif 35 <= m <= 70:
    VV = (m - 30) / 5 + 80
elif m > 70:
    VV = 89

print(str(int(VV)).zfill(2))
