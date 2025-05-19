Saluton

skribi("hej")

difini salutu (nomo) {
    skribi("Saluton: ", nomo)

    difini name (name2){
        variablo y asigini 5 
        reveni (" Hej " aldoni name2)
    }
    variablo name asigini funcio name (name2 = "Aha")

    skribi("Lol", name)
}

funcio salutu (nomo = "Jol")

difini test(n){
    variablo x asigini n 
    se (n granda 0){
        funcio test(n = n subtrahi 1)
    }
    skribi(x)
}

funcio test(n = 5)

difini silnia (n){
    se (n egala 0) {
        reveni 1
    } alie {
        reveni n multigi funcio silnia(n = n subtrahi 1)
    }
}

variablo wynik asigini funcio silnia(n = 5, n = 7, i = 70)

skribi(wynik)

Adiau