output = 'zZZzzZZz zZZzZZzz zZZzzzzZ zZZzzZZZ zZZZZzZZ zZzzZzzZ zzZzzzzz zZzzZZzz zZZzZZZZ zZZZzZZz zZZzzZzZ zzZzzzzz zZzzzzzZ zZzZzzZZ zZzzzzZZ zZzzZzzZ zZzzZzzZ zZZZZZzZ'.replace('z', '0').replace('Z', '1').split(' ')
for i in output:
    print(chr(int(i, 2)), end='')