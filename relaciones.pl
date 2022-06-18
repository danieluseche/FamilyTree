%es_hombre(X).
%es_mujer(Y).
%es_padre(X, Y).
%es_madre(X, Y).
%estan_casados(X, Y).

es_hijo(X,Y):- es_padre(Y,X).
es_hermano(X,Y):- es_hijo(X,Z), es_hijo(Y,Z). 
es_nieto(X,Z):- es_hijo(X,Y), es_hijo(Y,Z).
es_abuelo(X,Z):- es_hijo(Z,Y), es_hijo(Y,X).
es_tio(X,Y):- es_hermano(X,Z), es_hijo(Y,Z).
es_primo(X,Y):- es_hijo(X,Z), es_tio(Z,Y).
es_bisabuelo(X,W):- es_hijo(W, Z), es_hijo(Z, Y), es_hijo(Y, X).  
es_cunado(X, Y):- estan_casados(X, Z), es_mujer(Z), es_hermano(Y, Z).
