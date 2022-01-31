from Ath_module import *

while True:
    print_menu()
    keuze = input("Geef uw keuze in: ")
    vertalers = keuze_menu_provincie()
    if keuze == "1":
        toon_vertalers(vertalers)
    elif keuze == "2":
        beschikbare_vertalers(vertalers)
    elif keuze == "3":
        beschikbare_vertaler_met_taal(vertalers)
    elif keuze == "4":
        password(password)
        voeg_vertaler(vertalers)
    elif keuze == "5":
        password(password)
        verwijder_vertaler(vertalers)
    elif keuze == "6":
        voeg_taal(vertalers)
    elif keuze == "7":
        vertaler_reserveren(vertalers)
    elif keuze == "8":
        moedertaal_sort(vertalers)
    elif keuze == "9":
        break
