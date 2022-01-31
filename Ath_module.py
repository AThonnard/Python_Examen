#Dictionay Antwerpen
vertalers_antwerpen = {"Bertha Heinz":{"Moedertaal":"Nederlands","Talen":["Duits", "Italiaans", "Nederlands"],"Beschikbaar":"ja",},
                       "Olga Jansen":{"Moedertaal":"Nederlands","Talen":["Pool", "Russisch", "Nederlands"],"Beschikbaar":"ja"},
                       "Peter Jansen":{"Moedertaal":"Nederlands","Talen":["Duits", "Russisch", "Nederlands", "Engels"],"Beschikbaar":"nee"}
                       }
#Dictionay Limburg
vertalers_limburg = {"Jan Peters":{"Moedertaal":"Nederlands","Talen":["Frans", "Duits", "Spaans","Nederlands"],"Beschikbaar":"nee",},
                     "Claudio Da Franco":{"Moedertaal":"Italiaans","Talen":["Nederlands","Frans", "Italiaans"],"Beschikbaar":"ja",},
                     "Nadia Hermandez":{"Moedertaal":"Nederlands","Talen":["Nederlands", "Spaans", "Engels"],"Beschikbaar":"ja",}
                    }
#functie die bepaalt welke dictionary zal gebruikt worden
def keuze_menu_provincie():
    keuze = input("Bent u van Limburg of Antwerpen?: ")
    if keuze == "Antwerpen":
        lijst_vertalers = vertalers_antwerpen
    else:
        lijst_vertalers = vertalers_limburg

    return lijst_vertalers

#Afprinten menu
def print_menu():
    print("1. Druk op 1 om alle vertalers van jouw provincie te zien.")
    print("2. Druk op 2 om alle beschikbare vertalers te zien.")
    print("3. Druk op 3 om de beschikbare tolks te zien die een bepaalde taal spreken.")
    print("4. Druk op 4 om een tolk toe te voegen.")
    print("5. Druk op 5 om een vertalen te verwijderen. ")
    print("6. Druk op 6 om een taal toe te voegen aan een vertaler.")
    print("7. Druk op 7 om een vertaler te reserveren.")
    print("8. Druk op 8 om een alfabetische gesorteerdelijst te geven van de vertalers die een bepaalde taal spreken.")
    print("9. Druk 9 om het programma te stoppen")
    print("------------------------------------------------------------------------------------------------------------")

#Concatenate van voor- en achternaam vertaler
def vertaler():
    voornaam = input("Geef de voornaam in van de vertaler: ")
    achternaam = input("Geef de achternaam in van de vertaler: ")
    vertaler = voornaam + " " + achternaam
    return vertaler

#toon de vertalers van de gekozen provincie
def toon_vertalers(lijst):
    for key, value in lijst.items():
        print("Naam: ",key, " Moedertaal: ", value["Moedertaal"],"Beschikbaar:", value["Beschikbaar"])
        for taal in value["Talen"]:
            print(taal)
        print("\n")

#lijst die de beschikbare vertalers toont
def beschikbare_vertalers(lijst):
    print("De beschikbare vertaler:s zijn?")
    # we tonen hier de vertalers waar bij beschikbaar 'ja' staat
    for key, value in lijst.items():
        for k,v in value.items():
            res = v
            if res == "ja":
                print("Naam: ", key, " Moedertaal: ", value["Moedertaal"], "Beschikbaar:", value["Beschikbaar"])
                for taal in value["Talen"]:
                    print(taal)
                print("\n")

#functie die beschikbare vertalers laat zien die een bepaalde taal beheersen
def beschikbare_vertaler_met_taal(lijst):
    taal = input("Welke taal moet de bescikbare vertaler kunnen beheersen?: ")
    for key, value in lijst.items():
        for k,v in value.items():
            res = v
            if res == "ja":
                if taal in value["Talen"]:
                    print(f'{key} is beschikbaar en beheerst {taal}')

#check of password correct is
def password(x):
    password = input("Geef uw password in: ")
    while password != "MijnPassword":
        print("Password is niet correct")
        password = input("Geef uw password in: ")
    else:
        print("Password is correct")

#functie om een vertaler toe te voegen
def voeg_vertaler(lijst):
    naam = vertaler()
    moedertaal = input("Geef de moedertaal in van de vertaler: ")
    lijst.update({naam: {"Moedertaal": moedertaal, "Talen": [], "Beschikbaar": ""}})
    print(lijst)

#functie om vertaler te verwijderen uit d elijst
def verwijder_vertaler(lijst):
    naam = vertaler()
    if naam in lijst:
        lijst.pop(naam)
    else:
        print("Vertaler bestaat niet of is niet meer in de lijst.")

# #een taal toevoegen bij talen van een vertaler
# def voeg_taal(lijst):
#     naam = vertaler()
#     taal = input("Welke taal wil je toevoegen?: ")
#     # we checkn of vertaler in lijst is, indien wel, voegen we de taal toe
#     if naam in lijst.keys():
#         print("Vertaler is in lijst")
#         lijst.update(naam: {"Talen"= taal})
#     # foutboodscahp mocht vertaler niet in de lijst zijn
#     else:
#         print("Vertaler is niet in de lijst")

#functie om een vertaler te reserveren
def vertaler_reserveren(lijst):
    naam = vertaler()
    for naam, value in lijst.items():
        for k, v in value.items():
            res = v
            if res == "ja":
                lijst[naam]['Beschikbaar'] = 'nee'
                print(f'{naam} is gereserveerd."')

#functie lijst moedertaal gesorteerd A-Z
def moedertaal_sort(lijst):
    pass

