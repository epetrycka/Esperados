## interpreter.py
Cel: Jest to plik, który zawiera logikę interpretującą (czyli wykonującą) kod w twoim języku. Gdy parser wygeneruje drzewo składniowe, interpreter przekształca je na działający program.

Kiedy go używasz: Gdy chcesz, aby twój język wykonywał instrukcje bez kompilacji do kodu maszynowego. Interpreter wykonuje kod na bieżąco.

## runner.py
Cel: Zwykle zawiera główną funkcję, która uruchamia cały proces analizy i wykonania kodu. Może być odpowiedzialny za otwarcie pliku źródłowego, utworzenie odpowiednich obiektów (lexer, parser, interpreter) i uruchomienie programu.

Kiedy go używasz: Kiedy chcesz uruchomić cały proces z poziomu jednego miejsca, na przykład ładowanie pliku, przetwarzanie go i wykonywanie.

## visitor.py
Cel: Jest to plik, który implementuje wzorzec projektowy "visitor" i służy do przechodzenia przez drzewo składniowe wygenerowane przez parsera. Wzorzec visitor pozwala na dodawanie nowych operacji do drzewa składniowego bez zmiany struktury samego drzewa. W kontekście ANTLR generujesz klasę odwiedzającą (visitor), która wykonuje określone operacje na poszczególnych węzłach drzewa.

Kiedy go używasz: Kiedy chcesz przejść przez drzewo i wykonać operacje na poszczególnych elementach (np. obliczenia, walidację, transformacje).

## main.py
Cel: Plik główny, który uruchamia cały proces od początku do końca. Zwykle zawiera logikę uruchamiania programu i odpowiada za przekazanie pliku źródłowego do odpowiednich komponentów (lexer, parser, interpreter/visitor).

Kiedy go używasz: Kiedy chcesz mieć centralne miejsce, które zarządza uruchomieniem twojego programu i obsługuje wszystkie interakcje między różnymi częściami systemu (lexer, parser, interpreter/visitor).

### Podsumowanie:
interpreter.py – do wykonywania kodu w twoim języku.

runner.py – do uruchamiania całego procesu analizy i wykonania.

visitor.py – do przechodzenia przez drzewo składniowe w celu analizy lub przetwarzania danych.

main.py – główny plik, który łączy wszystko w jeden proces.

## How to execute the grammar?

```
> cd src
> python -m venv venv
> source venv/Scripts/activate
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt

(Download complete binaries from https://www.antlr.org/download/antlr-4.13.2-complete.jar and save in for example in C:/Users/User/ProgramFiles/antlr/)

> curl -O C/Users/User/ProgramFiles/antlr/antlr-4.13.2-complete.jar https://www.antlr.org/download/antlr-4.13.2-complete.jar
> echo 'alias antlr4="java -jar C/Users/User/ProgramFiles/antlr/antlr-4.13.2-complete.jar"' >> ~/.bashrc
> source ~/.bashrc
> cd ../Grammar
> antlr4 -Dlanguage=Python3 -visitor Esperando.g4 -o ../src/generated
> cd ../src
> python main.py
```