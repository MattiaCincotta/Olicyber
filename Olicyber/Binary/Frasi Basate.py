#Obiettivo: è necessario reversare la funzione hint di modo tale che venga stampata la flag, per fare ciò sarà anche necessario prendersi g_val5

def xor(a1, a2):
    result = bytearray(a2)
    for i in range(a2):
        result[i] = a1[i] ^ 0x42
    return result

def hint():
    result = xor(g_val5, 14)
    print(result.decode()) 

g_val5 = bytearray([0x0a, 0x2b, 0x2c, 0x36, 0x78, 0x62, 0x20, 0x23, 0x31, 0x27, 0x74, 0x76, 0x42, 0x00, 0x00, 0x00])
hint()  
