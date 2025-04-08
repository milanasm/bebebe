from palgad import *

palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed:")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmed lisamiseks\n2-Andmete kustutamiseks nime järgi")
    print("3-Suurim palk\n4-Väikseim palk\n5-Sorteeri kasvavalt\n6-Sorteeri kahanevalt")
    print("7-Otsime sama palgaga inimesed\n8-Otsi palk nime jargi\n9-Rohkem kui\n10-Vahem kui\n11-Keskmine palk\n12-Välju")
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
        Sama_palk(palgad,inimesed)
    elif v==8:
        Otsi_nime(palgad,inimesed)
    elif v==9:
        Rohkem_kui(palgad,inimesed)
    elif v==10:
        Vahem_kui(palgad,inimesed)
    elif v==11:
        Keskmine_palk(palgad,inimesed)
    elif v==12:
        break