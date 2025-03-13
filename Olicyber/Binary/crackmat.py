import sympy as sp

def solve_flag():
    flag = []
    for i, equation in enumerate([
        "x**2 - 204*x + 10404",  # a1
        "x**2 - 216*x + 11664",  # a2
        "x**2 - 194*x + 9409",   # a3
        "x**2 - 206*x + 10609",  # a4
        "x**2 - 246*x + 15129",  # a5
        "x**2 - 200*x + 10000",  # a6
        "x**2 - 102*x + 2601",   # a7
        "x**2 - 232*x + 13456",  # a8
        "x**2 - 202*x + 10201",  # a9
        "x**2 - 228*x + 12996",  # a10
        "x**2 - 218*x + 11881",  # a11
        "x**2 - 210*x + 11025",  # a12
        "x**2 - 220*x + 12100",  # a13
        "x**2 - 194*x + 9409",   # a14
        "x**2 - 220*x + 12100",  # a15
        "x**2 - 232*x + 13456",  # a16
        "x**2 - 202*x + 10201",  # a17
        "x**2 - 190*x + 9025",   # a18
        "x**2 - 96*x + 2304",    # a19
        "x**2 - 250*x + 15625"    # a20
    ]):
        x = sp.Symbol('x')
        solutions = sp.solve(equation, x)
        
        # Prendiamo il valore ASCII valido (deve essere un carattere visibile)
        valid_char = [chr(int(s)) for s in solutions if 32 <= s <= 126]
        
        if valid_char:
            flag.append(valid_char[0])
        else:
            raise ValueError(f"Nessun carattere valido per la posizione {i}")
    
    return "".join(flag)

if __name__ == "__main__":
    print("Flag trovata:", solve_flag())
