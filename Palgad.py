from module2 import *

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

while True:
    print("1 - Lisamine")
    print("2 - Eemaldamine")
    print("3 - Suurim palk ja omanik")
    print("4 - Kõige väiksem palk ja omanik")
    print("5 - Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega")
    print("6 - Ühesugused palgad")
    print("7 - Otsi palga järgi")
    v = int(input("Vali tegevus (sisesta 0 lõpetamiseks): "))

    if v == 0:
        break  

    elif v == 1:
        k = int(input("Mitu inimest lisame? "))
        inimesed, palgad = Lisamine(inimesed, palgad, k)
        
        
        for i in range(len(palgad)):
            print(inimesed[i], " saab kätte", palgad[i])
    elif v == 2:
        nimi = input("Sisesta inimese nimi, keda soovid eemaldada: ")
        inimesed, palgad = Eemaldamine(inimesed, palgad, nimi)

        for i in range(len(palgad)):
            print(inimesed[i], " saab kätte", palgad[i])

    elif v == 3:
        suurim_palk, saajad = SuurimPalk(inimesed, palgad)
        if suurim_palk is not None:
            print(f"Suurim palk on {suurim_palk}, mida saavad: {', '.join(saajad)}")
        else:
            print("Palgad on tühjad.")

    elif v == 4:
        väiksem_palk, saajad = KõigeVäiksemPalk(inimesed, palgad)
    if väiksem_palk is not None:
        print(f"Väikseim palk on {väiksem_palk}, mida saavad: {', '.join(saajad)}")
    else:
        print("Palgad on tühjad.")


    elif v == 5:
    a = int(input("Vali järjestus (1 - tõusev, -1 - kahanev): "))
    SortPalgad(inimesed, palgad, a)

    for i in range(len(palgad)):
        print(inimesed[i], " saab kätte", palgad[i])


    elif v == 6:
    ÜhesugusedPalgad(inimesed, palgad)


    elif v == 7:
    otsitav_nimi = input("Sisesta inimese nimi: ")
    OtsiPalgaJärgi(inimesed, palgad, otsitav_nimi)







