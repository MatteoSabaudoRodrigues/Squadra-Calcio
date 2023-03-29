# Tre liste vuote per salvare tutti i dati presi in input dal programma.

nomi = []
ruoli = []
forze = []

# done è una condizione per uscire dal ciclo infinito per gli input

done = False

squadra = input("Nome della squadra: ")

# Ciclo infinito per ricevere in input i giocatori, ruoli e forze

while True:
  nome = input("\nGiocatore: ")
  if nome.upper() == "FINE":

    # Controllo se ci sono almeno 1 giocatore in ogni ruolo.

    if 'p' in ruoli and 'd' in ruoli and 'c' in ruoli and 'a' in ruoli:
      break

    else:
      print("\n⚠ Comando 'fine' non consentito: prima di terminare l'immissione dei giocatori, assicurati che in ognuno dei 4 ruoli (portiere, difesa, centrocampo, attacco) sia presente almeno 1 giocatore.");
      continue

  nomi.append(nome)

  while True:
    ruolo = input("Inserisci il ruolo (p - d - a - c): ")

    if ruolo in ['p','d','c','a']:
      ruoli.append(ruolo)
      break

  while True:
    forza = int(input("Inserisci la forza (10-99): "))

    if 10 <= forza <= 99:
      forze.append(forza)
      break

# Calcola la media delle forze di ogni giocatore

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

# Calcola il valore max, min per ogni ruolo

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

# Output dei giocatori inseriti in nomi, i suoi ruoli e le forze.
print("\nSquadra: ", squadra)

print("NOME     RUOLO     FORZA")
for n, r, f in zip(nomi, ruoli, forze):
    print("{:<8} {:<8} {:<5}".format(n, r.upper(), f))

# Statistiche finali di ogni ruolo

print("\nRUOLO     MEDIA     MIN     MAX     TOT")
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("P", media_p, min_p, max_p, count_p))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("D", media_d, min_d, max_d, count_d))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("A", media_a, min_a, max_a, count_a))
print("{:<8}  {:<8.2f}  {:<5}   {:<5}   {:<5}".format("C", media_c, min_c, max_c, count_c))


# Somma delle forze inserite nella lista forze[] - Squadra 1
somma = 0
for elem in forze:
  somma += elem

# Seconda squadra inserita dal sistema - pre-definita.

squadra2 = "Squadra The Best"

nomi1 = ["Giovanni", "Carlos", "Albert", "Christian", "Thomas", "Saburri"]
ruoli1 = ["p", "d", "a", "c", "d", "a"]
forze1 = [45, 83, 73, 54, 34, 98]

# Somma delle forze inserite nella lista forze1[] - Squadra 2
somma2 = 0
for elem in forze1:
  somma2 += elem

# Stampa quale squadra è la piu forte in base alla somma delle forze dei giocatori

if somma > somma2:
  print(f"\nLa squadra {squadra} è più forte della squadra {squadra2}, con un punteggio di: {somma} a {somma2}".format(squadra, squadra2, somma, somma2))
else:
  print(f"\nLa squadra {squadra2} è più forte della squadra {squadra}, con un punteggio di: {somma2} a {somma}".format(squadra2, squadra, somma2, somma))
