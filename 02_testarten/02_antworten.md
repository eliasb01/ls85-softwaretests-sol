6a)
Es ist nicht eindeutig, ob mit dem ersten Satz gemeint ist, dass die Funktionen einzeln oder zusammen getestet werden. Es scheint in beiden Fällen nicht vernünftig getestet zu werden. Unit-Test und Integrationstest könnten also fehlen.
Es wird kein vernünftigen Systemtest, sondern nur einmal geschaut, ob das System läuft. Es muss eigentlich alles einmal mit den Anforderungen verglichen wernde.

6b)
Unit-Test: Man weiß nicht, ob alle Funktionen korrekt funktionieren.
Integrationstest: Man weiß nicht, ob die Funktionen nicht nur einzeln, sondern auch zusammen funktionieren.
Systemtest: Man weiß nicht, ob das gesamte System alle Anforderungen erfüllt und fehlerfrei ist.
Ggf. hat das Programm so viele Fehler, dass es gar nicht benutzt werden kann.

6c)
DIe drei Module sollten nach ihrer Implementierung einzeln getestet werden. Sobald eine der Funktionen neu dazukommt, sollte ihr zusammenspiel getestet werden, wenn sie zusammenhängen. Wenn alle implementiert wurden muss ein Systemtest stattfinden, um alles zusammen zu testen. Zum Schluss kommt der Abnahmetest mit den Abnehmern.

6d)
Zunächst ist ein Regressionstest sinnvoll, aber man sollte die späteren Systemtests und den Abnahmetest nicht vernachlässigen.

Tandemaufgabe

| Testart              | Was wird getestet                     | Ziel
-----------------------| --------------------------------------| -----------------------------------------------------------
| Unit-Test            | Einzelne Funktionen/Methoden isoliert | Prüfen, ob kleine Bausteine korrekt funktionieren          
| Integrationstest     | Zusammenspiel mehrerer Module         | Prüfen, ob Komponenten korrekt zusammenarbeiten          
| Systemtest           | Gesamtes System als Einheit           | Prüfen, ob das komplette System funktioniert             
| Abnahmetest          | System aus Sicht des Kunden           | Prüfen, ob Anforderungen erfüllt sind                      
| Regressionstest      | Bestehende Funktionen nach Änderungen | Sicherstellen, dass neue Änderungen nichts kaputt machen  