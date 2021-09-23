
for a in range (0, 26):
    for b in range (0, 26):
        for c in range (0, 26):
            for d in range (0, 26):
                for e in range (0, 26):
                    for f in range (0, 26):
                        for g in range (0, 26):
                            for h in range (0, 26):
                                if (((a + b + e + g) % 26)== 2) and (((b + c + f + h) % 26) == 16) and (((c + d + g + e) % 26) == 2) and (((d + a + h + f) % 26) == 24):
                                    print (a, b, c, d, e, f, g, h)
                                    break