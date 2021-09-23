def hyd_pres(p, g, z):
    trykk = (p * g * z)*pow(10, -4)
    return trykk
print (hyd_pres(1025, 10, 100))