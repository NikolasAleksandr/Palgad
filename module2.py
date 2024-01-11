def Lisamine(inimesed, palgad, kogus):
    """Andmete lisamine listidesse
	Tagastab listid
	:param list i: Inimeste nimekiri
	:param list p: Palkade loetelu
	:param list k: Inimeste kogus
	:rtype:list, list
   	"""
    for nimi in range(kogus):
        nimi = input("Sisesta uue inimese nimi: ")
        palk = int(input("Sisesta tema palk: "))
        inimesed.append(nimi)
        palgad.append(palk)
    return inimesed, palgad


def Eemaldamine(inimesed, palgad, nimi):
    if nimi in inimesed:
        index = inimesed.index(nimi)
        inimesed.pop(index)
        palgad.pop(index)
        print(f"{nimi} ja tema palk on eemaldatud.")
    else:
        print(f"{nimi} ei ole palgalehel.")
    return inimesed, palgad

def SuurimPalk(inimesed, palgad):
    if not palgad:
        return None, None

    maksimum_palk = max(palgad)
    indeksid_max_palk = [i for i, palk in enumerate(palgad) if palk == maksimum_palk]
    
    nimi_list = [inimesed[i] for i in indeksid_max_palk]

    return maksimum_palk, nimi_list

def KõigeVäiksemPalk(inimesed, palgad):
    if not palgad:
        return None, None
    minimum_palk= min(palgad)
    indeksid_min_palk = [i for i, palk in enumerate(palgad) if palk == minimum_palk]

    nimi_list = [inimesed[i] for i in indeksid_min_palk]
    return minimum_palk, nimi_list


def SortPalgad(i: list, p: list, a: int):
    N = len(i)

    if a == 1:  
        for n in range(0, N):
            for m in range(n + 1, N):
                if p[n] > p[m]:
                    
                    p[n], p[m] = p[m], p[n]

                    
                    i[n], i[m] = i[m], i[n]
    elif a == -1:  
        for n in range(0, N):
            for m in range(n + 1, N):
                if p[n] < p[m]:
                    
                    p[n], p[m] = p[m], p[n]

                    
                    i[n], i[m] = i[m], i[n]
    else:
        print("Vigane valik 'a' jaoks. Palun sisestage 1 tõstesorteerimiseks või -1 laskuvas järjestuses sorteerimiseks.")


def ÜhesugusedPalgad(i: list, p: list):
    duplikaadid = {}
    
    for n in range(len(p)):
        palk = p[n]
        if palk in duplikaadid:
            duplikaadid[palk].append(i[n])
        else:
            duplikaadid[palk] = [i[n]]

    for palk, inimesed_list in duplikaadid.items():
        if len(inimesed_list) > 1:
            print(f"Zarplata {palk} saavad: {', '.join(inimesed_list)}")


def OtsiPalgaJärgi(i: list, p: list, otsitav_nimi: str):
    leitud_palgad = []

    for n in range(len(i)):
        if i[n] == otsitav_nimi:
            leitud_palgad.append(p[n])

    if leitud_palgad:
        print(f"{otsitav_nimi} palgad: {', '.join(map(str, leitud_palgad))}")
    else:
        print(f"{otsitav_nimi} ei ole palgalehel.")

