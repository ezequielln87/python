valar = 1500.00

if valar <= 1830.29:
    valar -= valar * 0.08
elif valar <= 3050.52:
    valar -= valar * 0.09
elif valar <= 6101.06:
    valar -= valar * 0.11

print(valar)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
