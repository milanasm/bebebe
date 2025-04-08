p=[]
i=[]
def Lisa_inimesi(p:list,i:list):  #1ül
    """
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk:"))

                except:
                    print("Palk on arv:")
                p.append(palk)
                i.append(nimi)
                print("Andmed on lisatud")
        except:
                print("Kirjuta ainult tähtede kasutades")
    p.append(palk)
    i.append(nimi)

def Kustuta_inimene(p:list,i:list):   #2ül
    """
    """
    try:
        nimi=input("Nimi: ")
        if nimi.isalpha():
            k=i.count(nimi)
            if k>0:
                for j in range(k):
                    indeks=i.index(nimi)
                    i.pop(indeks)
                    p.pop(indeks)
            print(f"{nimi} ja tema palk on kustutatud.")
        else:
            print("Andmed puuduvad.")
    except:
        print("Kirjuta ainult tähtede kasutades.")

def suurim_palk(p:list,i:list): #3 samaya bolshaya ZP
    """
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    for j in range(k):
        indeks=p.index(suurim)
        print(f"Saab kätte {i[indeks]}")

def väiksem_palk(p: list, i: list): #4 samaya malenkaya ZP
    """
    """
    väiksem=min(p)
    print(f"Väikseim palk on {väiksem}")
    k=p.count(väiksem)
    for j in range(k):
        indeks=p.index(väiksem)
        print(f"Saab kätte {i[indeks]}")
        p.pop(indeks)
        i.pop(indeks)

def Sorteerimine_acs(p:list,i:list): #5
    """
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i
    
def Sorteerimine_desc(p:list,i:list): #6
    """
    """
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            if p[n]<p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]     
    return p, i

def Sama_palk(p: list, i: list):  #7ül
    """
    """
    loetud=[]
    for j in range(len(p)):
        k=0
        for l in range(len(loetud)):
            if p[j]==loetud[l]:
                k+=1
        if k==0:
            mitu=0
            for m in range(len(p)):
                if p[j]==p[m]:
                    mitu+=1
            if mitu>1:
                print(f"Palk {p[j]} saavad {mitu} inimest:")
                for n in range(len(p)):
                    if p[n]==p[j]:
                        print(f"{i[n]} - {p[n]}")
                loetud.append(p[j])

def Otsi_nime(p: list, i: list):  #8ül
    """
    """
    nimi=input("Sisesta nimi: ")
    if nimi.isalpha():
        leitud=0
        for j in range(len(i)):
            if i[j]==nimi:
                print(f"{i[j]} - {p[j]}")
                leitud+=1
        if leitud==0:
            print("Sellise nimega inimest ei leitud.")
    else:
        print("Kirjuta ainult tähtede kasutades.")

def Rohkem_kui(p:list,i:list):  #9ül
    """
    """
    try:
        summa=float(input("Sisesta summa: "))
        for j in range(len(p)):
            if p[j]>summa:
                print(f"{i[j]} - {p[j]}")
    except:
        print("Viga! Kirjuta arv.")

def Vahem_kui(p:list,i:list):
    """
    """
    try:
        summa=float(input("Sisesta summa: "))
        for j in range(len(p)):
            if p[j]<summa:
                print(f"{i[j]} - {p[j]}")
    except:
        print("Viga! Kirjuta arv.")

def Keskmine_palk(p:list,i:list):  #10ül
    """
    """
    if len(p)>0:
        keskmine=sum(p)/len(p)
        print(f"Keskmine palk on {keskmine}")
        k=p.count(keskmine)
        if k>0:
            for j in range(k):
                indeks=p.index(keskmine)
                print(f"Keskmist palka saab {i[indeks]}")
                p.pop(indeks)
                i.pop(indeks)
        else:
            print("Keegi ei saa täpselt keskmist palka.")
    else:
        print("Andmed puuduvad.")

