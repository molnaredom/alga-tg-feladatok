# Python3 code to find minimum steps to reach
# to specific cell in minimum moves by Knight
class cell:

    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


# checks whether given position is
# inside the board
def isInside(x, y, N):
    if (x >= 1 and x <= N and
            y >= 1 and y <= N):
        return True
    return False


# Method returns minimum step to reach
# target position
def minimum_eleresi_lepes_huszarral(indulasi_pozicio, erkezesi_pozicio):
    akt_huszar_allas = indulasi_pozicio
    # all possible movments for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    # az aktualis poziciot rogton bele is tesszük
    eddigi_lepesek_tomb = [{"cella_x": akt_huszar_allas["x"], "cella_y":akt_huszar_allas["y"], "tavolsag": 0}]

    # make all cell unvisited
    visited = [[False for i in range(9)]
               for j in range(9)]

    # visit starting state
    visited[akt_huszar_allas["x"]][akt_huszar_allas["y"]] = True

    # loop until we have one element in queue
    while (len(eddigi_lepesek_tomb) > 0):

        t = eddigi_lepesek_tomb.pop(0)

        print(t["tavolsag"])
        # if current cell is equal to target
        # cell, return its distance
        if (t["cella_x"] == erkezesi_pozicio["x"] and
                t["cella_y"] == erkezesi_pozicio["y"]):
            print(t["tavolsag"])
            exit()

        # iterate for all reachable states
        for i in range(8):

            x = t["cella_x"] + dx[i]
            y = t["cella_y"] + dy[i]

            if (isInside(x, y, 8) and not visited[x][y]):
                visited[x][y] = True
                eddigi_lepesek_tomb.append({"cella_x": akt_huszar_allas["x"],
                                       "cella_y":akt_huszar_allas["y"],
                                       "tavolsag": t["tavolsag"]+1}
                                      )


# Driver Code
if __name__ == '__main__':

    minimum_eleresi_lepes_huszarral(indulasi_pozicio ={"x": 6,"y": 1}, erkezesi_pozicio = {"x": 9,"y": 1})

# This code is contributed by
# Kaustav kumar Chanda
