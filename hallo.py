from datetime import date, datetime, timedelta
import yfinance as yf
import logging
import pandas as pd

# Erzwingt die Anzeige aller Fehlermeldungen in der Konsole
#logging.basicConfig(level=logging.DEBUG)

symbol = input("Welches Wertpapier? ").upper()
geburtstag = input("Wann wurdest du geboren? [YYYY-MM-DD]")
geburtsjahr = int(geburtstag[:4])
alter = int(date.today().year-geburtsjahr)

heute = date.today()
heute_str = heute.strftime("%Y-%m-%d")
start_datum = geburtstag
ende_datum = heute_str

try:
    # Daten vom Yahoo Finance Server abrufen
    ticker = yf.Ticker(symbol)
    
    # Den aktuellsten Preis aus den 'fast_info' extrahieren
    preis = ticker.fast_info['last_price']
    waehrung = ticker.fast_info['currency']

    # Ergebnis anzeigen
    print("-" * 30)
    print(f"Wertpapier: {symbol}")
    print(f"Aktueller Kurs: {preis:.2f} {waehrung}")
    print("-" * 30)

except Exception as e:
    print(f"Fehler Schritt 1: Das Kürzel '{symbol}' konnte nicht gefunden werden oder es gibt ein Netzwerkproblem.")

try:
    # Daten für diesen Zeitraum abrufen
    # Wir laden einen kleinen Puffer (z.B. 3 Tage), falls das Zieldatum ein Wochenende war
    start = start_datum
    ende = (datetime.strptime(start_datum, "%Y-%m-%d") + timedelta(days=3)).strftime("%Y-%m-%d")

    # Daten abrufen
    try:
        data = yf.download(symbol, start=start, end=ende, threads=False)
    except Exception as e:
        print(f"Fehler Schritt 2: Der Abruf der historischen Daten ging schief ({e})")

    # Den Preis extrahieren
    if not data.empty:
        # Wir nehmen den ersten verfügbaren Handelstag im Ergebnis
        erster_verfuegbarer_tag = data.index[0]
        preis_geburt = data.loc[erster_verfuegbarer_tag, 'Close'][symbol]

        print(f"Kurs von {ticker} am Geburtstag: {preis_geburt:.2f} {waehrung}")
    else:
        print("Keine Daten gefunden. War die Börse vielleicht geschlossen?")

    preis_heute = preis

    investment = 10/preis_geburt*preis_heute

    # Ergebnis anzeigen
    print("-" * 30)
    print(f"Wertpapier: {symbol}")
    print(f"Aktueller Kurs: {preis_heute:.2f} {waehrung}")
    print(f"Heutiger Wert von 10 {waehrung} Investment bei Geburt: {investment:.2f} {waehrung}")
    print("-" * 30)

except Exception as e:
    print(f"Fehler Schritt 3: Die Berechnung ging schief.")

print(f"Du müsstest jetzt ungefähr {alter} Jahre alt sein.")