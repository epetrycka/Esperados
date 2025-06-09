Saluton

skribi("test wyjatkow")

:O multiExpr

:O int str 
:O skribi(1 subtrahi "a")

:O int float
skribi(1 aldoni 1.5)

:O int bool
skribi(1 aldoni vere)

:O int int

:O int list
variablo listo lista1 asigini [1]
:O skribi(1 aldoni lista1)

:O int dict
variablo vortaro dict asigini {"jeden": 1}
:O skribi(1 subtrahi dict)

:O comparisonExpr
se (7.2 granda 1.5) {
    skribi("ok")
}

:O funcio test(n = 5)

:O additionExpr
:O skribi("a" subtrahi 3)

:O exponExpr
:O skribi("a" intensigi 2)

:O Listy
variablo listo lista asigini [1,2,3]
variablo listo lista2 asigini [1,2,4]
:O lista subtrahi 20
:O lista1 aldoni 1
:O lista1 aldoni (0,1)
:O lista[5] asigini 9
:O skribi(dict["a"])
:O skribi(lista[10])

:O findVariable
:O skribi(x)

:P
por ciu test en tests {
    skribi(test)
}
P:

Adiau