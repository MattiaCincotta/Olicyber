key = {'f': 18, 'l': 58, 'a': 22, 'g': 30, '{': 33, '4': 63, 'p': 68, 'r': 47, 'e': 6, 'n': 56, 't': 5, 'y': 40, '_': 17, '1': 30, 's': 53, 'c': 54, 'o': 63, '0': 67, 'w': 3, '3': 20, 'i': 26, 'u': 37, '6': 16, '5': 26, '9': 63, '8': 50, '}': 26}
flag = 'fsa3n_yt0yt_e1_tn_9_ctpf_1n54s1_psui8op{}g4s_rcr4l1n4e3wllrs16e_3ea_n'


def spin(flag, key):
    key = key % len(flag)
    return flag[-key:] + flag[:-key]

def decrypt(flag, key):
    for i in range(len(flag) - 1, 0, -1):  # start, stop, step
        flag = flag[:i] + spin(flag[i:], -key[flag[i-1]])  # Inverti la rotazione

    return flag
    
output = decrypt(flag, key)
print(f'output: {output}')