fel_gissningar = []
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
       
print(inmat("skriv"))
# den ska ha säker inmatning bara stor bokstav stor eller liten 












    