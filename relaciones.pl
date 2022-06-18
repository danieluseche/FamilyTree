'is_male',
'is_female',
'is_father',
'is_mother',
'are_married'

is_child(X,Y) :- is_father(Y,X); is_mother(Y,X).
is_brother(X,Y):- is_male(X), is_child(X,Z), is_child(Y,Z).
is_sister(X,Y):- is_female(X), is_child(X,Z), is_child(Y,Z).
is_grandchild(X,Z):- is_child(X,Y), is_child(Y,Z).
is_grandfather(X,Y):- is_male(X), is_grandchild(Y,X).
is_grandmother(X,Y):- is_female(X), is_grandchild(Y,X).
is_grandgrandfather(X,Y):- is_male(X), is_child(Y,Z), is_grandchild(Z,X).
is_grandgrandmother(X,Y):- is_female(X), is_child(Y,Z), is_grandchild(Z,X).

is_uncle(X,Y):- is_male(X), is_brother(X,Z), is_child(Y,Z).
is_aunt(X,Y):- is_female(X), is_brother(X,Z), is_child(Y,Z).
is_cousin(X,Y):- is_child(X,Z), (is_aunt(Z,Y); is is_uncle(Z,Y)).

is_brotherinlaw(X,Y):- are_married(X,Z), is_female(Z), is_brother(Y,Z).

es_hijo(X,Y):- es_padre(Y,X).
es_hermano(X,Y):- es_hijo(X,Z), es_hijo(Y,Z). 
es_nieto(X,Z):- es_hijo(X,Y), es_hijo(Y,Z).
es_abuelo(X,Z):- es_hijo(Z,Y), es_hijo(Y,X).
es_tio(X,Y):- es_hermano(X,Z), es_hijo(Y,Z).
es_primo(X,Y):- es_hijo(X,Z), es_tio(Z,Y).
es_bisabuelo(X,W):- es_hijo(W, Z), es_hijo(Z, Y), es_hijo(Y, X).  
es_cunado(X, Y):- estan_casados(X, Z), es_mujer(Z), es_hermano(Y, Z).