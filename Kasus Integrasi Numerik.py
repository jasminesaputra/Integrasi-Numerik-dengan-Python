def f(x):
    return 10 + 2*(x**2)

def trapezoidal(a, b, n, func):
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        s += 2 * func(a + i*h)
    return (h/2) * s

def simpson_13(a, b, n, func):
    if n % 2 != 0:
        raise ValueError("Simpson 1/3 membutuhkan n genap")
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        s += (4 if i % 2 == 1 else 2) * func(a + i*h)
    return (h/3) * s

def exact_integral(a, b):
    return (10*b + (2/3)*b**3) - (10*a + (2/3)*a**3)


# ===================== MAIN PROGRAM =====================
if __name__ == "__main__":
    a = 0
    b = 3

    exact = exact_integral(a, b)

    print("=== INTEGRASI NUMERIK ===")
    print("F(x) = 10 + 2x^2")
    print(f"Interval [{a}, {b}]")
    print(f"Nilai referensi (analitik) = {exact:.6f}\n")

    print(f"{'n':>5} | {'Trapesium':>12} | {'Error T':>10} | {'Simpson':>12} | {'Error S':>10}")
    print("-"*65)

    for n in [2, 4, 10, 50]:
        T = trapezoidal(a, b, n, f)
        errT = abs(T - exact)

        S = simpson_13(a, b, n, f)
        errS = abs(S - exact)

        print(f"{n:5d} | {T:12.6f} | {errT:10.6f} | {S:12.6f} | {errS:10.6f}")
