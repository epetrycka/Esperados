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

1. Własna składnia z językiem esperanto – zaprojektowana składnia do podstawowych operacji (zmienne, przypisania, warunki, pętle, funkcje, klasy).

2. Wymagane rozpoczęcie definiowania instrukcji programu słowem kluczowym "Saluto", koniec instrukcji programu - "Adiau".

3. Zmienne i typy – możliwość deklaracji globalnych i wewnętrznych zmiennych oraz użycie ich (np. int, string, bool - typ wartości przypisywany automatycznie, możliwe rzutowanie typów).

4. Wypisywanie danych do konsoli (kilka wartości o różnych typach) i pobieranie z kosoli.

5. Instrukcje warunkowe – wsparcie dla if, else, elif.

6. Pętle – while, for, for each - operacje break i continue wewnątrz pętli

7. Funkcje – możliwość definiowania i wywoływania funkcji, zapis wskaźnika do funkcji do zmiennej, zwracanie wartości przez funkcję (lub puste `return`)

8. Komentarze – możliwość dodawania komentarzy blokowych i liniowych.

9. Podstawowe operacje matematyczne i logiczne – dodawanie, odejmowanie etc., porównania, AND/OR/NOT + obsługa kolejności wykonywania działań.

10. Operacje dodawania na stringach.

11. Tworzenie tablic i map - definiowanie indexowanych tablic i map danych.

12. Usuwanie zmiennych z pamięci, zmiana wartości zmiennych (o tym samym typie).

13. Obsługa polskich znaków w konsoli i znaków białych w konsoli (np. '\n').

14. Obsługa błędów składniowych i błędów kompilacji – generowanie błędów, jeśli składnia jest nieprawidłowa.

15. Walidacja parametrów funkcji.

16. Operacje na tablich - replace, insert, add, remove.

17. Operacje na słownikach - replace, add, keys, values.

18. Działanie efektywne rekurencji. 

19. Interfejs CLI – interpreter, który przyjmuje plik .es i uruchamia kod. Kolorowanie składni i numeracja linii.


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

![image](https://github.com/user-attachments/assets/943b4280-3fba-4cc8-ac11-0ab7f19ff9b5)

[more examples](https://github.com/epetrycka/Esperados-SquickLang/tree/main/Examples)

## Uruchamianie programu

W zakładce *realese* dostępna jest najnowsza wersja programu i jego instalatora. 

### Instalacja

1. Należy pobrać plik EsperadosInstallator.exe i uruchomić go.
2. W okienku pojawi się wybór ścieżki do zapisu plików programu.
3. Po zatwierdzeniu program zostanie zainstalowany i automatycznie na pulpicie naszego komputera pojawi się skrót do aplikacji WelcomeToEsperados.exe, w której możemy korzystać z wygodnego interfejsu do obsługi naszego języka.

Jest dostępna możliwość również korzystania z języka z poziomu linii komend. Aby tego użyć należy wykonać następujące kroki:

#### ⚠️ Wymagania:

Zainstalowany Python 3 (dodany do PATH)

Aktywne venv lub zainstalowane wymagane paczki (antlr4, antlr4-python3-runtime, itp.) - pakiet install powinien zrobić to za ciebie.

1. Z zakładki realese pobrać plik Windows.zip lub Linux.zip w zależności od systemu operacyjnego i rozpakować w utworzonym folderze Esperados, wybranym w aplikacji instalatora.

### Windows

1. Wpisać w linii komend otwartej w folderze Esperados:
  
```bash
> ./install.bat
```

2. Wtedy będzie możliwe uruchamianie programu za pomocą komendy:

```bash
> ./esperados.bat example.es
```

4. Lub dodanie tymczasowego aliasu:

```bash
> doskey esperados=esperados.bat $*
```

5. Albo dodanie ścieżki do pliku `esperados.bat` do systemowych zmiennych środowiskowych (Path)

```bash
> esperados example.es
```

### Linux

1. Nadaj prawa do uruchomienia i uruchom skrypt instalatora.

```
chmod +x esperados install.sh
./install.sh
```

2. Uruchamiaj program.

```
./esperados example.es
```

3. Lub dodaj tymczasowy alias.

```
alias esperados="$(pwd)/esperados"
```

5. Albo stały alias.

```
echo 'alias esperados="$(pwd)/esperados"' >> ~/.bashrc
source ~/.bashrc
esperados example.es
```

---

*Życzymy dobrej zabawy podczas korzystania z Esperados!*
