t = 0
g = 9.8
po = float (input("Stenen droppes fra høyde: "))
p = po
while p>=0:
    p = (po - (g*t**2)/2)
    if p<=0:
        print("0 m")
        break
    else:
        print(f"{p:.1f} m")
    t = t + 1

print(f"Stenen lander mellom {t-1} og {t} sekunder etter at den droppes.")