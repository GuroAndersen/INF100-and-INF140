alfa = "abcdefghijklmnopqrstuvwxyz"
alfa_len = len(alfa)
mess = "KODESFVLXAZBGSUZCTKUWCJNZWIIHIAMHUDVLAOVRVPIYVVFE"
mess_len = len(mess)
key = "jisuan"
key_len = len(key)



x = mess_len % key_len
print(x)

tom = ""

for num in range (0, mess_len, 1):
    mess_time = mess[num]
    key_time = key[num%key_len]
    encrypt = (alfa.index(mess_time) + alfa.index(key_time)) % alfa_len
    ency = alfa[encrypt]
    tom = tom + ency
print (tom)