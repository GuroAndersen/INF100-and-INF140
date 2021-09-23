num = input("Binært tall: ")
num_len = len(num)

y = 0
x = 1
i = 0

sum = 0

for tall in num:
    sum += (int(tall) * 2**(num_len-1-i))
    i += 1

print (sum)