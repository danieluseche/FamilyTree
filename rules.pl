is_child(X,Y) :- is_parent(Y,X).
is_brother(X,Y):- \+(X==Y), is_male(X), is_child(X,Z), is_child(Y,Z).
is_sister(X,Y):- \+(X==Y), is_female(X), is_child(X,Z), is_child(Y,Z).
is_grandchild(X,Z):- is_child(X,Y), is_child(Y,Z).
is_grandfather(X,Y):- is_male(X), is_grandchild(Y,X).
is_grandmother(X,Y):- is_female(X), is_grandchild(Y,X).
is_grandgrandfather(X,Y):- is_male(X), is_child(Y,Z), is_grandchild(Z,X).
is_grandgrandmother(X,Y):- is_female(X), is_child(Y,Z), is_grandchild(Z,X).

is_uncle(X,Y):- is_male(X), is_brother(X,Z), is_child(Y,Z).
is_aunt(X,Y):- is_female(X), is_sister(X,Z), is_child(Y,Z).
is_cousin(X,Y):- is_child(X,Z), (is_aunt(Z,Y); is_uncle(Z,Y)).

is_brotherinlaw(X,Y):- is_male(X), are_married(X,Z), (is_brother(Y,Z);  is_sister(Y,Z)).
is_sisterinlaw(X,Y):- is_female(X), are_married(X,Z), (is_brother(Y,Z);  is_sister(Y,Z)).
