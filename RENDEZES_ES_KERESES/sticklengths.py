def minimalis_koltseg_azonos_botokhoz(botok_szama, botok):
    # Botok rendezése
    botok.sort()
    
    # Medián kiszámítása
    median = botok[botok_szama // 2]
    
    # Költség számítása
    koltseg = sum(abs(bot - median) for bot in botok)
    
    return koltseg

# Bemenet
botok_szama = int(input())
botok = list(map(int, input().split()))

# Megoldás meghívása
eredmeny = minimalis_koltseg_azonos_botokhoz(botok_szama, botok)

# Kimenet
print(eredmeny)

