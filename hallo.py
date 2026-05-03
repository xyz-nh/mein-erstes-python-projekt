import datetime

name = input("Wie heißt du? ")
geburtsjahr = int(input("Wann wurdest du geboren? "))

alter = int(datetime.date.today().year-geburtsjahr)

print(f"Hallo {name}, willkommen in der Open-Source-Welt!")
print(f"Du müsstest jetzt ungefähr {alter} Jahre alt sein.")