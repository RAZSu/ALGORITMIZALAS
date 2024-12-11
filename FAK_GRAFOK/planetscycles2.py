def teleportaciok_szamolasa(n, teleporterek):
    eredmeny = [0] * n  # Az eredményeket tároló lista
    latogatott = [False] * n  # A látogatott bolygókat jelöli

    for i in range(n):
        if not latogatott[i]:
            # Új útvonal indítása
            utvonal = []
            jelenlegi = i

            while not latogatott[jelenlegi]:
                latogatott[jelenlegi] = True
                utvonal.append(jelenlegi)
                jelenlegi = teleporterek[jelenlegi] - 1

            # Meghatározzuk, hogy találtunk-e ciklust
            if jelenlegi in utvonal:
                ciklus_kezdete = utvonal.index(jelenlegi)
                ciklus_hossza = len(utvonal) - ciklus_kezdete

                # Az eredmény frissítése a ciklusban lévő bolygókra
                for idx in range(ciklus_kezdete, len(utvonal)):
                    eredmeny[utvonal[idx]] = ciklus_hossza

                # Az eredmény frissítése a ciklushoz vezető bolygókra
                for idx in range(ciklus_kezdete):
                    eredmeny[utvonal[idx]] = ciklus_hossza + ciklus_kezdete - idx
            else:
                # Az eredmény frissítése olyan bolygókra, amelyek egy már kiszámított ciklushoz vezetnek
                for idx, bolygo in enumerate(utvonal):
                    eredmeny[bolygo] = eredmeny[jelenlegi] + len(utvonal) - idx

    return eredmeny


# Bemenet olvasása
n = int(input())  # A bolygók száma
teleporterek = list(map(int, input().split()))  # A teleporterek célpontjai

# Teleportációk számának kiszámítása
eredmeny = teleportaciok_szamolasa(n, teleporterek)

# Eredmény kiírása
print(' '.join(map(str, eredmeny)))
