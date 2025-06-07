Saluton

variablo a asigini 5
tutmonda variablo b asigini 10
variablo c asigini 5

skribi(a egala c)        :O True
skribi(a ne egala b)        :O True
skribi(a malgranda b)         :O True
skribi(a malgranda egala c)        :O True
skribi(b granda a)         :O True
skribi(b granda egala c)        :O True

skribi(vere kaj malvero)              :O False
skribi(vere au malvero)               :O True
skribi(ne malvero)                   :O True
skribi(ne (a egala b))                :O True
skribi((a egala c) kaj (b granda a))        :O True
skribi((a ne egala b) au (b malgranda a))         :O True
skribi(ne ((a granda b) au (b ne egala c)))   :O True
skribi((a egala c) kaj ne (b egala c))   :O True
skribi((a malgranda b) au (b malgranda a))          :O True
skribi((a egala b) au (c egala 5))        :O True

variablo x asigini vere
tutmonda variablo y asigini malvero

skribi(x kaj y)                 :O False
skribi(x au y)                  :O True
skribi(ne x)                   :O False
skribi(ne y)                   :O True
skribi(x kaj ne y)             :O True
skribi((x au y) kaj (ne y))    :O True
skribi((vere au malvero) kaj y)  :O False
skribi(vere au (malvero kaj y))  :O True

:O Operacje na liczbach całkowitych jako warunki logiczne (powinny działać jak w Pythonie - niezero = True)
skribi(5 kaj 3)                 :O 3
skribi(0 kaj 3)                 :O 0
skribi(0 au 4)                  :O 4
skribi(2 au 0)                  :O 2
skribi(ne 0)                   :O True
skribi(ne 1)                   :O False
skribi(ne (0 au 0))            :O True
skribi(ne (1 kaj 1))           :O False

:O Mieszanie typów (bool i int)
tutmonda variablo m asigini vere
variablo k asigini 0

skribi(m kaj k)                 :O 0
skribi(k au m)                  :O True
skribi(ne (m kaj k))           :O True

:O Mieszanie typów (int i float)
variablo f asigini 5
variablo g asigini 5.8

skribi(f malgranda g)           :O True #FIXME
skribi(f granda egala g)        :O False #FIXME
skribi(f egala g)               :O False #FIXME
skribi(f ne egala g)            :O True #FIXME
skribi(g kaj malvero)           :O False
skribi(g ne egala "string")     :O True
skribi(ne "Halo")               :O True

Adiau