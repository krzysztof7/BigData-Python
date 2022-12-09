"""
 * Stwórz 2 zmiennie: firstname i surname, które będą zawierać Twoje imię i nazwisko.
 * Połącz te zmiennie w takim sposób, żeby były rozdzielone spacją i zapisz wynik do zmiennej fullname.
 * Wykorzystaj f-string i wyświetl na ekran zawartość zmiennej fullname, w taki sposób, żeby zawartość zmiennej była poprzedzona słowami "Nazywam się ".
 * Wyświetl sumaryczną długość zmiennych firstname i surname. 
"""

firstname = "Krzysztof"
surname = "Piotrowski"

fullname = firstname + ' ' + surname

print(fullname)
print(f"Nazywam się {fullname}.")
print(len(firstname)+len(surname))
print(f"Nazywam się {firstname} {surname}.")

print(firstname.lower())

print("Nazywam się %s %s" % (firstname, surname))


