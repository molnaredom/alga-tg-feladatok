"""
Hatékony algoritmus kis számú elem rendzésére
@param n hosszusagu rendzeő számok sorozatát alkotó A[1..n] tömb

"""
def beszuro_rendezes(A):

    for j in range(1,len(A)):
        i = j-1
        kulcs = A[j]

        while i>=0 and A[i] > kulcs:
            A[i+1] = A[i]
            i =i-1
        A[i+1] = kulcs

    return A

A=[1,2,3,4,5]
print(beszuro_rendezes(A))


"""
Első kör:
i = 0, j= 1 A = [5,4,3,2,1]
kulcs a [1.] elem ami a 4 
Ezután megvizsgáljuk hogy a 0. elem (5) nagyobb-e mintz 1. elem(4)
Igen nagyobb tehát meg kell őket cserélni
az i=0 még mindig A[i+1] = A[i] -> A[1] = A[0] -> a 4 et 5 re cseréljük
i =i-1 csökkentjük itt az i < 0 tehát ha ujra a while ciklusba lepnenk mar nem lehetne indexelni az A-t (i=-1 mást ad)
Így megtörtént egy csere és kiléptünk a ciklusból
Tehátz először a  4 et 5 re cserélte. 
2. körben [4,5,3,2,1] ből [3,4,5,2,1] a hármat 2 vel balra tolta

Ha tovább megyünk pl a 2 ig, észrevesszük, h egy lépésből nem tudjuk megoldani(ahogy 3 nál se), hanem annyiszor
 kell egyesével hátrébb tenni a 2 est amennyi nagyobb elem van előtte
 tehát pl [3,4,5,2,1] a 2 előtt 3 elem van , így 3* kell arrébbtenni egyel előre


"""