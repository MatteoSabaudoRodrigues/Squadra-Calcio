nomi = []
ruoli = []
forze = []

done = False

squadra = input("Nome della squadra: ")

while not done:
    nome = input("Giocatore: ")
    if nome != "fine":
        nomi.append(nome)

        ruolo = input("Inserisci il ruolo (p - d - a - c): ").lower()

        while ruolo not in ["p", "d", "a", "c"]:
            ruolo = input("Inserisci il ruolo (p - d - a - c): ").lower()

        ruoli.append(ruolo)

        forza = int(input("Inserisci la forza: "))

        while forza < 10 or forza > 99:
            forza = int(input("Inserisci la forza: "))

        forze.append(forza)

    else:
        done = True

# calculate the average strength for each role
media_p = media_d = media_a = media_c = 0
count_p = count_d = count_a = count_c = 0
for ruolo, forza in zip(ruoli, forze):
    if ruolo == "p":
        media_p += forza
        count_p += 1
    elif ruolo == "d":
        media_d += forza
        count_d += 1
    elif ruolo == "a":
        media_a += forza
        count_a += 1
    elif ruolo == "c":
        media_c += forza
        count_c += 1

media_p = media_p / count_p if count_p != 0 else 0
media_d = media_d / count_d if count_d != 0 else 0
media_a = media_a / count_a if count_a != 0 else 0
media_c = media_c / count_c if count_c != 0 else 0

# calculate the minimum and maximum strength for each role
min_p = min_d = min_a = min_c = 0
max_p = max_d = max_a = max_c = 0
for ruolo, forza in zip(ruoli, forze):
    if ruolo == "p":
        if forza < min_p or min_p == 0:
            min_p = forza
        if forza > max_p:
            max_p = forza
    elif ruolo == "d":
        if forza < min_d or min_d == 0:
            min_d = forza
        if forza > max_d:
            max_d = forza
    elif ruolo == "a":
        if forza < min_a or min_a == 0:
            min_a = forza
        if forza > max_a:
            max_a = forza
    elif ruolo == "c":
        if forza < min_c or min_c == 0:
            min_c = forza
        if forza > max_c:
            max_c = forza

#output menu 1
print("\nSquadra: ", squadra)
print("NOME     RUOLO     FORZA")
for n, r, f in zip(nomi, ruoli, forze):
    print("{:<8} {:<8} {:<5}".format(n, r.upper(), f))

#output menu 2
print("\nRUOLO     MEDIA     MIN     MAX     TOT")
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("P", media_p, min_p, max_p, count_p))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("D", media_d, min_d, max_d, count_d))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("A", media_a, min_a, max_a, count_a))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("C", media_c, min_c, max_c, count_c))


#PUNTI TOTALI SQUADRA 1
somma = 0
for elem in forze:
  somma += elem

squadra2 = "Squadra 4ASA"

nomi1 = ["Giovanni", "Carlos", "Albert", "Christian", "Thomas", "Saburri"]
ruoli1 = ["p", "d", "a", "c", "d", "a"]
forze1 = [45, 83, 73, 54, 34, 98]

#PUNTI TOTALI SQUADRA 2
somma2 = 0
for elem in forze1:
  somma2 += elem


if somma > somma2:
  print(f"\nLa squadra {squadra} è più forte della squadra {squadra2}, con un punteggio di: {somma} a {somma2}".format(squadra, squadra2, somma, somma2))
else:
  print(f"\nLa squadra {squadra2} è più forte della squadra {squadra}, con un punteggio di: {somma2} a {somma}".format(squadra2, squadra, somma2, somma))
