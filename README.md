# Esperados - projekt w ramach zajęć Teoria kompilacji i kompilatory

Projekt ma na celu stworzenie własnego języka programowania, z użyciem słów kluczowych w języku esperanto. 
Język ma być łatwy w użyciu i możliwie najprostszy do zrozumienia.

<details>
  <summary>Autorzy</summary>
    <br>Eliza Petrycka (epetrycka@student.agh.edu.pl)
    <br>Dominika Bujnarowska (dbujnarowska@student.agh.edu.pl)
</details>

## Opis

Projekt zakłada stworzenie gramatyki i interpretera języka Esperados, który parsuje kod źródłowy napisany w Esperados i wykonuje go w czasie rzeczywistym. Interpreter będzie zaimplementowany w języku Python z wykorzystaniem narzędzia ANTLR4 do generowania skanera i parsera na podstawie zdefiniowanej gramatyki.

## Wybranie technologie

* Python - język implementacji interpretera
* ANTLR4 - generator skanerów i parserów
* pytest - narzędzie do testów

## Spis tokenów - [link](https://github.com/epetrycka/Squick-Lang/blob/main/spis_tokenów.md)

## Gramatyka języka - [link](https://github.com/epetrycka/Squick-Lang/blob/main/Grammar/Esperados.g4)

## Wymagania funkcjonalne

1. Własna składnia z językiem esperanto – zaprojektowana składnia do podstawowych operacji (zmienne, przypisania, warunki, pętle, funkcje, klasy).

2. Wymagane rozpoczęcie definiowania instrukcji programu słowem kluczowym "Saluto", koniec instrukcji programu - "Adiau".

3. Zmienne i typy – możliwość deklaracji globalnych i wewnętrznych zaminneych oraz użycie ich (np. int, string, bool).

4. Instrukcje warunkowe – wsparcie dla if, else, elif.

5. Pętle – while, for.

6. Funkcje – możliwość definiowania i wywoływania funkcji (definicje i skrócone - lambda).

7. Komentarze – możliwość dodawania komentarzy.

8. Podstawowe operacje matematyczne i logiczne – dodawanie, odejmowanie etc., porównania, AND/OR/NOT.

9. Operacje na stringach - dodawanie stringów.

10. Blok try-except-finally - możliwość obsługi błędów wewnątrz programu.

11. Tworzenie tablic i map - definiowanie indexowanych tablic i map dla danych.

12. Obsługa błędów składniowych i błędów kompilacji– generowanie błędów, jeśli składnia jest nieprawidłowa.

13. Interfejs CLI – interpreter, który przyjmuje plik .esp i uruchamia kod.

## Wymagania niefunkcjonalne

1. Język implementacji: Python + pytests dla testów

2. Użycie narzędzia ANTLR4.

3. Czytelność kodu źródłowego – składnia języka Esperados powinna być zrozumiała dla człowieka.

4. Dokumentacja składni – język ma zdefiniowaną gramtykę BNF w pliku Esperados.g4.

5. Zgodność z konwencjami kodowania – styl kodu podobny do GoLang (znak końca linii kończy instrukcję, bloki if/def/for zapakowane w nawiasy klamrowe '{}').

6. Szybkość działania nie jest kluczowa – nacisk na poprawność, nie wydajność.

7. Użycie maksymalnej ilości słów kluczowych zrozumiałych w języku esperanto (minimalizacja używania symboli).

---

## Code Example

```esperando
Saluton

difini salutu(nomo: snuro):
    reveni("Saluton, " + nomo)

por variablo en ["Mia", "Eta", "Amiko"]:
    salutu(variablo)

Adiau
```

## Uruchamianie programu

```bash
py src/main.py Examples/code.es
```

---

> [!IMPORTANT]
> Projekt jest na etapie developmentu