def g(n):
    if n <= 1:
        return n
    else:
        return 5 * g(n - 1) - 6 * g(n - 2)


def f(n):
    return 3**n -2**n


for i in range(0,40):
    print(i,"f és g értéke egyenlő" if g(i)==f(i) else "Nem egyenlőek", "értékük:",g(i))

"""
# 3^n -2^n
0 --> 0
1 --> 3 -2 = 1
2 --> 3^2 -2^2 = 9-4 = 5
3 --> 3^3 - 2^3 = 27-8 = 19
...

# 5 * (egyel ezelőtti érték) - 6 * (kettővel ezelttői érték)
2 --> 5*1 - 6*0 = 5
3 --> 5*5 - 6*1 = 19
4 --> 5*19 - 6*5 = 65
...




5*g(5*g(n) - 6*g(n-1)) - 6*g(n-2)




Ahogy láttuk a programban, mivel az első próbákre is megegyezik, a többi példánál is működni fog






teljes indukció:


"""