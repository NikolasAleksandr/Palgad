from module2 import *

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

while True:
    print("1 - Lisamine")
    print("2 - Eemaldamine")
    print("3 - Suurim palk ja omanik")
    print("4 - Koige vaiksem palk ja omanik")
    print("5 - Jarjestada palgad kasvavas ja kahanevas jarjekorras koos nimedega")
    print("6 - Uhhesugused palgad")
    print("7 - Otsi palga jargi")
    print("8 - Palgad suuremad kui")
    print("9 - Palgad vahemad kui")
    print("10 - Keskmine palk")
    v = int(input("Vali tegevus (sisesta 0 lopetamiseks): "))

    if v == 0:
        break  

    elif v == 1:
        k = int(input("Mitu inimest lisame? "))
        inimesed, palgad = Lisamine(inimesed, palgad, k)
        
        for i in range(len(palgad)):
            print(inimesed[i], " saab katte", palgad[i])

    elif v == 2:
        nimi = input("Sisesta inimese nimi, keda soovid eemaldada: ")
        inimesed, palgad = Eemaldamine(inimesed, palgad, nimi)

        for i in range(len(palgad)):
            print(inimesed[i], " saab katte", palgad[i])

    elif v == 3:
        suurim_palk, saajad = SuurimPalk(inimesed, palgad)
        if suurim_palk is not None:
            print(f"Suurim palk on {suurim_palk}, mida saavad: {', '.join(saajad)}")
        else:
            print("Palgad on tuhjad.")

    elif v == 4:
        vaiksem_palk, saajad = KoigeVaiksemPalk(inimesed, palgad)
        if vaiksem_palk is not None:
            print(f"Vaikseim palk on {vaiksem_palk}, mida saavad: {', '.join(saajad)}")
        else:
            print("Palgad on tuhjad.")
            
    elif v == 5:
         a = int(input("Vali jarjestus (1 - tõusev, -1 - kahanev): "))
         SortPalgad(inimesed, palgad, a)

         for i in range(len(palgad)):
             print(inimesed[i], " saab katte", palgad[i])
    
    elif v == 6:
         YhesugusedPalgad(inimesed, palgad)
         

    elif v == 7:
         otsitav_nimi = input("Sisesta inimese nimi: ")
         OtsiPalgaJargi(inimesed, palgad, otsitav_nimi)
   
    elif v == 8:
        limiit = int(input("Sisesta summa: "))
        PalgadSuuremadKui(inimesed, palgad, limiit)
    
    elif v == 9:
        limiit = int(input("Sisesta summa: "))
        PalgadVahemKui(inimesed, palgad, limiit)
        

    elif v == 10:
        keskmine_palk, keskmise_saaja_nimi = Keskmine(inimesed, palgad)
        if keskmine_palk is not None:
            print(f"Keskmine palk on {keskmine_palk}, mida saab {keskmise_saaja_nimi}.")
        else:
            print("Ei saa arvutada keskmist palka, kuna palgad on tyhjad.")
    
     
        

    
    









