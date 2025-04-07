p=[]
i=[]
def Lisa_inimesi(p:list,i:list):
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

def Kustuta_inimene(p:list,i:list):
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

def suurim_palk(p:list,i:list): #samaya bolshaya ZP
    """
    """
    suurim=max(p)
    print(f"Suurim palk on {suurim}")
    k=p.count(suurim)
    for j in range(k):
        indeks=p.index(suurim)
        print(f"Saab kätte {i[indeks]}")

def väiksem_palk(p: list, i: list): #samaya malenkaya ZP
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

def Sorteerimine_acs(p:list,i:list):
    """
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i
    
def Sorteerimine_desc(p: list, i: list):
    """
    """
    for n in range(0, len(i)):
        for m in range(n, len(i)):
            if p[n]<p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]     
    return p, i

def Omalik_palk(p: list, i: list):
    """
    """
    while True:
        if len(p)==0 or len(i)==0:
            print("Viga: nimekiri ei saa olla tühi.")
            return
 
        palk_dict={}
        for palk in p:
            if palk in palk_dict:
                palk_dict[palk]+=1
            else:
                palk_dict[palk]=1   
        for palk,count in palk_dict.items():
            if count>1:
                print(f"Palk {palk} esineb {count} korda.")
                print("Inimesed, kes saavad seda palka:")
                for j in range(len(p)):
                    if p[j]==palk:
                        print(f"{i[j]}: {p[j]}")
        break           