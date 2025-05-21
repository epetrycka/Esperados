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

## Spis tokenów - [link](https://github.com/epetrycka/Squick-Lang/blob/main/Grammar/spis_tokenów.md)

## Gramatyka języka - [link](https://github.com/epetrycka/Squick-Lang/blob/main/Grammar/Esperados.g4)

## Wymagania funkcjonalne

1. Własna składnia z językiem esperanto – zaprojektowana składnia do podstawowych operacji (zmienne, przypisania, warunki, pętle, funkcje, klasy). ✅

---

2. Wymagane rozpoczęcie definiowania instrukcji programu słowem kluczowym "Saluto", koniec instrukcji programu - "Adiau".

3. Zmienne i typy – możliwość deklaracji globalnych i wewnętrznych zmiennych oraz użycie ich (np. int, string, bool - typ wartości przypisywany automatycznie).

4. Wypisywanie danych do konsoli.

5. Instrukcje warunkowe – wsparcie dla if, else, elif.

6. Pętle – while, for, for each.

7. Funkcje – możliwość definiowania i wywoływania funkcji (definicje i skrócone - lambda).

8. Komentarze – możliwość dodawania komentarzy.

9. Podstawowe operacje matematyczne i logiczne – dodawanie, odejmowanie etc., porównania, AND/OR/NOT + obsługa kolejności wykonywania działań.

10. Operacje na stringach.

11. Tworzenie tablic i map - definiowanie indexowanych tablic i map danych.

12. Wczytywanie danych z konsoli do programu.

13. Obsługa polskich znaków w konsoli i znaków białych w konsoli (np. '\n').

---

14. Obsługa błędów składniowych i błędów kompilacji – generowanie błędów, jeśli składnia jest nieprawidłowa.

15. Blok try-except-finally - możliwość obsługi błędów wewnątrz programu.

16. Interfejs CLI – interpreter, który przyjmuje plik .es i uruchamia kod.


## Wymagania niefunkcjonalne

1. Język implementacji: Python + pytest do testów

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

difini salutu(snuro: nomo){
    skribi("Saluton, ", nomo)
}

por ciu (variablo en ["Mia", "Eta", "Amiko"]){
    salutu(nomo = variablo)
}

Adiau
```

## Uruchamianie programu

```bash
> cd EsperadosApp
> python -m venv venv
> source venv/Scripts/activate
> python -m pip install --upgrade pip
> python -m pip install -r requirements.txt
> python src/main.py ../Examples/code.es
```

---

> [!IMPORTANT]
> Projekt jest na etapie developmentu

<details>
  <summary><strong>TO DO</strong></summary>

### Gramatyka:
- [ ] Obsługa wartości `NULL` (`nenio`) dla zmiennych.
- [ ] Definiowanie map, lambd.
- [ ] Wyrażenia logiczne z operatorem `IN` (`en`) – sprawdzanie przynależności do listy/mapy/tablicy.
- [ ] Każda instrukcja musi kończyć się znakiem następnej lini.

<sub><i>Opcjonalnie:</i></sub>  
- [ ] Definicje klasy (do rozważenia).
- [ ] Wymuszanie typu zmiennej (np. `string(5)`, `int("56")`).
- [ ] Operator `IS` (`estas`) – sprawdzanie typu zmiennej.
- [ ] Operacje na stringach (`indexOf` itp.).
- [ ] Dodanie niemutowalnych list.
- [ ] Traktowanie kodu przed pierwszym `Saluto` i po `Adiau` jako komentarz (zobaczyć jak użyć modów aby to zadziałało bez przechodzenia parserem).

---

### Visitor (interpretacja):

- [ ] Obsługa wymuszania typu przy definicji i za pomocą funkcji.
- [ ] Implementacja klas i lambd.
- [ ] Obsługa list, map.
- [ ] Wsparcie dla polskich znaków i białych znaków (np. `\n`).
- [ ] Zapisywanie funkcji w scopach, poza scopem nie powinno być do niej dostępu

---

### Error handler:

- [ ] Obsługa błędów bardziej precyzyjnie: invalid token, missing token, syntax error, incomplete sentence, other
- [ ] Walidacja czy element znajduje się w słowniku
- [ ] Sprawdzenie czy wartość jest liczbą ?

</details>