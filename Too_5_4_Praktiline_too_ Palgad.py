from palgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed:")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmed lisamiseks\n2-Andmete kustutamiseks nime järgi")
    v=int(input())
    if v==1:
        Lisa_inimesi(palgad,inimesed)
    elif v==2:
        Kustuta_inimene(palgad,inimesed)
    elif v==3:
        suurim_palk(palgad,inimesed)
    elif v==4:
        väiksem_palk(palgad,inimesed)
    elif v==5:
        Sorteerimine_acs(palgad,inimesed)
    elif v==6:
        Sorteerimine_desc(palgad,inimesed)
    elif v==7:
        break
    else:
        print("Vale valik. Palun proovige uuesti")

        