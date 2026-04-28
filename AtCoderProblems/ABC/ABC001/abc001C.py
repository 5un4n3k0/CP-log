from decimal import *

Deg, Dis = map(int, input().split())

deg = Deg / 10
Dis = (Decimal(Dis) / Decimal(60)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

dirs = [
    "NNE","NE","ENE","E","ESE","SE","SSE","S",
    "SSW","SW","WSW","W","WNW","NW","NNW"
]

Dir = "N"

for i in range(len(dirs)):
    if 22.5 * i + 11.25 <= deg < 22.5 * (i + 1) + 11.25:
        Dir = dirs[i]

if Dis <= Decimal("0.2"):
    Dir = "C"
    W = 0
elif Dis <= Decimal("1.5"):
    W = 1
elif Dis <= Decimal("3.3"):
    W = 2
elif Dis <= Decimal("5.4"):
    W = 3
elif Dis <= Decimal("7.9"):
    W = 4
elif Dis <= Decimal("10.7"):
    W = 5
elif Dis <= Decimal("13.8"):
    W = 6
elif Dis <= Decimal("17.1"):
    W = 7
elif Dis <= Decimal("20.7"):
    W = 8
elif Dis <= Decimal("24.4"):
    W = 9
elif Dis <= Decimal("28.4"):
    W = 10
elif Dis <= Decimal("32.6"):
    W = 11
else:
    W = 12

print(Dir, W)
