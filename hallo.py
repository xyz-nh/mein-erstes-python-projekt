import datetime
import yfinance as yf

symbol = input("Welches Wertpapier-Kürzel möchtest du prüfen? ").upper()
geburtsjahr = int(input("Wann wurdest du geboren? "))

alter = int(datetime.date.today().year-geburtsjahr)

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
    print(f"Fehler: Das Kürzel '{symbol}' konnte nicht gefunden werden oder es gibt ein Netzwerkproblem.")

print(f"Du müsstest jetzt ungefähr {alter} Jahre alt sein.")