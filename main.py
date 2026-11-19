import random 
ordlista = [
    "äpple", "hus", "bil", "hund", "katt",
    "skola", "lärare", "elev", "bok", "penna",
    "bord", "stol", "dator", "mobil", "telefon",
    "fönster", "dörr", "golv", "tak", "vägg",
    "sol", "måne", "stjärna", "himmel", "moln",
    "regn", "snö", "vind", "storm", "åska",
    "vatten", "eld", "luft", "jord", "sten",
    "skog", "träd", "blomma", "gräs", "buske",
    "berg", "sjö", "hav", "flod", "strand",
    "fisk", "fågel", "häst", "ko", "gris",
    "lejon", "tiger", "björn", "varg", "räv",
    "kanin", "mus", "orm", "groda", "fjäril",
    "mat", "bröd", "ost", "mjölk", "smör",
    "kött", "potatis", "morot", "tomat", "gurka",
    "pasta", "ris", "sopa", "pizza", "glass",
    "frukt", "päron", "banan", "apelsin", "citron",
    "dag", "natt", "morgon", "kväll", "vecka",
    "månad", "år", "timme", "minut", "sekund",
    "springa", "hoppa", "simma", "cykla", "gå",
    "äta", "dricka", "sova", "vakna", "läsa",
    "skriva", "räkna", "tänka", "prata", "lyssna",
    "glad", "ledsen", "arg", "trött", "pigg",
    "snabb", "långsam", "stor", "liten", "lång",
    "kort", "stark", "svag", "varm", "kall",
    "röd", "blå", "grön", "gul", "svart",
    "vit", "brun", "rosa", "lila", "orange",
    "vän", "familj", "mamma", "pappa", "syskon",
    "bror", "syster", "barn", "människa", "person",
    "pengar", "arbete", "tid", "kärlek", "glädje",
    "musik", "film", "spel", "sport", "fotboll","handgemäng"
] # det finns 151 st ord :) 


def igen_inmat(txt):
    while True: 
           x = input(txt).lower()
           if x == "j": 
               return 1
           elif x == "n":
               return 2 
           else: 
               print("svara med J/N tack.")
               continue

def inmat(txt):
    while True: 
       x = input(txt).lower()
       if len(x) == 1 and x.isalpha() == True:
           return x
       elif x.isalpha() == False:
           print("Får endast inehålla bokstäver")
           continue
       elif not len(x) == 1:
           print("Får endast inehålla en bokstäver")
           continue
       
# den ska ha säker inmatning bara stor bokstav stor eller liten ^^^^^
# här är huvud programmet som faktist kört saken 
while True:
    fel_gissningar = []
    gissningkvar = 10
    ut_str = ""
    ord = ordlista[random.randint(0,150)].lower()
    ut_str = ["*"] * len(ord)
    while True:
        if "*" not in ut_str:
            print("Grattis du har vunnit !!!!!")
            break
        elif gissningkvar == 0:
            print(f"du har slut på gissningar ordet var {ord}")
            break
        gissning = inmat("gissa gärna bara en bokstav åt gången :D ---->")
        print(f"du har {gissningkvar} felgissningar kavar")
        if gissning in fel_gissningar: # jag lenardo skrev :D yay!!
            print (" det finns redan med en sådan bokstav gissa igen!!")
            continue 
        elif gissning not in ord:
            fel_gissningar.append(gissning)
            print(f"bokstäverna {"".join(fel_gissningar)} finns inte med")
            gissningkvar -= 1
        else:
            for i , bokstav in enumerate(ord):
                if gissning == bokstav:
                    ut_str[i] = gissning
            
        print("".join(ut_str))

    if igen_inmat("har du lust att köra igen  j/n ??? ") == 1:
        continue
    else:
        break
print("Programet avslutades")