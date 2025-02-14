def js_xor(a, b):
    # Simula ToInt32: convertiamo a e b in numeri a 32 bit
    a = int(a) & 0xFFFFFFFF
    b = int(b) & 0xFFFFFFFF
    res = a ^ b
    # Se il risultato è >= 2^31, lo interpretiamo come negativo
    if res & 0x80000000:
        res = res - 0x100000000
    return res

def compute_token():
    token = [None] * 36  # Il token ha 36 caratteri

    # Posizione 13: (((-30420 / 13) / 30) + 123)
    a = int(-30420 / 13)   # -2340
    b = int(a / 30)        # -78
    token[13] = chr(b + 123)  # -78+123 = 45 -> '-'

    # Posizione 11: (((((-33063 / 103) / 107) ^ 86) + 76) + 111)
    a = int(-33063 / 103)   # -321
    b = int(a / 107)        # -3
    c = js_xor(b, 86)       # -3 ^ 86 in 32 bit
    token[11] = chr(c + 76 + 111)  # (-3^86) + 76 + 111

    # Posizione 29: (((-251 ^ 141) + 64) + 105)
    c = js_xor(-251, 141)
    token[29] = chr(c + 64 + 105)

    # Posizione 3: (((((2052 ^ 87) ^ 111) / 68) ^ 91) - 12)
    a = js_xor(2052, 87)
    b = js_xor(a, 111)
    c = int(b / 68)
    d = js_xor(c, 91)
    token[3] = chr(d - 12)

    # Posizione 16: ((((16 ^ 23) + 61) - 119) + 150)
    a = js_xor(16, 23)
    token[16] = chr(a + 61 - 119 + 150)

    # Posizione 2: (((-1140 / 95) ^ 82) + 139)
    a = int(-1140 / 95)  # -12
    b = js_xor(a, 82)
    token[2] = chr(b + 139)

    # Posizione 6: (((20266 - 26) / 115) - 123)
    a = 20266 - 26  # 20240
    b = int(a / 115)  # 20240/115 = 176
    token[6] = chr(b - 123)

    # Posizione 23: ((((1218 - 57) + 2) ^ 52) / 27)
    a = 1218 - 57 + 2  # 1163
    b = js_xor(a, 52)
    c = int(b / 27)
    token[23] = chr(c)

    # Posizione 21: ((((27 - 113) - 83) + 79) + 141)
    a = 27 - 113 - 83 + 79 + 141  # 27-113=-86, -86-83=-169, -169+79=-90, -90+141=51
    token[21] = chr(a)

    # Posizione 14: ((((((167 ^ 77) ^ 133) - 107) ^ 5) ^ 80) - 29)
    a = js_xor(167, 77)
    b = js_xor(a, 133)
    c = b - 107
    d = js_xor(c, 5)
    e = js_xor(d, 80)
    token[14] = chr(e - 29)

    # Posizione 27: ((((((57812794 ^ 50) / 88) + 127) / 90) / 49) - 94)
    a = js_xor(57812794, 50)
    b = int(a / 88)
    c = b + 127
    d = int(c / 90)
    e = int(d / 49)
    token[27] = chr(e - 94)

    # Posizione 7: (((((8375612 / 28) - 139) / 145) + 5) / 39)
    a = int(8375612 / 28)
    b = a - 139
    c = int(b / 145)
    d = c + 5
    e = int(d / 39)
    token[7] = chr(e)

    # Posizione 18: ((((((-7664 ^ 69) + 3) - 24) / 56) ^ 133) + 48)
    a = js_xor(-7664, 69)
    b = a + 3 - 24
    c = int(b / 56)
    d = js_xor(c, 133)
    token[18] = chr(d + 48)

    # Posizione 20: (((((179 ^ 85) + 32) - 117) ^ 149) ^ 55)
    a = js_xor(179, 85)
    b = a + 32 - 117
    c = js_xor(b, 149)
    d = js_xor(c, 55)
    token[20] = chr(d)

    # Posizione 25: ((((((235 + 77) - 77) - 35) - 127) + 24) ^ 5)
    a = (235 + 77 - 77 - 35 - 127 + 24)
    token[25] = chr(js_xor(a, 5))

    # Posizione 24: (((-14 + 60) ^ 65) - 14)
    a = -14 + 60
    token[24] = chr(js_xor(a, 65) - 14)

    # Posizione 28: (((236 - 140) ^ 135) ^ 129)
    a = 236 - 140
    token[28] = chr(js_xor(js_xor(a, 135), 129))

    # Posizione 0: (((29 ^ 93) / 8) + 48)
    a = js_xor(29, 93)
    b = int(a / 8)
    token[0] = chr(b + 48)

    # Posizione 12: (((((16654 ^ 78) ^ 145) / 83) + 25) ^ 130)
    a = js_xor(16654, 78)
    b = js_xor(a, 145)
    c = int(b / 83)
    d = c + 25
    token[12] = chr(js_xor(d, 130))

    # Posizione 8: ((((154 ^ 126) ^ 118) - 5) - 96)
    a = js_xor(154, 126)
    b = js_xor(a, 118)
    token[8] = chr(b - 5 - 96)

    # Posizione 32: (((((7 ^ 143) - 112) + 59) - 68) + 38)
    a = js_xor(7, 143)
    b = a - 112 + 59 - 68 + 38
    token[32] = chr(b)

    # Posizione 4: (((((10817 + 112) - 120) - 81) / 149) + 28)
    a = 10817 + 112 - 120 - 81
    b = int(a / 149)
    token[4] = chr(b + 28)

    # Posizione 15: ((((((262 ^ 116) ^ 140) ^ 117) - 105) - 133) - 59)
    a = js_xor(262, 116)
    b = js_xor(a, 140)
    c = js_xor(b, 117)
    token[15] = chr(c - 105 - 133 - 59)

    # Posizione 5: ((((((13809800 / 145) / 10) + 137) ^ 143) / 138) ^ 118)
    a = int(13809800 / 145)
    b = int(a / 10)
    c = b + 137
    d = js_xor(c, 143)
    e = int(d / 138)
    token[5] = chr(js_xor(e, 118))

    # Posizione 19: ((((-428 ^ 83) / 101) + 100) ^ 102)
    a = js_xor(-428, 83)
    b = int(a / 101)
    token[19] = chr(js_xor(b + 100, 102))

    # Posizione 10: ((((6720 + 28) + 16) / 76) - 33)
    a = 6720 + 28 + 16
    b = int(a / 76)
    token[10] = chr(b - 33)

    # Posizione 31: (((15456 / 138) - 14) ^ 3)
    a = int(15456 / 138)
    token[31] = chr(js_xor(a - 14, 3))

    # Posizione 17: (((1657 - 59) + 136) / 34)
    a = 1657 - 59 + 136
    b = int(a / 34)
    token[17] = chr(b)

    # Posizione 1: ((((((-4323 ^ 53) / 56) + 21) + 43) + 41) + 22)
    a = js_xor(-4323, 53)
    b = int(a / 56)
    c = b + 21 + 43 + 41 + 22
    token[1] = chr(c)

    # Posizione 9: ((((((34470 / 15) ^ 60) + 122) / 37) - 12) ^ 7)
    a = int(34470 / 15)
    b = js_xor(a, 60)
    c = int((b + 122) / 37)
    token[9] = chr(js_xor(c - 12, 7))

    # Posizione 35: (((298 - 27) - 146) ^ 24)
    a = 298 - 27 - 146
    token[35] = chr(js_xor(a, 24))

    # Posizione 26: (((97 ^ 133) ^ 35) - 97)
    a = js_xor(97, 133)
    token[26] = chr(js_xor(a, 35) - 97)

    # Posizione 33: (((((12604 / 137) - 95) - 63) - 3) + 122)
    a = int(12604 / 137)
    token[33] = chr(a - 95 - 63 - 3 + 122)

    # Posizione 34: (((((342639 / 33) + 121) ^ 3) / 133) ^ 45)
    a = int(342639 / 33)
    b = a + 121
    c = js_xor(b, 3)
    d = int(c / 133)
    token[34] = chr(js_xor(d, 45))

    # Posizione 22: ((((((132974976 / 128) - 3) - 53) + 149) / 148) / 130)
    a = int(132974976 / 128)
    b = a - 3 - 53 + 149
    c = int(b / 148)
    d = int(c / 130)
    token[22] = chr(d)

    # Posizione 30: ((((((2319989 + 11) / 80) / 145) ^ 114) ^ 94) ^ 134)
    a = int((2319989 + 11) / 80)
    b = int(a / 145)
    c = js_xor(b, 114)
    d = js_xor(c, 94)
    e = js_xor(d, 134)
    token[30] = chr(e)
    
    return ''.join(token)

if __name__ == '__main__':
    print('Token trovato:', compute_token())
