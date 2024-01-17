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
    """Eemaldab inimese ja tema palga vastavalt sisestatud nimele.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    """
    if nimi in inimesed:
        index = inimesed.index(nimi)
        inimesed.pop(index)
        palgad.pop(index)
        print(f"{nimi} ja tema palk on eemaldatud.")
    else:
        print(f"{nimi} ei ole palgalehel.")
    return inimesed, palgad

def SuurimPalk(inimesed, palgad):
    """Leiab suurima palga ja tagastab selle ning vastava inimese nime.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :rtype: tuple
    """
    if not palgad:
        return None, None

    maksimum_palk = max(palgad)
    indeksid_max_palk = [i for i, palk in enumerate(palgad) if palk == maksimum_palk]
    
    nimi_list = [inimesed[i] for i in indeksid_max_palk]

    return maksimum_palk, nimi_list

def KoigeVaiksemPalk(inimesed, palgad):
    """Leiab vaikseima palga ja tagastab selle ning vastava inimese nime.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :rtype: tuple
    """
    if not palgad:
        return None, None
    minimum_palk= min(palgad)
    indeksid_min_palk = [i for i, palk in enumerate(palgad) if palk == minimum_palk]

    nimi_list = [inimesed[i] for i in indeksid_min_palk]
    return minimum_palk, nimi_list


def SortPalgad(i: list, p: list, a: int):
    """Sorteerib palgad vastavalt kasutaja valitud jarjestusele.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :param int a: Jarjestuse suund (1 - tõusev, -1 - kahanev)
    """
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
        print("Vigane valik 'a' jaoks. Palun sisestage 1 tostesorteerimiseks voi -1 laskuvas jarjestuses sorteerimiseks.")


def YhesugusedPalgad(i: list, p: list):
    """Leiab ja kuvab inimesed, kes saavad samasugust palka.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    """
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


def OtsiPalgaJargi(i: list, p: list, otsitav_nimi: str):
    """Otsib inimese palga jargi ja kuvab leitud palgad.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :param str otsitav_nimi: Otsitava inimese nimi
    """
    leitud_palgad = []

    for n in range(len(i)):
        if i[n] == otsitav_nimi:
            leitud_palgad.append(p[n])

    if leitud_palgad:
        print(f"{otsitav_nimi} palgad: {', '.join(map(str, leitud_palgad))}")
    else:
        print(f"{otsitav_nimi} ei ole palgalehel.")

def PalgadSuuremadKui(i: list, p: list, limiit: int):
    """Kuvab inimesed, kes saavad rohkem kui maaratud summa.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :param int limiit: Maaratud summa
    """
    suuremad_inimesed = [(inimene, palk) for inimene, palk in zip(i, p) if palk > limiit]

    if suuremad_inimesed:
        print(f"Inimesed, kes saavad rohkem kui {limiit}:")
        for inimene, palk in suuremad_inimesed:
            print(f"{inimene} saab {palk} katte")
    else:
        print(f"Ykski inimene ei saa rohkem kui {limiit}.")

def PalgadVahemKui(i: list, p: list, limiit: int):
    """Kuvab inimesed, kes saavad vähem kui määratud summa.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :param int limiit: Maaratud summa
    """
    vahem_inimesed = [(inimene, palk) for inimene, palk in zip(i, p) if palk < limiit]

    if vahem_inimesed:
        print(f"Inimesed, kes saavad vahem kui {limiit}:")
        for inimene, palk in vahem_inimesed:
            print(f"{inimene} saab {palk} katte")
    else:
        print(f"Ykski inimene ei saa vahem kui {limiit}.")
        

def Keskmine(i: list, p: list):
    """Leiab keskmise palga ja inimese, kes saab sellele koige lahedasema palga.
    :param list i: Inimeste nimekiri
    :param list p: Palkade loetelu
    :return: Keskmise palga vaartus, Keskmisele palgale koige lahemal oleva inimese nimi
    :rtype: tuple
    """
    
    if not p:
        print("Palgad on tyhjad.")
        return None, None

    keskmine_palk = sum(p) / len(p)
    keskmise_saaja_index = p.index(min(p, key=lambda x: abs(x - keskmine_palk)))

    return keskmine_palk, i[keskmise_saaja_index]


