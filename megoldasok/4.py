# Python3 code to find minimum steps to reach
# to specific cell in minimum moves by Knight
class Mezo:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.tavolsaga = dist


def teruleten_belul_van_e(x, y, tablameret):
    if 1 <= x <= tablameret and 1 <= y <= tablameret:
        return True
    return False


# Method returns minimum step to reach
# target position
def min_huszarlepes(huszar_pozicioja, cel_pozicio, tabla_meret):
    lepes_lehetosegek = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    mar_latogatott_helyek_listaja = [Mezo(huszar_pozicioja[0], huszar_pozicioja[1], 0)]

    tabla_adott_pozicioja_volt_e_vizsgalva = []
    for i in range(tabla_meret + 1):
        tabla_adott_pozicioja_volt_e_vizsgalva.append([False for _ in range(tabla_meret + 1)])

    tabla_adott_pozicioja_volt_e_vizsgalva[huszar_pozicioja[0]][huszar_pozicioja[1]] = True

    # vegigprobalgatjuk az összes lehetőséget
    while True:
        if len(mar_latogatott_helyek_listaja) < 1:
            return -1

        aktualis_pozicio = mar_latogatott_helyek_listaja.pop(0)

        if aktualis_pozicio.x == cel_pozicio[0] and aktualis_pozicio.y == cel_pozicio[1]:
            return aktualis_pozicio.tavolsaga

        for i in range(8):

            x = aktualis_pozicio.x + lepes_lehetosegek[i][0]
            y = aktualis_pozicio.y + lepes_lehetosegek[i][1]

            if teruleten_belul_van_e(x, y, tabla_meret) and not tabla_adott_pozicioja_volt_e_vizsgalva[x][y]:
                tabla_adott_pozicioja_volt_e_vizsgalva[x][y] = True
                mar_latogatott_helyek_listaja.append(Mezo(x, y, aktualis_pozicio.tavolsaga + 1))


if __name__ == '__main__':
    print(min_huszarlepes(huszar_pozicioja=[1, 2], cel_pozicio=[2, 2], tabla_meret=8))
