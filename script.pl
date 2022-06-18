#!/usr/bin/swipl

[facts],[rules].

is_child("Daniel Ignacio Useche", "Javier Useche").
is_child("Ana Maria Useche", "Javier Useche").
is_child("Yelitza Paredes", "Irma Silva").

is_brother("Javier Useche", "Albadaniela Useche").
is_brother("Simon Paredes", "Yelitza Paredes").
is_brother("Luis Javier Useche", "Daniel Ignacio Useche").

is_sister("Yuli Paredes", "Julio Paredes").
is_sister("Maria Virginia", "Gabriel").
is_sister("Ana Maria Useche", "Jonathan Javier Useche").

is_grandchild("Sofia", "Ali Ramirez").
is_grandchild("Cesar Manuel Paredes", "Ramon Ignacio Paredes").
is_grandchild("Natalia Lucia Becerra Useche", "Javier Useche").

is_grandfather("Daniel Useche", "Luis Javier Useche").
is_grandfather("Ramon Ignacio Paredes", "Carlos Chuecos").
is_grandfather("Simon Paredes", "Gabriel").

is_grandmother("Yuli Paredes", "Sofia").
is_grandmother("Irma Silva", "Juliana Paredes").
is_grandmother("Yelitza Paredes", "Natalia Lucia Becerra Useche").

is_grandgrandfather("Ramon Ignacio Paredes", "Monserrat").
is_grandgrandfather("Daniel Useche", "Liam Useche").
is_grandgrandfather("Daniel Useche", "Natalia Lucia Becerra Useche").

is_grandgrandmother("Alba Prato", "Liam Useche").
is_grandgrandmother("Irma Silva", "Aranxa").
is_grandgrandmother("Irma Silva", "Sofia").

is_uncle("Jonathan Javier Useche", "Natalia Lucia Becerra Useche").
is_uncle("Javier Useche", "Danyelica Useche").
is_uncle("Julio Paredes", "Jose Ignacio Chuecos").

is_aunt("Albadaniela Useche", "Daniel Ignacio Useche").
is_aunt("Marisabel Paredes", "Daniel Ignacio Useche").
is_aunt("Maria Fernanda Paredes", "Maria Victoria").

is_cousin("Maria Fernanda Paredes", "Daniel Ignacio Useche").
is_cousin("Simon Paredes", "Juliana Paredes").
is_cousin("Luis Javier Useche", "Maria Andrea Paredes").

is_brotherinlaw("Luis Chuecos", "Simon Paredes").
is_brotherinlaw("Ali Ramirez", "Julio Paredes").
is_brotherinlaw("Erick Becerra", "Jonathan Javier Useche").

is_sisterinlaw("Milagros Galvis", "Ana Maria Useche").
is_sisterinlaw("Albadaniela Useche", "Yelitza Paredes").
is_sisterinlaw("Analicia von shritz", "Julio Cesar Chuecos").
halt.
