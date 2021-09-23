message = "SECURITY"

for bokstav in message:
    M = ord(bokstav)
    p = 13
    q = 19
    e = 5
    n = p * q
    phi_n = (p - 1)*(q - 1)

    d = pow(e,(-1), mod= phi_n)
    c = (M**e) % n
    print (hex(c))
    
    





