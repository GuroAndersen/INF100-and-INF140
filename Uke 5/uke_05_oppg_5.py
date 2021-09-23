def egen_abs(a):
    if a<0:
        return (a*(-1))
    else:
        return (a)



def egen_max(a, b):
    c = ((a+b)+ egen_abs(a-b))/2
    return c

def egen_min(a, b):
    c = (a+b - egen_abs(a-b))/2
    return c

def egen_len(a):
    tell_1 = 0
    for letter in a:
        tell_1 += 1
    return tell_1

print (egen_len("-3"))