from sympy import mod_inverse

congruences = [
    (47, 29),
    (53, 3),
    (63, 20),
    (5, 3),
    (8, 3),
]
N = 6277320  

def chinese_remainder(congruences, N):
    result = 0
    for n_i, a_i in congruences:
        N_i = N // n_i  
        M_i = mod_inverse(N_i, n_i)  
        result += a_i * N_i * M_i  
    return result % N  

x = chinese_remainder(congruences, N)
print(f"x % {N} = {x}")
