"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Die Formel zur Berechnung der Variable rabatt ist falsch, die Prozentzahl muss durch 100 geteilt werden

# Defect (fehlerhafte Stelle im Code):
# TODO: Die Prozentzahl muss beim Berechnen der Variable rabatt durch 100 geteilt werden

# Failure (was der Benutzer bemerken würde):
# TODO: Der Preis würde immer negativ sein, weil bei dieser Formel rabatt immer größer ist als preis


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    rabatt = preis * (prozent/100)
    return preis - rabatt


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    print(berechne_rabatt_korrigiert(100.0,20))
    print(berechne_rabatt_korrigiert(100.0,50))
    print(berechne_rabatt_korrigiert(300,50))
    print(berechne_rabatt_korrigiert(1,1))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    |    x     |           |
# | Programm mit Testdaten ausführen    |          |    x      |
# | Syntaxprüfung durch den Editor      |    x     |           |
# | Walkthroughs im Team                |    x     |           |
# | Unit-Tests laufen lassen            |          |     x     |
# | Checklisten für Codestruktur        |    x     |           |
#
# Warum reicht statisches Testen allein nicht aus?
# Indem man sich nur den Quellcode anschaut, kann man nicht alle Fehler erkennen. Man kann so nicht wissen, wie das Programm tatsächlich aussieht und läuft


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# Eine Seite oder ein Programm wird mit einem Browser geöffnet und kann nicht richtig geladen werden.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# Stellen mit komplexen Vorgängen (z.B. im ERP-System Eingaben prüfen, ob sie logisch möglich sind) enthalten wahrscheinlich mehrere Fehler als eine lange Stelle in der nur die UI definiert wird.

# Welches Prinzip überrascht dich? Warum?
# Dass so eine große Mehrheit aller Fehler in so einem kleinem Bereich ist. Ich bin davon ausgegangen, dass man bei leichteren Passagen weniger aufpasst und diese schnell fertig haben will und sich deswegen dort auch Fehler einschleichen können. Bei komplizierten Passagen macht man sich mehr Gedanken und vermeidet so Fehler.
