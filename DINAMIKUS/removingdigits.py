def nulla(n):
    lepesszamlalo = 0
    while n > 0:                                         
        legnagyobb = max(int(szam) for szam in str(n))   
        n -= legnagyobb
        lepesszamlalo += 1
    return lepesszamlalo

n = int(input())
print(nulla(n))