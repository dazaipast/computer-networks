def exp(a):
    print(f"Число: {a}  ({bin(a)})")
    print(f"  a & 1  = {a & 1}")
    print(f"  a | 1  = {a | 1}")
    print(f"  a ^ 1  = {a ^ 1}")
    print(f"  ~a     = {~a}")
    print(f"  a << 1 = {a << 1}")
    print(f"  a >> 1 = {a >> 1}")

a = int(input("Введите число: "))
exp(a)