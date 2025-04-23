:O To jest komentarz jednoliniowy

Saluton

:P
To jest komentarz blokowy
Składa się z wielu linii
P:

variablo x entjero asigini 0
variablo y flosi asigini 1.5
variablo tekst snuro asigini "Cześć"

tutmonda variablo licznik entjero asigini 10

skribi("Witaj", tekst)

por (i; 0; 5; 1) {
  skribi("Iteracja:", i)

  se (i granda egala 2) {
    skribi("i jest większe lub równe 2")
  } alie se (i ne egala 1) {
    skribi("i nie jest równe 1")
  } alie {
    skribi("i to 1")
  }

  gis (i malgranda 2) {
    skribi("Pętla while, i =", i)
    haltu
  }

  daurigi
}

skribi("Koniec pętli")

difini salutu(snuro: nomo){
    skribi("Saluton: ", nomo)
}

funcio salutu (nomo = "Jol")

Adiau
