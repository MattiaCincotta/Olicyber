flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'

decoded_flag = ''.join([
    chr((ord(c) >> 8) & 0xFF) + chr(ord(c) & 0xFF)  
    for c in flag
])

print(decoded_flag)
