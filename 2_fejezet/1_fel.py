import random


def egyenloe(n):
    veletlen_szam_index = random.randint(0, n-1)
    # print("n =",n,"index =",veletlen_szam_index, "talált_tömbelem = ",tomb[veletlen_szam_index])
    if tomb[veletlen_szam_index] == keresett_elem:
        # print("Kész vagyunk!")
        return global_n-n+1
    elif n-1 == 0:
        # print("Az összes indexet megpróbáltuk")
        return global_n-n+1
    else:
        return egyenloe(n-1)


for global_n in range(1,21):
    i = 0
    szum = 0
    while True:
        tomb = [random.randint(0, global_n - 1) for i in range(global_n)]
        # print("tomb=" ,tomb)

        keresett_elem = tomb[random.randint(0, global_n - 1)]
        # print("keresett elem =", keresett_elem)

        i += 1
        szum += egyenloe(global_n)

        if i> 100000:
            print(f"{global_n} =",i/szum)
            break




